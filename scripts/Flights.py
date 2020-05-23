from scripts.Desti import Desti
class Flights:


    def __init__(self, source, destination, codivol, nPassatgers, datesource, dateDestination, flights, maxFlights):
        self.source = source
        self.destination = destination
        self.codiVol = codivol
        self.__nPassatgers = nPassatgers
        self.datesource = datesource
        self.dateDestination = dateDestination
        self.__flights = flights
        self.__maxFlights = maxFlights
        self.__nVols = 0


    def AfegirDestí(self, nom, preu):
        if len(self.__flights) < self.maxFlights:
            COD = len(self.__flights)
            desti = Desti(nom, COD, preu)
            self.__flights.append(desti)
            self.__nVols += 1
        else:
            print("numero màxim de destins assolits")
        return self.__nVols

    def EliminarDestí(self, COD):
        for dest in self.__flights:
            if dest.getCOD() == COD:
                self.__flights.remove(dest)

    def ConsultarLlista(self):
        return self.__flights

    def getNumeroDestins(self):
        return len(self.__flights)

    def consultaPreu(self):
        return self.destination.getPreu()

    def getNPassatgers(self):
        return self.__nPassatgers
    def __eq__(self, codVol):
        if self.codiVol==codVol:
            return True