#!/usr/bin/env python3
import os
import argparse

import pandas as pd 

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help="input filename", required=True)
parser.add_argument('-o', '--output', help="output filename", required=True)
parser.add_argument('-r', '--root', help="root filepath to read / write the files from", default="/data")
args = parser.parse_args() 

uplead = pd.read_csv(os.path.join(args.root, args.input))

airtable = uplead[['LastName', 'FirstName', 'Email', 'CompanyName', 'Title', 'Website']].copy()
airtable = airtable.rename(index=str, columns={"LastName": "Last name", "FirstName": "First name", "CompanyName": "Organization", "Title": "Job title"})
airtable.loc[:, "Contact stage"] = 'Contact not initiated'
airtable.loc[:, "QA'd"] = 'No'
airtable.loc[:, "QA'd by"] = None
airtable.loc[:, "Source of contact info"] = "UpLead"
airtable.loc[:, "Notes"] = None
path = os.path.join(args.root, args.output)
airtable.to_csv(path, index=False)

print("exported translated file to " + args.output)

