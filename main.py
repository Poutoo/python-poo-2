from app.classes.voiture import Voiture
from app.utils.utils import show

if __name__ == "__main__":
    ma_voiture = Voiture("Toyota", "Corolla")
    ma_voiture.accelerer(50)
    
    show(ma_voiture, "ma_voiture")
    
    print(ma_voiture.afficher_details())
    
    