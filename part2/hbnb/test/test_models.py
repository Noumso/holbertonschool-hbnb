from app.models.users import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def test_user():
    user = User(first_name="Jean", last_name="Dupont", email="jean@example.com")
    assert user.first_name == "Jean"
    assert user.last_name == "Dupont"
    assert user.email == "jean@example.com"
    assert user.is_admin is False
    print("✅ Test User OK")

def test_place():
    owner = User(first_name="Alice", last_name="Smith", email="alice@example.com")
    place = Place(title="Maison au calme", description="Vue sur mer", price=120, latitude=48.85, longitude=2.35, owner=owner)
    assert place.owner == owner
    assert place.title == "Maison au calme"
    print("✅ Test Place OK")

def test_review():
    user = User(first_name="Bob", last_name="Builder", email="bob@example.com")
    place = Place(title="Studio", description="Petit mais fonctionnel", price=75, latitude=45.76, longitude=4.84, owner=user)
    review = Review(text="Super séjour", rating=5, place=place, user=user)
    assert review.place == place
    assert review.user == user
    assert review.rating == 5
    print("✅ Test Review OK")

def test_amenity():
    amenity = Amenity(name="Wi-Fi")
    assert amenity.name == "Wi-Fi"
    print("✅ Test Amenity OK")

# Exécuter tous les tests
if __name__ == "__main__":
    test_user()
    test_place()
    test_review()
    test_amenity()