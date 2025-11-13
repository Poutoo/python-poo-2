from app.classes.vehicule import Vehicule
from app.classes.moteur import Moteur

class Voiture(Vehicule, Moteur):
    def __init__(self, marque: str, model: str, vitesse: float = 0.0):
        super().__init__(marque, model)
        self.vitesse = vitesse

    def accelerer(self, increment: float) -> None:
        self.vitesse += increment
    
    def freiner(self, decrement: float) -> None:
        self.vitesse = max(0.0, self.vitesse - decrement)
    
    def afficher_details(self) -> str:
        details = super().afficher_details()
        return f"{details}, Vitesse: {self.vitesse} km/h"
    
    def klaxonner(self) -> str:
        return "Beep Beep!"
    