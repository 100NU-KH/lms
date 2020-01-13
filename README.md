# Loan Management System - LMS

Clone lms in local directory.

- Create virtual enviornment for LMS
- Activate virtual enviorment usign source <env_name>/bin/activate.

- install all requirements using below commands
	
	pip3 install -r requirements.txt


- Create the mysql database and update the credentials in the django settings.py file for the DB connection.

- LMS Urls 
	- /application/create/  				- Application creation 
	- /applicatoin/list/    				- lists all applications with pagination
	- /application/update/<application-id>/ - manager user can update the application status to approved or rejected


Done !!