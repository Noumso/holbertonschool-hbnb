from app.models.users import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def test_classes():
    user = User("Alice", "Dupont", "alice@example.com")
    place = Place("Maison au calme", "Maison avec vue", 80, 45.0, 3.0, user)
    amenity = Amenity("Wi-Fi")
    review = Review("Super séjour", 5, place, user)

    place.add_review(review)
    place.add_amenity(amenity)

    print(f"Utilisateur : {user.first_name} {user.last_name}")
    print(f"Lieu : {place.title} avec {len(place.reviews)} avis")
    print(f"Avis : {review.text} - note : {review.rating}")
    print(f"Commodité : {place.amenities[0].name}")

test_classes()