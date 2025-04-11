from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()

        if not name or len(name) > 50:
            raise ValueError("Le nom de la commodité est requis et doit faire moins de 50 caractères.")

        self.name = name