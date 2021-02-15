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

# How to get your local project up and running

## Clone the project to your machine
```
git clone https://github.com/wukunze/chat_ml_assignment.git
```
* check out the **develop** branch

## Set up your local MySQL server
* In `cse_site\cse_site\settings.py`, under DATABASES, set USER and PASSWORD to your local MySQL root credentials.
* **NOTE:** DO NOT COMMIT the `settings.py` file if you only make the changes above to connect the app to your database because different developers may name their root credentials differently.
* Create a database named **ubs_system** in your local MySQL.

## Migrate (tell Django to generates tables for you)
* In `chat_ml_assigment\cse_site\`, run
```
python manage.py migrate
```
* Check that tables are added to you database
* Run the server
```
python manage.py runserver
```
* In your web browser, navigate to `http://127.0.0.1:8000/admin`
* If you can see the login page for admin, the project is working correctly.

# About Gitflow
* The **develop** branch is sacred. Please don't work on it unless you're creating a migration (which means changing the database. More on this later.).
* You normal workflow would be something like this:
    * Fetch the remote repository
    * If there are changes on the remote **develop** branch, pull those changes to your local **develop** branch
    * Create a new branch off of your local **develop** branch using this naming convention `#<story_number>_<short_title_of_breakdown_task>`
    * Work on the breakdown task. 
        * Note: you can always merge your local **develop** branch into your local task branch just so that you work on the latest state of the application. This is a good practice.
        * Commit and push your local task branch to the remote repository often. This is a good practice.
        




