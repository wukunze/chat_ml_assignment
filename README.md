# chat_ml_assignment
class assignment


## command may used in this project

* check version
```
python -m django --version
```
* create project
```
django-admin startproject cse_site  # run one time is ok , i have created site "cse_site"
```

* cd into chat_ml_assigment/cse_site and run:
```
python manage.py runserver
```

* cd into chat_ml_assigment/cse_site and run:
```
python manage.py startapp ubs_project  # run one time is ok , i have created application "ubs_project"
```

* cd into chat_ml_assigment/cse_site and run server
```
python manage.py runserver
```

* run this after added new application in chat_ml_assigment/cse_site/settings.py "INSTALLED_APS"
```
python manage.py migrate
```


* run this after we changed ubs_project.models.py
```
python manage.py makemigrations ubs_project
```
* check what will be run in database. new files will create in ubs_project/migrations/xxxx_initial.py
```
python manage.py sqlmigrate polls xxxx
```
* create or modify table in mysql
```
python manage.py migrate
```

* use django shell to test code
```
python manage.py shell
```

* create admin account

`this is an django application called "django.contrib.admin", you can find the reason in /cse_site/cse_site/urls.py`
```
python manage.py createsuperuser
```
`go to http://127.0.0.1:8000/admin/ after start server`




# How to get your local project up and running

## Clone the project to your machine
```
git clone https://github.com/wukunze/chat_ml_assignment.git
```
* check out the **develop** branch

## Run the server
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
    * Create a new branch off of your local **develop** branch using this naming convention `feature/#<story_number>_<short_title_of_breakdown_task>`
    * Work on the breakdown task. 
        * Note: you can always merge your local **develop** branch into your local task branch just so that you work on the latest state of the application. This is a good practice.
        * Commit and push your local task branch to the remote repository often. This is a good practice.
        * Once you finish your task, create a Pull Request to merge your remote task branch to the remote develop branch. A simple Code Review process here is that you add other developers to the Pull Request as your reviewers. If 3 people approve your code, Hoang or Kunze will merge you code in.

# About Migration (Changing the database)
* While working on your story/task, you may find that you need to modify the database. Just reach out to Hoang or Kunze and we can have a quick call to review your changes. 
* A migration should be done on develop. This prevents the app/database from being broken while other developers are working on their tasks. Since we are using our local database, this won't happen as often but ensuring that everybody is working on a latest models/tables is a good thing to have. This is also the reason why Hoang and Kunze need to review you migration before you commit and push it. 
* Once you've done pushing your migration to the remote develop branch, announce it on the General chat so other developers can pull your changes.




