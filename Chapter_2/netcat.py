"""
Replacing Netcat
"""

import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    output = subprocess.check_output(
        shlex.split(cmd),
        stderr=subprocess.STDOUT
        )
    return output.decode()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='BHP Net Tool',
        
    )