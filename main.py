from app.classes.voiture import Voiture
from app.utils.utils import show
from app.utils.utils import faire_parler
from app.classes.chat import Chat
from app.classes.chien import Chien

if __name__ == "__main__":
    ma_voiture = Voiture("Toyota", "Corolla")
    ma_voiture.accelerer(50)
    
    show(ma_voiture, "ma_voiture")
    
    print(ma_voiture.afficher_details())
    
    # Chien et Chat
    mon_chien = Chien()
    mon_chat = Chat()
    faire_parler(mon_chien)
    faire_parler(mon_chat)
    
    