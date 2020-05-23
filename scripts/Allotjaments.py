class Allotjaments:

    def __init__(self, direccio, preu, tipusAllotjament, nomAllotjament, codi, durada):
        self.direccio = direccio
        self.__preu = preu
        self.tipusAllotjament = tipusAllotjament
        self.nomAllotjament = nomAllotjament
        self.__codi = codi
        self.__durada = durada

    def getDireccio(self):
         return self.__direccio

    def getPreu(self):
        return self.__preu * self.__durada

    def getTipusAllotjament(self):
        return self.__tipusAllotjament

    def getNomAllotjament(self):
        return self.nomAllotjament

    def getCodi(self):
        return self.__codi

    def getDurada(self):
        return self.durada