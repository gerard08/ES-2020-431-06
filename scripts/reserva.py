from scripts.Desti import  Desti
from scripts.User import User
from scripts.Skyscanner import Skyscanner
from scripts.Flights import Flights
from scripts.Cars import Cars
from scripts.PaymentData import PaymentData
from scripts.Allotjaments import Allotjaments
from scripts.Bank import Bank
from scripts.Rentalcars import Rentalcars
from scripts.Booking import Booking
from scripts.Skyscanner import Skyscanner
class reserva:

    def __init__(self, preu=0, usuaris=[], nUsuaris=0, llistaVols=[], llistaVehicles=[], pagament=PaymentData("","","","",""), allotjament=[], Destins=[]):
        self.__preu = preu
        self.__usuaris = usuaris
        self.__nUsuaris = nUsuaris
        self.__llistaVols = llistaVols
        self.__llistaVehicles = llistaVehicles
        self.__pagament = pagament
        self.__llistaAllotjaments = allotjament
        self.__Destins = Destins
        self.__maxFlights = 4
        self.__maxReintents = 5
    def get_data_pagament(self):
        return self.__pagament

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

        self.__llistaVehicles.append(Cars(marca, matricula, llocRecollida, duradareserva, preuHora))
        self.getPreuTotal()


    def eliminarVehicle(self, matricula):
        for el in self.__llistaVehicles:
            if el.getMatricula() == matricula:
                self.__llistaVehicles.remove(el)
                self.getPreuTotal()
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
        if metode_pagament == 'Visa':
            self.__pagament.set_tipus_targeta(metode_pagament)
        else:
            if metode_pagament == 'Mastercard':
                self.__pagament.set_tipus_targeta(metode_pagament)
            else :
                print('Error, metode de pagament no disponible')
    def rellenar_dades_Facturació(self,nomtitular,  numtargeta, tipustargeta, codiseguretat):

        if not isinstance(nomtitular,str):
            return "Dades invalides"
        if not isinstance(numtargeta, int):
            return "Dades invalides"
        if not isinstance(tipustargeta, str):
            return "Dades invalides"
        if not isinstance(codiseguretat, int):
            return "Dades invalides"
        if  len(str(numtargeta)) != 16:
            return "Dades invalides"
        if  len(str(codiseguretat))!=3:
            return "Dades invalides"
        if tipustargeta != 'Visa' and tipustargeta !="Mastercard":
            return "Dades invalides"
        self.__pagament=PaymentData(nomtitular,  numtargeta, tipustargeta, codiseguretat, self.__preu)
        return "Dades correctes"

    def obtenir_usuari(self):
        return self.__usuaris #mal feta

    def afegirAllotjament(self, direccio, preu, tipusAllotjament, nomAllotjament, codi, durada):
        ID = len(self.__llistaAllotjaments)
        self.__llistaAllotjaments.append(Allotjaments(direccio, preu, tipusAllotjament, nomAllotjament, codi, durada))
        self.getPreuTotal()
        return ID

    def eliminarAllotjament(self, ID):
        for el in self.__llistaAllotjaments:
            if el.getCodi() == ID:
                self.__llistaAllotjaments.remove(el)
                self.getPreuTotal()
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

    def RealitzarPagament(self,User, payment_data):
        a = Bank.do_payment("",User,payment_data)
        i=1
        while a!=True and i<self.__maxReintents:
             a = Bank.do_payment("", User, payment_data)
             i = i + 1

        if a == True:
            return ("Pagament realitzat correctament"),i
        else:
            return ("Error en el pagament"),i

    def ConfirmarReservaVols(self,User,Fligths):
        a = Skyscanner.confirm_reserve("",User,Fligths)
        i = 1
        while a != True and i < self.__maxReintents:
            a = Skyscanner.confirm_reserve("", User, Fligths)
            i=i+1
        if a == True:
            return ("Reserva realitzada correctament"),i
        else:
            return ("Error en la reserva"),i

    def ConfirmarReservaCoches(self, User, Cars):
        a = Rentalcars.confirm_reserve("", User,  Cars)
        i = 1
        while a != True and i< self.__maxReintents:
            a = Rentalcars.confirm_reserve("", User,  Cars)
            i = i + 1
        if a == True:
            return ("Reserva realitzada correctament"),i
        else:
            return ("Error en la reserva"),i

    def ConfirmarReservaAllotjaments(self, User, Allojament):
        a = Booking.confirm_reserve("", User, Allojament)
        i = 1
        while a != True and i < self.__maxReintents:
            a = Booking.confirm_reserve("", User, Allojament)
            i = i + 1
        if a == True:
            return ("Reserva realitzada correctament"),i
        else:
            return ("Error en la reserva"),i
