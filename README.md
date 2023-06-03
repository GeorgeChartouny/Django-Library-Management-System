# Django-Library-Management-System
A Django app for managing library

## Install Python if not installed on your machine
 You can check if python is installed by running the following command:
 
 ```bash
 python --version
 ```

 If not visit the website and download the Python installer that matches your OS www.python.org

## Make sure pip is installed with Python
Usually pip is installed automatically with python 2.8 or later

To check if you have pip run the following command
```bash
pip --version
```

## Install Django framework

Check if Django is installed on your machine:
```bash
django --version
```

If the version was not shown and an error was printed, run the following:
```bash
pip install django
```

## Migrate 
 it is recommended to run the migration commands to set up the database schema and apply any pending database changes.
 ```bash
 python manage.py migrate
 ```

 ## Run the server
 First go into the appropriate directory:
 ```bash
cd lmsProject/
 ```
 start the application(by default port 8000 will be reserved for the app):
 ```bash
 python manage.py runserver
 ```