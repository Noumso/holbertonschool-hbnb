import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())  # Identifiant unique
        self.created_at = datetime.now()  # Date de création
        self.updated_at = datetime.now()  # Dernière mise à jour

    def save(self):
        """Met à jour la date de mise à jour"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Met à jour les attributs de l'objet à partir d'un dictionnaire"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()