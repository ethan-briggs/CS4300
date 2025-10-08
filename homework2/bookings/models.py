from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-release_date']


class Seat(models.Model):
    SEAT_STATUS = [
        ('available', 'Available'),
        ('booked', 'Booked'),
    ]
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    booking_status = models.CharField(max_length=20, choices=SEAT_STATUS, default='available')
    
    def __str__(self):
        return f"{self.movie.title} - Seat {self.seat_number}"
    
    class Meta:
        unique_together = ['movie', 'seat_number']
        ordering = ['seat_number']


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='bookings')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seat {self.seat.seat_number}"
    
    class Meta:
        ordering = ['-booking_date']
