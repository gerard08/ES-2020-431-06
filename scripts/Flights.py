class Flights:


    def __init__(self, maxFlights):
        self.source = ''
        self.destination = ''
        self.codiVol = ''
        self.__nPassatgers = 0
        self.datesource = ''
        self.dateDestination = ''
        self.__flights = []
        self.maximPassatgers = 20
        self.__maxFlights = maxFlights



    def AfegeixPassatgers(self, nPassatgers):
        if self.__nPassatgers <= self.maximPassatgers:
            self.__nPassatgers += nPassatgers
        else:
            print("El numero de passatgers afegits supera la capacitat de l'avió ")

    def EsborraPassatger(self, nPassatgers):
        if self.__nPassatgers >= nPassatgers:
            self.__nPassatgers -= nPassatgers
        else:
            print("El numero de passatgers a l'avió és inferior al numero a eliminar")

    def AfegirDestí(self, Destí):
        if len(self.__flights) < self.maximPassatgers:
                self.__flights.append(Destí)
        else:
            print("numero màxim de destins assolits")

    def EliminarDestí(self, Destí, preu):
        if Destí in self.__flights:
                self.__flights.remove(Destí)
        else:
            print("Destí a esborrar no trobat a la llista de destins")

    def ConsultarLlista(self):
        return self.__flights

    def getNumeroDestins(self):
        return len(self.__flights)

    def consultaPreu(self):
        preu = 0
        for el in self.__flights:
            preu += el.getPreu()
        return preu

    def getNPassatgers(self):
        return self.__nPassatgers