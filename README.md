# Django app to get records from NAT API 



## Description
This Django app allows the user to get a record from The National Archives (TNA) API using record ID. It's assumed the user already has the record ID. 
A user types the record ID into a textbox and then the app gets the corresponding record from the TAN API and presents the user information about that record based on some predefined rules:
1.  Given a valid record ID is specified when the client is run and the returned record’s ‘title’ is not null Then the record’s ‘title’ should be displayed
2. Given a valid record ID is specified when the client is run and the returned record’s ‘title’ is null and the returned record’s ‘scopeContent. description’ is not null then the record’s ‘scopeContent. description’ should be displayed
3. Given a valid record ID is specified
When the client is run
And the returned record’s ‘title’ is null
And the returned record’s ‘scopeContent. description’ is null And the returned record’s ‘citablereference’ is not null
Then the record’s ‘citablereference’ should be displayed
4. Given a valid record ID is specified
When the client is run
And the returned record’s ‘title’ is null
And the returned record’s ‘scopeContent. description’ is null And the returned record’s ‘citablereference’ is null
Then a message ‘not sufficient information’ should be displayed
5. Given an invalid record ID is specified
When the client is run
Then a message ‘no record found’ should be displayed

## Getting Started
This Django app requires some libraries and they are listed in the file requirements.txt. 
Please follow the installation steps below to install the app using a virtual environment. 

## Main Dependencies
Python 3 (Tested with Python 3.8.2) \
Django 

## Installation

### Install Django and python dependencies
```
mkdir TNA
cd TNA
git init
git pull https://github.com/pavlosant/TNA_API.git
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
```

## Execution
After finishing the above installation steps run the Django server from within the TNA directory created in the installation process above:

```
cd TNA
python manage.py runserver
```

Go to `http://127.0.0.1:5000/` or `http://localhost:5000/` \
Click on VCF_upload from navigation menu. This will take you to `http://localhost:5000/api/upload` \
Select a VCF file from your computer or select the example vcf within the repository in the directory `./test_vcf/homo_sapiens_GRCh38.vcf` 

Click Submit. This will post your VCF to server and upload it for VEP. The VEP container starts running with this input VCF. \
Wait until the VEP container completes and the annotations will be presented as json in the same window at `http://localhost/api/annotations`.\
Do not refresh or leave the window after pressing Submit while VEP is running. \
If you do leave the window or close it by accident, you can still find the annotations after a few minutes at:

`http://localhost/api/annotations`

Press `Ctrl-C` when you wish to stop the flask server from running. 

## API execution examples using curl
From the same directory (vep_api):

### Upload VCF - POST
```
curl -F "file=@test_vcf/homo_sapiens_GRCh38.vcf" http://127.0.0.1:5000/api/upload 

Response:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/api/annotations">/api/annotations</a>. If not click the link.
```
# View annotations - GET
```
curl http://127.0.0.1:5000/api/annotations

Response:
{"VEP_version":"v104.3","run_date":"2021-06-09 18:09:13","results":[{"#Uploaded_variation":"rs7289170","Location":{"chromosome":"22","start":"17181903","end":"17181903"},"Allele":"G","Gene":"ENSG00000093072","Feature":"ENST00000262607","Feature_type":"Transcript","Consequence":"synonymous_variant","cDNA_position":"1571","CDS_position":"1359","Protein_position":"453","Amino_acids":"Y","Codons":"taT/taC","Existing_variation":"-","Extra":"IMPACT=LOW;STRAND=-1"},{"#Uploaded_variation":"rs7289170","Location":{"chromosome":"22","start":"17181903","end":"17181903"},"Allele":"G","Gene":"ENSG00000093072","Feature":"ENST00000330232","Feature_type":"Transcript","Consequence":"synonymous_variant","cDNA_position":"841","CDS_position":"636","Protei...}
```
## Testing 
The unittest python package for tests was used and the tests can be executed using:
```
python manage.py test

```
## Authors
`Pavlos Antoniou @pavlosant`

