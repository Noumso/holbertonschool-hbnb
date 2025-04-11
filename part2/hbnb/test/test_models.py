from app.models.users import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def run_tests():
    print("🔧 Test création utilisateur...")
    user = User("Jean", "Martin", "jean.martin@email.com")
    assert user.first_name == "Jean"
    assert user.is_admin == False
    print("✅ Utilisateur OK")

    print("🔧 Test création lieu...")
    place = Place("Appartement Paris", "Très bel appart", 120, 48.8566, 2.3522, user)
    assert place.title == "Appartement Paris"
    assert place.owner == user
    print("✅ Lieu OK")

    print("🔧 Test création avis...")
    review = Review("Super endroit !", 5, place, user)
    place.add_review(review)
    assert len(place.reviews) == 1
    print("✅ Avis OK")

    print("🔧 Test commodité...")
    amenity = Amenity("Climatisation")
    place.add_amenity(amenity)
    assert place.amenities[0].name == "Climatisation"
    print("✅ Commodité OK")

    print("🎉 Tous les tests sont passés avec succès !")

if __name__ == "__main__":
    run_tests()