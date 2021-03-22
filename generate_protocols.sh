#!/usr/bin/env bash
pipenv run python generate_protocols.py
pipenv run black .