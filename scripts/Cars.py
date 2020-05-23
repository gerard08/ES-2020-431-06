class Cars:

    def __init__(self,marca, matricula, llocrecollida, duradareserva, preuHora):

        self.marca = marca
        self.__matricula = matricula
        self.llocrecollida = llocrecollida
        self.duradareserva = duradareserva
        self.__preuHora = preuHora



    def getMarca(self):
        return self.marca

    def getMatricula(self):
        return self.__matricula

    def getLlocRecollida(self):
        return self.llocrecollida

    def getDuradaReserva(self):
        return self.duradareserva

    def getPreu(self):
        return self.__preuHora * self.duradareserva