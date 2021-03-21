import argparse
import hashlib
import hmac
import logging
import os
import struct
import subprocess

import anyio
from anynet import http

from nintendo import nnas
from nintendo.games import SMM
from nintendo.nex import backend, datastore_smm as datastore, settings

logging.basicConfig(level=logging.DEBUG)

DEVICE_ID = int(os.environ["DEVICE_ID"])  # From MCP_GetDeviceId
SERIAL_NUMBER = os.environ["SERIAL_NUMBER"]
SYSTEM_VERSION = 0x260
REGION_ID = 4  # EUR
COUNTRY_ID = 97  # PL
COUNTRY_NAME = "PL"
LANGUAGE_ID = 1  # en
LANGUAGE = "en"

USERNAME = os.environ["NN_USERNAME"]  # Nintendo Network ID
PASSWORD = os.environ["NN_PASSWORD"]  # Nintendo Network password

ASH0_DECOMPRESSOR_PATH = os.environ["ASH0_DECOMPRESSOR_PATH"]
ASH0_HEADER = b"ASH0"

# note that you still need sound.bwv, but it's (almost?) always the same – so can be taken from any other level
FILENAMES = [
    "thumbnail0.tnl",
    "course_data.cdt",
    "course_data_sub.cdt",
    "thumbnail1.tnl",
]


def decompress_and_save_ash(ash, filename):
    ash_filename = f"{filename}.ash0"
    with open(ash_filename, "wb") as fp:
        fp.write(ASH0_HEADER)
        fp.write(ash)

    subprocess.check_output([ASH0_DECOMPRESSOR_PATH, ash_filename, filename])
    os.remove(ash_filename)


def data_id_from_course_id(course_id):
    checksum_orig, zeros, part1, part2 = course_id.split("-")
    return int(part1 + part2, base=16)


def checksum_course_id(course_id):
    key = hashlib.md5(SMM.ACCESS_KEY.encode("utf-8")).digest()
    data = struct.pack("<Q", data_id_from_course_id(course_id))
    checksum = hmac.HMAC(key, data, digestmod=hashlib.md5).digest()

    return checksum[3:1:-1].hex().upper()


async def main(args):
    nas = nnas.NNASClient()
    nas.set_device(DEVICE_ID, SERIAL_NUMBER, SYSTEM_VERSION)
    nas.set_title(SMM.TITLE_ID_EUR, SMM.LATEST_VERSION)
    nas.set_locale(REGION_ID, COUNTRY_NAME, LANGUAGE)

    access_token = await nas.login(USERNAME, PASSWORD)
    nex_token = await nas.get_nex_token(access_token.token, SMM.GAME_SERVER_ID)

    s = settings.default()
    s.configure(SMM.ACCESS_KEY, SMM.NEX_VERSION)
    async with backend.connect(s, nex_token.host, nex_token.port) as be:
        async with be.login(str(nex_token.pid), nex_token.password) as client:
            store = datastore.DataStoreClientSMM(client)

            get_param = datastore.DataStorePrepareGetParam()
            data_id = data_id_from_course_id(args.course_id)
            get_param.data_id = data_id

            req_info = await store.prepare_get_object(get_param)
            headers = {header.key: header.value for header in req_info.headers}
            response = await http.get(req_info.url, headers=headers)
            response.raise_if_error()

            ashes = response.body.split(ASH0_HEADER)[1:]
            target_dir = os.path.join("dump", args.course_id[-9:])
            os.makedirs(target_dir, exist_ok=True)
            for filename, ash in zip(FILENAMES, ashes):
                decompress_and_save_ash(ash, os.path.join(target_dir, filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--course-id", action="store", required=True)
    anyio.run(main, parser.parse_args())
