from . import User
from . import Skyscanner
from . import Flights
from . import Cars
from . import PaymentData

class Reserva:

    def __init__(self, preu, usuaris, llistaVols, llistaVehicles, pagament, llistaAllotjaments):
        self.__preu = preu
        self.__usuaris = usuaris
        self.__llistaVols = llistaVols
        self.__llistaVehicles = llistaVehicles
        self.__pagament = pagament
        self.__llistaAllotjaments = llistaAllotjaments

    def afegirUsuari(self,  nom, DNI, mail):
        ID = len(self.__usuaris)
        self.__usuaris.append(User(nom, DNI, mail, ID))
        return ID

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

    def obtenir_usuari(self):
        return self.usuari

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