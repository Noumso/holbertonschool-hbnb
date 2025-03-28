# app/models/place.py

from app.models.base_model import BaseModel
from app.models.user import User
from sqlalchemy.orm import validates


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities
    
    @validates('title')
    def validate_title(self, key, value):
        """Validation for title"""
        if not value:
            raise TypeError("Title must be present.")
        if len(value) > 100:
            raise ValueError(
                "Title must be present with a maximum of 100 characters.")
        return value
    
    @validates('description')
    def validate_description(self, key, value):
        """Validation for description"""
        if len(value) > 1000:
            raise ValueError(
                "Description must be less than 1000 characters.")
        return value

    @validates('price')
    def validate_price(self, key, value):
        if not isinstance(value, int):
            raise TypeError("Price must be an integer.")
        if value <= 0 or not value:
            raise ValueError("The price must be present and greater than 0.")
        return value

    @validates('latitude')
    def validate_latitude(self, key, value):
        if not isinstance(value, float):
            raise TypeError("Latitude must be a float.")
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90.0 and 90.0")
        return value

    @validates('longitude')
    def validate_longitude(self, key, value):
        if not isinstance(value, float):
            raise TypeError("Longitude must be a float.")
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180.0 and 180.0")
        return value
    
    @validates('owner_id')
    def validate_owner_id(self, key, value):
        if not isinstance(value, str):
            raise TypeError("Owner must be a User ID string.")
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        self.save()
    
    def delete_review(self, review):
        """Delete a review from the place."""
        if review in self.reviews:
            self.reviews.remove(review)
            self.save()

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
        self.save()

    def delete_amenity(self, amenity):
        """Delete a review from the place."""
        if amenity in self.amenities:
            self.reviews.remove(amenity)
            self.save()
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
