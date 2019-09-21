#!/usr/bin/env python3

import subprocess

# https://stackoverflow.com/a/58037245/9157799
def shell_cmd(COMMAND):
    RUN_COMMAND = 'bash -c "source ~/.sharedsources && ' + COMMAND + '"'
    STDOUT = subprocess.getoutput(RUN_COMMAND)
    return STDOUT


shell_cmd('tts hello world!')
