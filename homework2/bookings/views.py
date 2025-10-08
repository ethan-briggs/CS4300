from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# API ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available seats"""
        movie_id = request.query_params.get('movie_id')
        if movie_id:
            seats = Seat.objects.filter(movie_id=movie_id, booking_status='available')
        else:
            seats = Seat.objects.filter(booking_status='available')
        serializer = self.get_serializer(seats, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get_queryset(self):
        """Filter bookings by user if authenticated"""
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user)
        return Booking.objects.all()
    
    def perform_create(self, serializer):
        """Automatically set the user when creating a booking"""
        serializer.save(user=self.request.user)


# Template Views
def movie_list(request):
    """Display all movies"""
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    """Display available seats for a movie and handle booking"""
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)
    
    if request.method == 'POST' and request.user.is_authenticated:
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id, movie=movie)
        
        if seat.booking_status == 'available':
            Booking.objects.create(
                movie=movie,
                seat=seat,
                user=request.user
            )
            seat.booking_status = 'booked'
            seat.save()
            messages.success(request, f'Successfully booked seat {seat.seat_number}!')
            return redirect('booking_history')
        else:
            messages.error(request, 'This seat is already booked.')
    
    context = {
        'movie': movie,
        'seats': seats
    }
    return render(request, 'bookings/seat_booking.html', context)


@login_required
def booking_history(request):
    """Display user's booking history"""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})