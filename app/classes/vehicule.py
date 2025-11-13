class Vehicule:
    def __init__(self, marque: str, model: str):
        self.marque = marque
        self.model = model
    
    def afficher_details(self):
        return f"Marque: {self.marque}, Modèle: {self.model}"