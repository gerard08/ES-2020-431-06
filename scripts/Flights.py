class Flights:


    def __init__(self, maxFlights):
        self.source = ''
        self.destination = ''
        self.codiVol = ''
        self.__nPassatgers = 0
        self.datesource = ''
        self.dateDestination = ''
        self.__flights = []
        self.maximPassatgers = 365
        self.__preu = 0
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

    def AfegirDestí(self, Destí, preu):
        if len(self.__flights) < self.maximPassatgers:
            if preu > 0:
                self.__flights.append(Destí)
                self.__preu += preu
            else:
                print("El preu no pot ser negatiu")
        else:
            print("numero màxim de destins assolits")

    def EliminarDestí(self, Destí, preu):
        if Destí in self.__flights:
            if preu > 0:
                self.__flights.remove(Destí)
                self.__preu -= preu
            else:
                print("El preu no pot ser negatiu")
        else:
            print("Destí a esborrar no trobat a la llista de destins")

    def ConsultarLlista(self):
        return self.__flights

    def getNumeroDestins(self):
        return len(self.__flights)

    def consultaPreu(self):
        return self.__preu

    def getNPassatgers(self):
        return self.__nPassatgers