from . import reserva


class PaymentData:

    def __init__(self):
        self.nom_titular = " "
        self.num_targeta = 0
        self.tipus_targeta = "none"
        self.codi_seguretat = 0
        self.import_total = 0
        pass

    def calcular_preu(self, Res: reserva):
        self.import_total = Res.preu
        pass