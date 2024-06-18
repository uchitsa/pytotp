[![Hits-of-Code](https://hitsofcode.com/github/uchitsa/pytotp?branch=main)](https://hitsofcode.com/github/uchitsa/pytotp/view?branch=main)
## Python TOTP 2FA

### Usage:

* create a direcrory for TOTP keys mkdir -p ~/.config/pytotp

* gpg --yes --batch --passphrase 'Some-words' --quick-generate-key "Py TOTP"

* gpg -e -r "Py TOTP" >~/.config/pytotp/<SERVID>.gpg

* python3 pytotp.py <SERVID>
