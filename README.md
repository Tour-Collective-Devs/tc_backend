# TC jobsite backend
This repo holds the backend code for the tour collective jobsite.

## virtual environment
This repo has a few python package dependencies that must be installed to develop on the project.

1. as a sibling to this directory, create a python virtual environment
1. install dependencies from the requirements.txt file with 'pip install -r requirements.txt'

## API
The following resources are available through the api...

### Employer
Employer model stores 
1. username
1. email
1. password hash

see auth section for more information on how to handle employers

### Genre
available fields
id: pk
url: url to detail view
name: name of the genre

### Role
available fields
id: pk
url: url to detail view
name: name of the role
description: description of the role

### Event
available fields
id: pk
url: url to detail view
employer: link to employer 
genres: array of genres
role: link to role
start_date: start date
end_date: end date
description: description of the job
total_pay: integer
show_count: integer
required_experience: char field
pay_type: select field


## Auth
Our employer and (crew not finished) models uses django-rest-authentication endpoints

employers can be created at endpoint api/employer/registration
employers can login at api/employer-auth/login
employers can be logged out by posting to api/employer-auth/logout

## working with auth token
We can make sure that certain views are blocked unless the request includes a current auth token by following the steps listed in the django documentation here: http://www.django-rest-framework.org/api-guide/permissions/

## sending token in header
The following is an example javascript code snippet of how you would send the token in a request header to validate the request with a logged in user. This code assumes the value of the users current auth token is being stored in session storage on the browser.

```
fetch('URL_GOES_HERE', { 
   method: 'post', 
   headers: new Headers({
     'Authorization': `Token ${sessionStorage.getItem('DRF_Token')}`, 
     'Content-Type': 'application/json'
   }), 
   body: someObjectVariableProbablyPassedToFunction
 });
 ```


## file structure / naming conventions

directories all lowercase snake case
files all lower case snake case
class names match file names except with uppercase words
example...

file name `crew_user_account.py` for crew account model file
class name `Crew_User_Account` for the class name in the file

make sure to add classes within directories to the directories init file

## Deploying this project
Follow these steps to deploy a new version of this api to our digital ocean server.

1. SSH into the server `ssh tc....`
1. From the home directory of that user you can paste in the following commands in whole to update the server
```
source env/bin/activate
cd tc_backend
git pull origin master
python manage.py collectstatic
python manage.py makemigrations
python manage.py makemigrations allauth
python manage.py makemigrations users
python manage.py makemigrations api
python manage.py migrate
sudo systemctl restart gunicorn
sudo systemctl restart nginx
exit
```

Depending on the complexity of the update certain lines may or may not be needed. If the new update does not contain any changes to models you can safely remove all the lines dealing with database migration.
