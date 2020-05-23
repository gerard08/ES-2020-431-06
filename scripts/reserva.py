from scripts.Desti import  Desti
from scripts.User import User
from scripts.Skyscanner import Skyscanner
from scripts.Flights import Flights
from scripts.Cars import Cars
from scripts.PaymentData import PaymentData
from scripts.Allotjaments import Allotjaments

class reserva:

    def __init__(self, preu=0, usuaris=[], nUsuaris=0, llistaVols=[], llistaVehicles=[], pagament=None, allotjament=[], Destins=[]):
        self.__preu = preu
        self.__usuaris = usuaris
        self.__nUsuaris = nUsuaris
        self.__llistaVols = llistaVols
        self.__llistaVehicles = llistaVehicles
        self.__pagament = pagament
        self.__llistaAllotjaments = allotjament
        self.__Destins = Destins
        self.__maxFlights = 4


    def get_preu(self):
        return self.__preu

    def get_nUsuaris(self):
        return self.__nUsuaris

    def get_llistatVols(self):
        return self.__llistaVols

    def get_Destins(self):
        return self.__Destins

    def afegirUsuari(self,  nom, DNI, mail,ID,carnetcotxe):
        self.__usuaris.append(User(nom, DNI, mail, ID, carnetcotxe))
        self.__nUsuaris += 1
        self.getPreuTotal()

    def esborrarUsuari(self, ID):
        for el in self.__usuaris:
            if el.getID() == ID:
                self.__usuaris.remove(el)
                self.__nUsuaris -= 1
                return True
        return False

    def afegirVehicle(self, marca, matricula, llocRecollida, duradareserva, preuHora):
        ID = len(self.__llistaVehicles)
        self.__llistaVehicles.append(Cars(ID,marca, matricula, llocRecollida, duradareserva, preuHora))
        return ID

    def eliminarVehicle(self, ID):
        for el in self.__llistaVehicles:
            if el.getCodi() == ID:
                self.__llistaVehicles.remove(el)
                return True
        return False

    def getPreuTotal(self):
        total = 0
        for el in self.__llistaVols:
            total += el.consultaPreu() * len(self.__usuaris)
        for el in self.__llistaVehicles:
            total += el.getPreu()
        for el in self.__llistaAllotjaments:
            total += el.getPreu()
        self.__preu = total
        return total

    def seleccionar_metode_pagament(self,metode_pagament):
        if metode_pagament != 'Visa':
            self.metode_pagament = metode_pagament
        else:
            if metode_pagament == 'Mastercard':
                self.metode_pagament = metode_pagament
            else :
                print('Error, metode de pagament no disponible')


    def obtenir_usuari(self):
        return self.__usuaris #mal feta

    def afegirAllotjament(self, direccio, preu, tipusAllotjament, nomAllotjament, codi, durada):
        ID = len(self.__llistaAllotjaments)
        self.__llistaAllotjaments.append(Allotjaments(direccio, preu, tipusAllotjament, nomAllotjament, codi, durada))
        return ID

    def eliminarAllotjament(self, ID):
        for el in self.__llistaAllotjaments:
            if el.getCodi() == ID:
                self.__llistaAllotjaments.remove(el)
                return True
        return False

    def afegirDesti(self, nom, COD, preu):
        if len(self.__llistaVols)<self.__maxFlights:
            D=Desti( nom, COD, preu)
            self.__Destins.append(D)
            self.__llistaVols.append(Flights("",D,COD,"","","","",""))
            self.getPreuTotal()

    def eliminarDesti(self,COD):
        for i,el in enumerate(self.__Destins):
            a=el.getCOD
            if el.getCOD()==COD:
                self.__Destins.remove(el)
                self.__llistaVols.pop(i)
                self.getPreuTotal()
    def realitzarPagament(self):


