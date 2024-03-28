## Python TOTP 2FA

### Usage:

* create a direcrory for TOTP keys mkdir -p ~/.config/mytotp

* gpg --yes --batch --passphrase 'Some-words' --quick-generate-key "My TOTP"

* gpg -e -r "My TOTP" >~/.config/mytotp/<SERVID>.gpg

* python3 mytotp.sh <SERVID>
