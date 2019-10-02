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
    data = PASSWORD.encode('utf8')
    sha256hash = hashlib.sha256(data).digest()
    PASSWORD_HASH = binascii.hexlify(sha256hash).decode("utf-8")
    result = HASH == PASSWORD_HASH
    print(result)
    if result:
        exit(0)
    exit(1)
