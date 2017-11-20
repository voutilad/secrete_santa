# Secrete Santa Mailer

This is just a script for mass mailing secret santa stuff.

## Requirements
1) Friends(?)
2) Python3 _(Not tested with Py2, but should be tweakable for it.)_
3) Gmail account configured for SMTP access

## Usage
Simple!

```
usage: sendmail.py [-h] -i INPUT_CSV -u FROM_ADDRESS [-d DELIMITER]
                   [-q QUOTE_CHAR]

Bulk emailer for JCSanta!

optional arguments:
  -h, --help       show this help message and exit
  -i INPUT_CSV     path to 2 column csv with columns: [to, assignment, address]
  -u FROM_ADDRESS  gmail user/email for sending email via SMTP
  -d DELIMITER     csv delimiter (default: ','
  -q QUOTE_CHAR    csv quote character (default: '"')
```
