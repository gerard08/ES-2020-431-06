from . import reserva


class PaymentData:

    def __init__(self, nomtitular,  numtargeta, tipustargeta, codiseguretat, importtotal):
        self.nom_titular = nomtitular
        self.__num_targeta = numtargeta
        self.tipus_targeta = tipustargeta
        self.__codi_seguretat =codiseguretat
        self.__import_total = importtotal
        pass

    def calcular_preu(self, Res: reserva):
        self.__import_total = Res.preu
        pass

    def mostra_num_targeta(self):
        return self.__num_targeta

    def mostra_import(self):
        return self.__import_total

