from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if not title or len(title) > 100:
            raise ValueError("Le titre est requis et doit faire moins de 100 caractères.")
        if price <= 0:
            raise ValueError("Le prix doit être un nombre positif.")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("La latitude doit être comprise entre -90 et 90.")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("La longitude doit être comprise entre -180 et 180.")
        if owner is None:
            raise ValueError("Un propriétaire valide est requis.")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Ajoute un avis au lieu"""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Ajoute une commodité au lieu"""
        self.amenities.append(amenity)