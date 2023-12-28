
# BACKEND for HUDDLEARN

Draftly working, 
You can register new user, login
Work with JWT tokens

You can use GET POST PATCH, to list, add and modify this entities
1. skills
2. studygroups
3. projectgroups
4. huddleusers


There is a HUDDLE.postman_collection.json for POSTMAN working
You can use it


## Installation Notes

1. Install aLL modules pipfile, or
```
pip install django
pip install djangorestframework
pip install djangorestframework-jwt
```
2. Install PostgreSQL to localhost:5432, make a database huddledb

3. In SQL run:
```
CREATE USER huddle_django_user WITH PASSWORD 'dj_h_817_asjpp';

ALTER USER huddle_django_user CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE huddledb TO huddle_django_user;

GRANT ALL PRIVILEGES ON SCHEMA public TO huddle_django_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO huddle_django_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO huddle_django_user;
ALTER USER huddle_django_user WITH LOGIN;

```
4. Run
``` 
python manage.py makemigrations
python manage.py migrate
```

5. Make a Django admin superuser
6. Run Django console 
```python manage.py shell
```
and run
```
import huddleapi.models
from django.contrib.auth.models import User
adm_user = User.objects.get(username="admin")
huddladmin=huddleapi.models.HuddleUser.objects.create(user=adm_user, fullname='Admin Adminovitch')
```


7. Run
```
python manage.py runserver

```

8. Have fun



### TODO

1. add skills additions

3. in the add users check if user is not in group
4. remove user - check if user creator - prohibit
    if user in coordinators - remove from there

5. a lot of staff