from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        # Run seeding code only when the app starts
        from bookings.models import Movie, Seat
        from datetime import date

        try:
            # Only seed if no movies exist
            if not Movie.objects.exists():
                movies_data = [
                    {"title": "Inception", "description": "A mind-bending thriller", "release_date": date(2010, 7, 16), "duration": 148},
                    {"title": "The Dark Knight", "description": "Batman vs Joker", "release_date": date(2008, 7, 18), "duration": 152},
                    {"title": "Interstellar", "description": "Space exploration", "release_date": date(2014, 11, 7), "duration": 169},
                ]

                for data in movies_data:
                    movie = Movie.objects.create(**data)
                    for row in ['A', 'B', 'C', 'D', 'E']:
                        for num in range(1, 11):
                            Seat.objects.create(movie=movie, seat_number=f"{row}{num}", booking_status="available")
                print("Seeded movies and seats successfully.")
        except (OperationalError, ProgrammingError):
            # Database not ready yet (e.g., first migration)
            pass