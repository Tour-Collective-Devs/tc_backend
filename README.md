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


## file structure / naming conventions

directories all lowercase snake case
files all lower case snake case
class names match file names except with uppercase words
example...

file name `crew_user_account.py` for crew account model file
class name `Crew_User_Account` for the class name in the file

make sure to add classes within directories to the directories init file


for further reading...
https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
