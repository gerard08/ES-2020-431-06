class Cars:

    def __init__(self, codi, marca, matricula, llocrecollida, duradareserva, preuHora):
        self.__codi = codi
        self.marca = marca
        self.__matricula = matricula
        self.llocrecollida = llocrecollida
        self.duradareserva = duradareserva
        self.__preuHora = preuHora

    def getCodi(self):
        return self.__codi

    def getMarca(self):
        return self.marca

    def getMatricula(self):
        return self.__matricula

    def getLlocRecollida(self):
        return self.llocrecollida

    def getDuradaReserva(self):
        return self.duradareserva