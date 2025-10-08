from django.core.management.base import BaseCommand
from bookings.models import Movie, Seat
from datetime import date

class Command(BaseCommand):
    help = "Seeds the database with sample movies and seats."

    def handle(self, *args, **options):
        # Prevent duplicates if data already exists
        if Movie.objects.exists():
            self.stdout.write(self.style.WARNING("Movies already exist — skipping seed."))
            return

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
            self.stdout.write(self.style.SUCCESS(f"Created {movie.title} with 50 seats")) 
