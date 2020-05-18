class Flights:

    #'Flights' encapsula la API externa proporcionada per Skyscanner.com
    # La classe 'Flights' conté la llista de vols pels quals es vol confirmar la reserva. De cada vol té la següent informació:
    #- Codi del vol
    #- Destinació
    #- Número de passatgers

    def __init__(self):
        self.source = ''
        self.destination = ''
        self.codiVol = ''
        self.nPassatgers = 0
        self.datesource = ''
        self.dateDestination = ''
        self.flights = []
        self.maximPassatgers = 365
        self.preu = 0



    def AfegeixPassatgers(self, nPassatgers):
        if self.nPassatgers <= self.maximPassatgers:
            self.nPassatgers += nPassatgers
        else:
            print("El numero de passatgers afegits supera la capacitat de l'avió ")

    def EsborraPassatger(self, nPassatgers):
        if self.nPassatgers >= nPassatgers:
            self.nPassatgers -= nPassatgers
        else:
            print("El numero de passatgers a l'avió és inferior al numero a eliminar")

    def AfegirDestí(self, Destí, preu):
        self.flights.append(Destí)
        self.preu += preu

    def EliminarDestí(self, Destí, preu):
        if Destí in self.flights:
            self.flights.remove(Destí)
            self.preu -= preu

    def ConsultarLlista(self):
        return self.flights

    def getNumeroDestins(self):
        return len(self.flights)

    def consultaPreu(self):
        return self.preu
