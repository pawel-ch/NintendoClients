
#===== Wii U Games =====#

class Friends:
	TITLE_ID_EUR = 0x10001C00
	TITLE_ID_USA = 0x10001C00
	TITLE_ID_JAP = 0x10001C00
	LATEST_VERSION = 0
	
	GAME_SERVER_ID = 0x3200
	ACCESS_KEY = "ridfebb9"
	NEX_VERSION = 20000

class DKCTF:
	TITLE_ID_EUR = 0x0005000010138300
	TITLE_ID_USA = 0x0005000010137F00
	TITLE_ID_JAP = 0x0005000010144800
	LATEST_VERSION = 17
	
	GAME_SERVER_ID = 0x10144800
	ACCESS_KEY = "7fcf384a"
	NEX_VERSION = 30400 #3.4.0
	SERVER_VERSION = 3
	
class MK8:
	TITLE_ID_EUR = 0x000500001010ED00
	TITLE_ID_USA = 0x000500001010EC00
	TITLE_ID_JAP = 0x000500001010EB00
	LATEST_VERSION = 64
	
	GAME_SERVER_ID = 0x1010EB00
	ACCESS_KEY = "25dbf96a"
	NEX_VERSION = 30504 #3.5.4 (AMK patch)
	SERVER_VERSION = 2002
	
class SMM:
	TITLE_ID_EUR = 0x000500001018DD00
	TITLE_ID_USA = 0x000500001018DC00
	TITLE_ID_JAP = 0x000500001018DB00
	LATEST_VERSION = 272
	
	GAME_SERVER_ID = 0x1018DB00
	ACCESS_KEY = "9f2b4678"
	NEX_VERSION = 30810 #3.8.10 (AMA patch)
	SERVER_VERSION = 3017
	

#===== Switch Games =====#

class CaveStory:
	GAME_SERVER_ID = 0x2BA73000
	ACCESS_KEY = "c2a631ad"
	NEX_VERSION = 40003 #4.0.3
	
class DQBuilders:
	GAME_SERVER_ID = 0x2CD9DB00
	ACCESS_KEY = "e720a303"
	NEX_VERSION = 40003 #4.0.3

class MK8Deluxe:
	GAME_SERVER_ID = 0x2B309E01
	ACCESS_KEY = "09c1c475"
	NEX_VERSION = 40007 #4.0.7 (apptrbs)

class SMO:
	GAME_SERVER_ID = 0x255BA201
	ACCESS_KEY = "afef0ecf"
	NEX_VERSION = 40302 #4.3.2
	
class Tetris99:
	TITLE_ID = 0x010040600C5CE000
	TITLE_VERSION = 0x50000
	
	GAME_SERVER_ID = 0x23BDA200
	ACCESS_KEY = "cdd6114d"
	NEX_VERSION = 40600 #4.6.4 (app99)
	CLIENT_VERSION = 5
	
class Splatoon2:
	PIA_VERSION = 50901
	PIA_APP_VERSION = 60
	PIA_KEY = bytes.fromhex("ee182a63e216cdb1f51ad4bed8cf6508")
	
class SMM2:
	TITLE_ID = 0x01009B90006DC000
	TITLE_VERSION = 0x30000
	
	GAME_SERVER_ID = 0x22306D00
	ACCESS_KEY = "fdf6617f"
	NEX_VERSION = 40605 #4.6.18 (appslop)
	CLIENT_VERSION = 52
	
	PIA_VERSION = 51800
	PIA_APP_VERSION = 3
	PIA_KEY = bytes.fromhex("667c18475889faab61f93ef1da180971")
