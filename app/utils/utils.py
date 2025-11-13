from pprint import pprint
from app.classes.animal import Animal

def show(variable: any, name: str = '')-> None:
    """ 
    Petite fonction qui pemet de regarder à l'intérieur des objets ou des variables dans la console.
    Args:
        variable (any): La variable ou l'objet à afficher.
        name (str, optional): Le nom de la variable ou de l'objet.
        Défaut à une chaîne vide.
    """
    
    if hasattr(variable, '__dict__'):
        if name:
            print(f"Objet observé : {name} (Type : {type(variable)})")
            class_name = type(variable).__name__
            print(f"Classe : {class_name}")
            
            # propriètés de l'objet
            class_attributes = {
                key: value for key, value in type(variable).__dict__.items()
                if not callable(value) and not key.startswith('__')
            }
            
            for eleme in class_attributes:
                if isinstance(class_attributes[eleme], classmethod):
                    class_attributes[eleme] = "<Methode de classe>"
                if isinstance(class_attributes[eleme], property):
                    class_attributes[eleme] = "<Propriété de classe>"
                if isinstance(class_attributes[eleme], staticmethod):
                    class_attributes[eleme] = "<Méthode statique de classe>"
                if(len(class_attributes) > 0):
                    print("\nPropriétés de la classe :")
                    pprint(class_attributes)
            
            # propriètés de l'instance
            print("\nPropriétés de l'instance :")
            properties = vars(variable)
            pprint(properties)
            
            # méthodes de l'objet
            print("\nMéthodes de l'objet :")
            methods = [method for method in dir(variable)
                if callable(getattr(variable, method)) and not method.startswith("__")]
            pprint(methods)
        else: # ce n'est pas un objet
            print(f"Variable observée : {name} (Type : {type(variable)})")
            print("\nValeur :", end="")
            pprint(variable)
            
def faire_parler(animal: Animal) -> None:
    """ 
    Fonction qui fait parler un animal.
    Args:
        animal (Animal): L'animal qui va parler.
    """
    show(animal, "animal")
    print(animal.parler())