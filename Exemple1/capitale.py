from Exemple1.ville import Ville

class Capitale(Ville): # Héritage ...
    # constructeur
    def __init__(self, p_nom, p_pays, p_nombreHabitants, p_monument):
        super().__init__(p_nom, p_pays, p_nombreHabitants)
        self.monument = p_monument

    # @Override tostring en faisant appel à str du parent ...
    def __str__(self):
        return super().__str__() + "[" + self.monument + "]"



class CapitaleV2(Ville): # Héritage ...
    # constructeur
    def __init__(self, ville, p_monument):
        super().__init__(ville.nom, ville.pays, ville.nombreHabitants)
        self.monument = p_monument
    # @Override tostring en faisant appel à str du parent ...
    def __str__(self):
        return super().__str__() + "[" + self.monument + "]"
class CapitaleV3(): # Pas Héritage ...
    # constructeur
    def __init__(self, p_ville, p_monument):
        self.ville = p_ville
        self.monument = p_monument
    # @Override tostring en faisant appel à str du parent ...
    def __str__(self):
        return ("[ " + str(self.ville.nom) + " "+ str(self.ville.pays) + " "
                + str(self.ville.nombreHabitants) + "]"+ "[" + self.monument + "]")
c2 = CapitaleV2(Ville("Ottawa", "Ca", 1000000), "parlement")
c3 = CapitaleV3(Ville("Ottawa", "Ca", 1000000), "parlement")