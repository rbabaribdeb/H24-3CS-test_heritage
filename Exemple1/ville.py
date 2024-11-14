class Ville:
    def __init__(self, p_nom, p_pays, p_nombreHabitants):
        self.nom = p_nom
        self.pays = p_pays
        self.nombreHabitants = p_nombreHabitants

    def type_ville(self):
        if int(self.nombreHabitants) > 1000000:
            message = "c'est une grande ville"
        else:
            message = "c'est un petite ville"
        return message
    def __str__(self):
        return "[ " + str(self.nom) + " "+ str(self.pays) + " "+ str(self.nombreHabitants) + "]"
    def autreMethode(self):
        pass



