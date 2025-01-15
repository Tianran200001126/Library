# Library Management System

A simple library management system built with Django.

---

## Features

### Admin Features:
- Secure login for admin users.
- View a list of all the books in the library.
- Access details of all the readers.
- Assign books to readers.
- View the details of a book

### Reader Features:
- Secure login for reader users.
- View personal details.
- Check the list of books they have borrowed.

---

## Installation and Run Instructions

Follow these steps to set up and run the application:

### Step-by-Step Commands

1. Install the requirements files:
   ```bash
   pip install -r requirements.txt

2. Run the migration:
   ```bash
   python manage.py makemigrations and python manage.py migrate
3. Create admin:
   ```bash
   python manage.py createsuperuser
4. Run the webservice and go to login URL:
   ```bash
   python manage.py runserver     
