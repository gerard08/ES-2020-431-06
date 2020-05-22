class Desti:


    def __init__(self, nom, COD, preu):
        self.__nom = nom
        self.__COD = COD
        self.__preu = preu

    def getNom(self):
        return self.__nom

    def getCOD(self):
        return self.__COD

    def getPreu(self):
        return self.__preu