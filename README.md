Movie Theater Booking Application
A Django-based web application for booking movie theater seats with a RESTful API and Bootstrap UI.
Features

🎬 Browse available movies
💺 Interactive seat selection and booking
📋 View booking history
🔌 RESTful API for all operations
📱 Responsive Bootstrap interface
🔐 User authentication

Quick Start
Prerequisites

Python 3.8+
pip
Virtual environment (recommended)

Installation
bash# Clone the repository
cd homework2

# Create and activate virtual environment
python3 -m venv hw2_env
source hw2_env/bin/activate

# Install dependencies
pip install django djangorestframework

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create admin user
python3 manage.py createsuperuser

# Populate sample data
python3 manage.py shell
Then paste this in the shell:
pythonfrom bookings.models import Movie, Seat
from datetime import date

movies = [
    {"title": "Inception", "description": "A mind-bending thriller", "release_date": date(2010, 7, 16), "duration": 148},
    {"title": "The Dark Knight", "description": "Batman vs Joker", "release_date": date(2008, 7, 18), "duration": 152},
]

for data in movies:
    m = Movie.objects.create(**data)
    for row in ['A', 'B', 'C']:
        for num in range(1, 11):
            Seat.objects.create(movie=m, seat_number=f'{row}{num}', booking_status='available')

exit()
bash# Start the server
python3 manage.py runserver 0.0.0.0:3000
Usage
Web Interface

Home: View all available movies
Book Seats: Click "Book Seats" on any movie
Login: Use admin credentials to book seats
My Bookings: View your booking history

Running Tests
bashpython3 manage.py test bookings
Admin Panel
Access the admin panel at /admin/ with your superuser credentials to:

Add/edit/delete movies
Manage seats
View all bookings

Technologies Used

Backend: Django 4.2.7
API: Django REST Framework 3.14.0
Frontend: Bootstrap 5
Database: SQLite (development)

Troubleshooting
Database Issues
bash# Reset database
rm db.sqlite3
python3 manage.py migrate
Migration Issues
bash# Fresh migrations
rm -rf bookings/migrations/0*.py
python3 manage.py makemigrations bookings
python3 manage.py migrate
Port Already in Use
bash# Use a different port
python3 manage.py runserver 0.0.0.0:8000

References:
ChatGPT was used for logic.
Claude was used for generating code and formatting README(could use some work).
