# uplead-ci-airtable-translator


Usage: 

```bash
$ ls -l
-rw-r--r--@ 1 sudoguest  staff  1673 May  9 10:10 UpLead_05-09-2019.csv
$ docker pull 10forward/uplead-ci-airtable
$ docker run -v $(pwd):/data 10forward/uplead-ci-airtable -i UpLead_05-09-2019.csv -o airtable-ci.csv
exported translated file to /airtable-ci.csv
$ ls -l
-rw-r--r--  1 sudoguest  staff  406 May  9 11:00 airtable-ci.csv
-rw-r--r--@ 1 sudoguest  staff  1673 May  9 10:10 UpLead_05-09-2019.csv
```