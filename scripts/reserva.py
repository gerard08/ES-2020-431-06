from . import User
from . import Skyscanner
from . import Flights
from . import Cars
from . import PaymentData

class Reserva:

    def __init__(self, preu, usuaris, llistaVols, llistaVehicles, pagament, allotjament):
        self.__preu = preu
        self.__usuaris = usuaris
        self.__llistaVols = llistaVols
        self.__llistaVehicles = llistaVehicles
        self.__pagament = pagament
        self.__allotjament = allotjament

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

    def afegirVehicle(self, marca, matricula, llocRecollida, durada):
        ID = len(self.__llistaVehicles)
        self.__usuaris.append(Cars(ID,marca, matricula, llocRecollida, durada))
        return ID

    def eliminarVehicle(self, ID):
        for el in self.__llistaVehicles:
            if el.getCodi() == ID:
                self.__llistaVehicles.remove(el)
                return True
        return False



    def obtenir_usuari(self):
        return self.usuari



    '''
    def Confirmar_reserva(Skyscaner,Rentalcars,Hotels):
        Skyscaner.confirm_reserve(user: User, flights: Flights)
        Rentalcars.confirm_reserve( user: User, cars: Cars)
        Hotels.confirm_reserve()
        '''