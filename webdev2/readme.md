# Django Tweeting App


## Overview

This Django project provides a user authentication system with functionalities for user signup, signin, and signout. It uses Django’s built-in authentication framework to manage user accounts and sessions, with error handling and user feedback included.It allows the user to post tweets, edit and delete them.

## Features

- **Signup**: Register new users with validation for existing email addresses and password confirmation.
- **Signin**: Allow users to log in using their email and password.
- **Redirects**: Redirect users to the `index.html` page after successful signup or signin.
- **Error Handling**: Display error messages for existing emails, password mismatches, and invalid credentials.

## Requirements

- Python 3.x
- Django 4.x

## Setup

### Clone the Repository

```bash
git clone https://github.com/ANOsapien/LeranersSpace_Webdev/tree/main/webdev2
```
### Activate virtual environment

```bash
python -m venv venv
On Windows use `venv\Scripts\activate`
```
### Install dependencies

```bash
pip install -r requiremnts.txt
```
### Create a superuser to access the Django admin panel

```bash

python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```
### Open your browser 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) or ['Click here'](http://127.0.0.1:8000/)



