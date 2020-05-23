from scripts.Desti import Desti


class Flights:

    def __init__(self, source, destination, codivol, nPassatgers, datesource, dateDestination):
        self.source = source
        self.destination = destination
        self.codiVol = codivol
        self.__nPassatgers = nPassatgers
        self.datesource = datesource
        self.dateDestination = dateDestination

    def ConsultarLlista(self):
        return self.__flights

    def getNumeroDestins(self):
        return len(self.__flights)

    def consultaPreu(self):
        return self.destination.getPreu()

    def getNPassatgers(self):
        return self.__nPassatgers

    def __eq__(self, codVol):
        if self.codiVol == codVol:
            return True