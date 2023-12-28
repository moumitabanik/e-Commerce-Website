E-Commerce Application Readme
This repository contains the source code for a simple E-Commerce application built using Django. Follow the instructions below to set up the development environment and run the application.

Prerequisites
Python 3.x
Virtualenv
MySQL Database
Git (optional)

Setup
Clone the repository (if you haven't already):

git clone https://github.com/your-username/e-commerce.git
cd e-commerce

Create a virtual environment:

virtualenv env
Activate the virtual environment:

On Windows:

.\env\Scripts\activate
On macOS and Linux:

source env/bin/activate
Install Django and MySQL client:

pip install django
pip install mysqlclient
Install Pillow:

pip install pillow
Pillow is a Python Imaging Library that adds support for opening, manipulating, and saving many different image file formats. It is required for image handling in the application.

Database Configuration
Create a MySQL database for the application.

Update the database configuration in the settings.py file:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Replace 'your_database_name', 'your_database_user', and 'your_database_password' with your actual database information.

Running the Application
Apply migrations:

python manage.py migrate
Create a superuser (admin) account:

python manage.py createsuperuser
Follow the prompts to set up the admin account.

Run the development server:

python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

Log in to the admin panel using the superuser credentials at http://127.0.0.1:8000/admin/.