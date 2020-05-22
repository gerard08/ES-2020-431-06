from . import User
from . import Skyscanner
from . import Flights
from . import Cars
from . import PaymentData

class Reserva:

    def __init__(self, preu = None, usuaris = None, llistaVols = None, llistaVehicles = None, pagament = None, allotjament =None):
        self.__preu = preu
        self.__usuaris = usuaris
        self.__llistaVols = llistaVols
        self.__llistaVehicles = llistaVehicles
        self.__pagament = pagament
        self.__llistaAllotjaments = allotjament
        self.__Vols = None
        self.__nusuari = 0
        self.__nVehicle = 0

    def afegirUsuari(self,  nom, DNI, mail):
        self.__usuaris.append(User(nom, DNI, mail, self.__nusuari))
        self.__nusuari += 1
        return self.__nusuari

    def esborrarUsuari(self, ID):
        for el in self.__usuaris:
            if el.getID() == ID:
                self.__usuaris.remove(el)
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
        total += self.__Vols.consultaPreu() * len(self.__usuaris)
        for el in self.__llistaVehicles:
            total += el.getPreu()

        for el in self.__llistaAllotjaments:
            total += el.getPreu()

        return total

    def obtenir_usuari(self):
        return self.__usuaris #mal feta

    def afegirAllotjament(self, direccio, preu, tipusAllotjament, nomAllotjament, codi, durada):
        ID = len(self.__llistaAllotjaments)
        self.__llistaAllotjaments.append(Allotjaments(direccio, preu, tipusAllotjament, nomAllotjament, codi, durada))
        return ID

    def eliminarAllotjament(self, ID):
        for el in self.__llistaAllotjaments:
            if el.getCodi() == ID:
                self.__llistaAllotjaments(el)
                return True
        return False



    '''
    def Confirmar_reserva(Skyscaner,Rentalcars,Hotels):
        Skyscaner.confirm_reserve(user: User, flights: Flights)
        Rentalcars.confirm_reserve( user: User, cars: Cars)
        Hotels.confirm_reserve()
        '''