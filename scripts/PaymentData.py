from . import reserva


class PaymentData:

    def __init__(self):
        self.nom_titular = None
        self.__num_targeta = 0
        self.tipus_targeta = None
        self.__codi_seguretat = 0
        self.__import_total = 0
        pass

    def calcular_preu(self, Res: reserva):
        self.__import_total = Res.preu
        pass

    def mostra_num_targeta(self):
        return self.__num_targeta

    def mostra_import(self):
        return self.__import_total

