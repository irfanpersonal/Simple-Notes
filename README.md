# Notes

A straightforward Notes Application designed to help users get familiar with Django development. It includes extensive comments throughout the code, making it a helpful reference for future Django projects.

## Technologies Used

- [Python](https://www.python.org/): A versatile, high-level programming language known for its readability, ease of use, and wide range of applications, including web development, data analysis, artificial intelligence, and more.
- [Django](https://www.djangoproject.com/): A high-level Python web framework that encourages rapid development and clean, pragmatic design. It simplifies the creation of web applications by providing reusable components like authentication, database management, and URL routing, allowing developers to focus on building features. Known for its scalability, security, and adherence to the DRY (Don't Repeat Yourself) principle, Django is widely used for building both simple and complex web applications.
- [SQLite](https://www.sqlite.org/): A lightweight, serverless, self-contained SQL database engine that is widely used for embedded database applications. Unlike traditional database management systems, SQLite is fully contained within a single file, making it easy to set up and use. It’s ideal for small to medium-sized applications, development environments, and situations where simplicity, portability, and minimal configuration are key. SQLite is commonly used in mobile apps, web browsers, and other applications that need reliable, file-based storage without the overhead of a full-fledged database server.

## Setup Instructions

1st - Download the project

2nd - Create a virtual environment using the built in "venv" module. And then
activate it.

python3 -m venv .venv

- python3 is the Python Interpreter you want to use
- -m is a flag that says I would like to run a module as a script
- venv is the built in module used to creating virtual environments
- .venv is the virtual environment name I would like to have (convention)

source .venv/bin/activate - to activate virtual environment

3rd - Install all the dependencies

pip install -r requirements.txt

4th - Navigate to the "myproject" directory.

5th - Run the following two commands

python3 manage.py makemigrations - Notify Django of the Changes you want made to the Database

python3 manage.py migrate - Apply Change to Database

6th - Run the following command to start up application

python3 manage.py runserver 4000

DONE
