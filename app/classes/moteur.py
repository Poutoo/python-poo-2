class Moteur:
    def __init__(self, puissance: int):
        self.puissance = puissance
        
    def demarrer(self) -> str:
        return "Moteur démarré"
    
    def arreter(self) -> str:
        return "Moteur arrêté"
    
    def afficher_details(self) -> str:
        return f"Puissance du moteur: {self.puissance} CV"