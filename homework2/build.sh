#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
"""

print("=" * 70)
print("SETUP COMPLETE - Follow these steps:")
print("=" * 70)
print("\n1. Run migrations:")
print("   python3 manage.py makemigrations")
print("   python3 manage.py migrate")
print("\n2. Create superuser:")
print("   python3 manage.py createsuperuser")
print("\n3. Create sample data (in Django shell):")
print("   python3 manage.py shell")
print("   >>> from bookings.models import Movie, Seat")
print("   >>> from datetime import date")
print("   >>> m = Movie.objects.create(title='Inception', description='A mind-bending thriller', release_date=date(2010,7,16), duration=148)")
print("   >>> for i in range(1, 21): Seat.objects.create(movie=m, seat_number=f'A{i}', booking_status='available')")
print("\n4. Run tests:")
print("   python3 manage.py test bookings")
print("\n5. Run server:")
print("   python3 manage.py runserver 0.0.0.0:3000")
print("\n6. Access at: https://app-containerName-SectionID.devedu.io/")
print("=" * 70)