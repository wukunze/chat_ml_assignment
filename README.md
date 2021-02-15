# chat_ml_assignment
class assignment


# command that used in this project -- Kunze Wu

# check version
python -m django --version


# create project
django-admin startproject cse_site  # run one time is ok , i have created site "cse_site"

# cd into chat_ml_assigment/cse_site and run:
python manage.py runserver


# cd into chat_ml_assigment/cse_site and run:
python manage.py startapp ubs_project  # run one time is ok , i have created application "ubs_project"


# cd into chat_ml_assigment/cse_site and run server
python manage.py runserver



# run this after added new application in chat_ml_assigment/cse_site/settings.py "INSTALLED_APS"
python manage.py migrate



# run this after we changed ubs_project.models.py
python manage.py makemigrations ubs_project
# if you want to ckeck what will be run in database. new files will create in ubs_project/migrations/xxxx_initial.py
python manage.py sqlmigrate polls xxxx
# this command will create and profile table in mysql
python manage.py migrate



# use API to test code :
python manage.py shell



# create admin account ,this is an django application called "django.contrib.admin", you can find the reason in /cse_site/cse_site/urls.py
python manage.py createsuperuser
# go to http://127.0.0.1:8000/admin/ after start server
