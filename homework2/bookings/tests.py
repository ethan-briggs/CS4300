from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="A test movie description",
            release_date=date.today(),
            duration=120
        )
    
    def test_movie_creation(self):
        """Test that a movie can be created"""
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)
    
    def test_movie_str(self):
        """Test the string representation of movie"""
        self.assertEqual(str(self.movie), "Test Movie")


class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test",
            release_date=date.today(),
            duration=120
        )
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_number="A1",
            booking_status="available"
        )
    
    def test_seat_creation(self):
        """Test that a seat can be created"""
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertEqual(self.seat.booking_status, "available")
    
    def test_seat_uniqueness(self):
        """Test that seat numbers are unique per movie"""
        with self.assertRaises(Exception):
            Seat.objects.create(
                movie=self.movie,
                seat_number="A1",
                booking_status="available"
            )


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test",
            release_date=date.today(),
            duration=120
        )
        self.seat = Seat.objects.create(
            movie=self.movie,
            seat_number="A1",
            booking_status="available"
        )
    
    def test_booking_creation(self):
        """Test that a booking can be created"""
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat,
            user=self.user
        )
        self.assertEqual(booking.user.username, 'testuser')
        self.assertEqual(booking.seat.seat_number, 'A1')


class APIEndpointTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Test Movie",
            description="Testing API",
            release_date=date.today(),
            duration=90
        )
    
    def test_movie_list_endpoint(self):
        """Test that the movie list API endpoint works"""
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
    
    def test_seat_list_endpoint(self):
        """Test that the seat list API endpoint works"""
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, 200)
