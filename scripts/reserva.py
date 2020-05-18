from . import User
from . import Skyscanner
from . import Flights
from . import Cars

class Reserva:

    def __init__(self):
        self.preu = 0
        self.usuari = None
        v = Flights(10)
        c = Cars(3)
        self.vols = v.ConsultarLlista()
        self.destinacions = []
        pass

    def obtenir_usuari(self):
        return self.usuari



    '''
    def Confirmar_reserva(Skyscaner,Rentalcars,Hotels):
        Skyscaner.confirm_reserve(user: User, flights: Flights)
        Rentalcars.confirm_reserve( user: User, cars: Cars)
        Hotels.confirm_reserve()
        '''