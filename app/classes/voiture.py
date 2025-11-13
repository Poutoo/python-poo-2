from vehicule import Vehicule

class Voiture(Vehicule):
    def __init__(self, marque: str, model: str, vitesse: float = 0.0):
        super().__init__(marque, model)
        self.vitesse = vitesse    
