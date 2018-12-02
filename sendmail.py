#!/usr/bin/env python
"""
Mass mail secret santa assignments! Ho ho ho!
"""
import argparse
import csv
import datetime
import sys

from getpass import getpass
from email.message import EmailMessage
from smtplib import SMTP_SSL

SMTP_HOST = "smtp.gmail.com"
YEAR = datetime.datetime.now().year
MSG = """Ho ho ho!

Your {year} Secrete Santa assignment is:

\t{assignment}
\t{address}

Please remember to try to send your gift in time for the holidays!

Remember the rules!

1) Have zero expectations of receiving anything of quality or value
   (Corollary: Spend as much or as little as you want)
2) Share what you receive via email blast with PICS or GTFO
3) Try to get your stuff shipped before XxxMass and/or Channukah/Hannuka/
   Hakunamattata and/or Kwanza
4) No loafing
5) You don't have to remain anonymous, but it's more fun that way.
6) Do not collect a week's worth of urine in a Jose Cuervo bottle and gift it.
   The USPS frowns upon shipping liquids.

If you have any questions, reply to this email. Hopefully I read it.

If you do not receive a gift by Dec 31, please email me!

Ho ho ho,
JCSecreteSanta {year}
"""
SUBJECT = "Your JC Secrete Santa {year} assignment!".format(year=YEAR)

def new_message(to_email, from_email, assignment, address):
    m = EmailMessage()
    m["To"] = to_email
    m["From"] = from_email
    m["Subject"] = SUBJECT
    m.set_content(MSG.format(assignment=assignment,
                             address=address.replace("\n", "\n\t"),
                             year=YEAR))
    return m

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk emailer for JCSanta!")
    parser.add_argument("-i", dest="input_csv", required=True,
                        help="path to 3 column csv with columns: "
                        "[to, assignment, address]")
    parser.add_argument("-u", dest="from_address", required=True,
                        help="gmail user/email for sending email via SMTP")
    parser.add_argument("-d", dest="delimiter", default="\"",
                        help="csv delimiter (default: ','")
    parser.add_argument("-q", dest="quote_char", default="\"",
                        help="csv quote character (default: '\"')")
    args = vars(parser.parse_args())

    print("...parsing {csv}".format(csv=args["input_csv"]))
    with open(args["input_csv"], "r") as csv_file:
        reader = csv.DictReader(csv_file)

        print("...connecting to {host}".format(host=SMTP_HOST))
        with SMTP_SSL(SMTP_HOST) as smtp:
            print("...logging in with user {user}".format(user=args["from_address"]))
            smtp.login(args["from_address"],
                       getpass("{u} Password: ".format(u=args["from_address"])))

            print("...mailing...")
            cnt = 0
            for row in reader:
                try:
                    message = new_message(row["to"], args["from_address"],
                                      row["assignment"], row["address"])
                    smtp.send_message(message)
                    cnt = cnt + 1
                except:
                    print("Failed to send to: {to}".format(row['to']), file=sys.stderr)

            print("...done! Sent {n} emails.".format(n=cnt))
            smtp.quit()
