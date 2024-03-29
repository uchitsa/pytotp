#!/usr/bin/env python
"""
Put TOTP key for service SERVID to GPG file crypted for 'Py TOTP'
  gpg -e -r 'Py TOTP' > ~/.config/pytotp/SERVID.gpg
"""

import subprocess
import os
import sys
import time
from datetime import datetime

KEYDIR = os.path.expanduser('~/.config/pytotp')
KEYEXT = '.gpg'
SERVID = sys.argv[1]

if not SERVID:
    print("Usage: {} SERVID\n\tSERVID is a service ID, abbreviated, w/o ext:".format(sys.argv[0]))
    available_keys = [f.replace(KEYDIR + '/', '').replace(KEYEXT, '') for f in os.listdir(KEYDIR) if f.endswith(KEYEXT)]
    print('\n'.join(available_keys))
    exit(2)

key_file = os.path.join(KEYDIR, SERVID + KEYEXT)
if not os.path.isfile(key_file):
    print("No key for {}".format(key_file))
    exit(1)

skey = subprocess.check_output(['gpg', '-d', '--quiet', key_file]).decode('utf-8').strip()

now_seconds = datetime.now().second
wait_time = 60 - now_seconds
if wait_time > 30:
    wait_time -= 30

print("Seconds: {} (wait {}) ...".format(now_seconds, wait_time))
time.sleep(wait_time)

totp = subprocess.check_output(['oathtool', '-b', '--totp', '-'], input=skey.encode('utf-8')).decode('utf-8').strip()

print(totp)
skey = "none"

exit(0)
