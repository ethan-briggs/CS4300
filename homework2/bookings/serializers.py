from rest_framework import serializers
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'duration']

    def validate_release_date(self, value):
        if value is None:
            raise serializers.ValidationError("release_date cannot be empty.")
        return value



class SeatSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    
    class Meta:
        model = Seat
        fields = ['id', 'movie', 'movie_title', 'seat_number', 'booking_status']


class BookingSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'movie', 'movie_title', 'seat', 'seat_number', 'user', 'username', 'booking_date']
        read_only_fields = ['booking_date', 'user']
    
    def create(self, validated_data):
        # Mark seat as booked when creating booking
        seat = validated_data['seat']
        if seat.booking_status == 'booked':
            raise serializers.ValidationError("This seat is already booked.")
        seat.booking_status = 'booked'
        seat.save()
        return super().create(validated_data)

