class Desti:


    def __init__(self, nom, COD):
        self.__nom = nom
        self.__COD = COD
        self.__preu = 0

    def getNom(self):
        return self.__nom

    def getCOD(self):
        return self.__COD

    def getPreu(self):
        return self.__preu