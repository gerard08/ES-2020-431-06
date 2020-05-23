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
    def get_nomtitular(self):
        return self.nom_titular

    def get_codiseguretat(self):
        return self.__codi_seguretat

    def mostrar_tipus_targeta(self):
        return self.tipus_targeta

    def mostra_num_targeta(self):
        return self.__num_targeta

    def set_tipus_targeta(self,tarj):
        self.tipus_targeta=tarj
    def mostra_import(self):
        return self.__import_total

