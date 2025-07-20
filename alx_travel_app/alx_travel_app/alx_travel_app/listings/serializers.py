from rest_framework import serializers
from .models import User, Listing, Booking, Review

class UserSerializer(serializers.ModelSerializer):
	email = serializers.CharField(
        max_length=100,
        help_text="The email has a (max 100 characters)."
    )
	class Meta:
		model = User
		fields = ['user_id', 'username', 'email']
		

class ListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Listing
		fields = __all__


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = __all__
		

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = __all__