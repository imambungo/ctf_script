#!/usr/bin/env python3

import subprocess
import hashlib, binascii

# https://stackoverflow.com/a/58037245/9157799
def shell_cmd(COMMAND):
    RUN_COMMAND = 'bash -c "source ~/.sharedsources && ' + COMMAND + '"'
    STDOUT = subprocess.getoutput(RUN_COMMAND)
    return STDOUT


# check if proposed password match the given hash
def is_password_match_hash256(PASSWORD, HASH):
    PASSWORD_HASH = hash256(PASSWORD)

    result = HASH == PASSWORD_HASH
    if result:
        exit(0)
    exit(1)


def hash256(PASSWORD):
    data = PASSWORD.encode('utf8')
    sha256hash = hashlib.sha256(data).digest()
    PASSWORD_HASH = binascii.hexlify(sha256hash).decode("utf-8")
    return PASSWORD_HASH
