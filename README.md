# uplead-ci-airtable-translator

This script will read an exported UpLead csv of leads and grab all the relevant columns for the Customer Illuminated Airtable template. 

## flags

```bash
$ ./translate_uplead_to_ci.py -h
usage: translate_uplead_to_ci.py [-h] -i INPUT -o OUTPUT [-r ROOT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input filename
  -o OUTPUT, --output OUTPUT
                        output filename
  -r ROOT, --root ROOT  root filepath to read / write the files from
```

It has a dependency on pandas, so feel free to pull the [docker image](https://hub.docker.com/u/10forward/uplead-ci-airtable) to run the script. 

## docker usage

The docker image will look for the input file (`-i`) in the `/data/` directory in its container, so mount a folder with your exported leads to `/data`. The processed file (filename denoted by `-o`) will also be written into that mounted directory. 

Usage: 

```bash
$ ls
UpLead_05-09-2019.csv
$ docker pull 10forward/uplead-ci-airtable
$ docker run -v $(pwd):/data 10forward/uplead-ci-airtable -i UpLead_05-09-2019.csv -o airtable-ci.csv
exported translated file to /airtable-ci.csv
$ ls -l
airtable-ci.csv
UpLead_05-09-2019.csv
```
