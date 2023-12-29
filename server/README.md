

![img_4.png](img_4.png)

# BACKEND for HUDDLEARN

Work with JWT tokens

You can use GET POST PUT PATCH DELETE, use additional actions, use pictures, filter for this entities:
1. skills
2. studygroups
3. projectgroups
4. huddleusers

## Authorisation

Successful action of registration or login responses with JSON with tokens like
```
{
    "refresh": "eyJhbGciOiJIU.....",
    "access": "eyJhbGciOiJIU...."
{
```
```access``` is the access token, you should use ```"JWT "+response.access``` in the Authorisation header field of all your request


### Registration
```
auth/register/
```
JSON:
```
{
    "username": "Your name",
    "password": "your pass",
    "email": "myemail@some.com"
}
```

It will create ad DB field with this user, 
and also create a HuddleUser instance connected to this User

all enties will use this HuddleUser instance ID to members, creator, coordinators list fields, so be careful

### Login
```
/auth/login/
```
JSON:
```
{
    "username": "Your name",
    "password": "your pass",
}
```


## Complete CRUD endpoints, JSON:
### by default in dev, the base url is: ```localhost:8000/```

```
/skills/
/studygroups/
/projectgroups/
/huddleusers/
```
JSON example for POST ```studygroups/```:
```
{
    "name":"New group",
    "description":"Emerald guitar sound fantasy"
}
```


### Use GET, POST, PUT, PATCH, DELETE to
```
/skills/<skill_id>/
/studygroups/<studygroup_id>/
/projectgroups/<projectgroup_id>/
/huddleusers/<huddleuser_id>/
```
JSON example for PATCH ```studygroups/10/```:
```
{
    "description":"New description"
}
```


(See huddleapi/models.py for fields names)

You are getting JSON in response

## Adding and removing members of the group:
JSON: ```{ "user_id": <HuddleUserID> }```
```
/studygroups/<studygroup_id>/add_member/
/studygroups/<studygroup_id>/remove_member/
/projectgroups/<projectgroup_id>/add_member/
/projectgroups/<projectgroup_id>/remove_member/
```
*Logic*: With all check (if such user by user_id exists, if he is not already in the group), 
if requesting user (by token) is creator or coordinator of the group user will be added to member, if not - to 
```request_users``` field. 
For removing - you cannot remove coordinator, user can remove himself, you must be creator or coordinator to remove other users,
if users is in the ```request_users``` field this action removes him

## Skills
for those endpoints:
```
/studygroups/<studygroup_id>/
/projectgroups/<projectgroup_id>/
/huddleusers/<huddleuser_id>/
```
use actions 
```
/add_skill/
/remove_skill/
```
JSON: ```{ "skill_id": <SkillID> }```

Only user may modify his skills list, only creator or coordinator may modify group skills
Examples:
```
/studygroups/6/add_skill/
/projectgroups/9/remove_skill/
/huddleusers/4/add_skill/
/projectgroups/9/remove_skill/
```

*Logic* will check if skill exist, you cannot add skill already added, and cannot remove missing skill

## Filtering

```studygroups``` and ```projectgroups``` and be filtered by skill. If you provide multiple skills, AND logic is used
Filtering is done by Skill ID field. So you should have groups with filled up skills and can filter by skills
examples:
```
/studygroups/?skills=1
/studygroups/?skills=2&skills=3
/projectgroups/?skills=3

```

## Pictures

Back-end support picture uploads, store them and allow to request it by static urls, given in 'picture' fields of all entities.

Uploaded picture automatically rescaled to (300,300). 

With GET you automatically get response with ```picture``` field with url you can directly get from server

To upload picture you can use POST, PUT and PATCH
To do so use  ```Content-Type: multipart/form-data```

Fill in the text fields like JSON request (i.e. ```name```, ```description```) 

Use the field ```picture``` with the file data of the image

simple example:
```
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');

const apiUrl = 'http://127.0.0.1:8000/studygroups/';

// Create form data
const form = new FormData();
form.append('name', 'YourGroupName');
form.append('description', 'YourGroupDescription');

// Attach a file (replace 'path/to/your/image.jpg' with the actual path)
form.append('picture', fs.createReadStream('path/to/your/groupimage.jpg'));

// Make the POST request
axios.post(apiUrl, form, {
    headers: {
        ...form.getHeaders(),
        // Include additional headers if needed
        // 'Authorization': 'Bearer YourAccessToken',
    },
})
    .then(response => {
        console.log('Success:', response.data);
    })
    .catch(error => {
        console.error('Error:', error.response.data);
    });
```



# POSTMAN
There is a also ```HUDDLE.postman_collection.json``` collection in this repo for POSTMAN working

You must first create users, use Authorization with JWT token, create entries
You can use it and see how endpoints are reached





# Installation Notes

Back-end works on Python 10 + Django + Django REST freamwork + Postgre SQL 15


## Download and run [PostgreSQL 15](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) installer version 15.5 
Use default setting, adress: localhost and port 5432. Remember your superuser name (postgres) and password.
After install run ```pgAdmin4``` from the package, login with password. Expand from drop-down Servers>PostgreSQL>Databases
With right click open menu and select Create Database

![img.png](img.png)

Make the database named ```huddledb``` 
Then click on the new database name, and click Query.

![img_1.png](img_1.png)

in SQL query window insert this text and run:
```
CREATE USER huddle_django_user WITH PASSWORD 'dj_h_817_asjpp';

ALTER USER huddle_django_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE huddledb TO huddle_django_user;

GRANT ALL PRIVILEGES ON SCHEMA public TO huddle_django_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO huddle_django_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO huddle_django_user;
ALTER USER huddle_django_user WITH LOGIN;

```

![img_2.png](img_2.png)



## Install aLL modules 

You should have Python installed. naviate to the ```server``` folder with pipfile and pipfile.lock files
run
```
pip install pipenv
pipenv install
```
And run this to enter virtual environment, and navigate to server directory:
```
pipenv shell
```


(ALTERNATIVE) If you don't want to use pipenv, just make the venv and install all with pip
```
python -m venv venv

pip install django
pip install djangorestframework
pip install djangorestframework-jwt
pip install django-filter
pip install Pillow

```

And run this to enter virtual environment:
```
venv\Scripts\activate

```


## Initialize the database with migrations and make a Django superuser

In the shell of virtual environment run:
```
cd huddlearn
python manage.py createsuperuser --username=admin
```
Enter required email and password

Run this to prepare the project
``` 
python manage.py makemigrations
python manage.py migrate
```
Run Django console 
```
python manage.py shell
```
In python django console run this (it will create a connected HuddleUser instance for our admin)

```
import huddleapi.models
from django.contrib.auth.models import User
adm_user = User.objects.get(username="admin")
huddladmin=huddleapi.models.HuddleUser.objects.create(user=adm_user, fullname='Admin Adminovitch')
exit()
```

Run server
```
python manage.py runserver

```

Have fun



# TODO

// in the future back-end may requre more functionality
