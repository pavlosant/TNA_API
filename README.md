# Django app to get records from NAT API 



## Description
This Django app allows the user to get a record from The National Archives (TNA) API using a record ID. It's assumed the user already knows the record ID. 
A user types the record ID into a textbox and then the app gets the corresponding record from the TNA API and presents the user information about that record based on some predefined rules:
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
This Django app requires additional python libraries which are listed in the file requirements.txt. 
Please follow the installation steps below to install the app using a virtual environment. 

## Main Dependencies

Python 3 (Tested with Python 3.8.2) \
Django 4 (Tested with Django v 4.0.4)

## Installation

### Install Django and python dependencies
Open a linux or mac terminal and type the following:

```
mkdir TNA
cd TNA
git init
git pull https://github.com/pavlosant/TNA_API.git
pip install --upgrade pip #this is to update to latest version because earlier versions on mac failed to install the cryptography package 
python3 -m venv venv 
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate # required to build database models before running the server
```

## Execution
After finishing the above installation steps run the Django server from within the TNA directory created in the installation process above:

```
#make sure you are in the TNA directory (cd TNA)
python manage.py runserver
```
You will see something similar to the following in your terminal:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 28, 2022 - 13:22:13
Django version 4.0.4, using settings 'tnaapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open your favourite web browser and go to `http://127.0.0.1:8000/` or `http://localhost:8000/` \

The home page of the django web app will be displayed.
![Screenshot](img/home.png?raw=true "Screenshot of home page")

Type or paste the record ID to the textbox (for example use "251cd289-2f0d-48fc-8018-032400b67a56", without the quotes) and press Enter. \

This will post your record ID to the server and call the NAT API using GET to retrieve the record for that ID if it exists in the NAT database. \
If a record is available it will be saved in the ORM Django database and you
will then be redirected to
`http://127.0.0.1:8000/records/{recordID}/` where you will see a page with the record ID and the corresponding information about that record (following the rules mentioned in the Description section of this document). 

For example, for the record ID of "251cd289-2f0d-48fc-8018-032400b67a56" you will be redirected to 
`http://127.0.0.1:8000/records/251cd289-2f0d-48fc-8018-032400b67a56/`
where you will see the title of the record: `Titanic and Lusitania disasters.`

![Screenshot](img/API_screenshot.png?raw=true "Screenshot of example execution")


Click on the `Home` button on the top left of the screen to return to the home page where you can try the app with more record IDs if you wish. 

## Testing 
The unittest python package for tests was used and the tests available can be executed using:
```
python manage.py test

```
## Assumptions
As the user requirements were specifically asking to get records from the NAT API using the recordID I did not implement a search functionality with a text query. \
From the examples given in the user requirements I initially assumed all recordIDs would have `uuid` type but after running some more examples on the NAT API I noticed some records had alphanumerical strings as IDs. I then updated the model accordingly to accept strings for the id field.



## Authors
`Pavlos Antoniou @pavlosant`

