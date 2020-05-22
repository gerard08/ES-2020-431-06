class User:

    def __init__(self, nom, DNI, mail, ID, carnetcotxe):
        self.__nom = nom
        self.__DNI = DNI
        self.__mail = mail
        self.__ID = ID
        self.carnetcotxe = carnetcotxe

    def getID(self):
        return self.__ID

    def getNom(self):
        return self.__nom

    def getDNI(self):
        return self.__DNI

    def getMail(self):
        return self.__mail

    def setDrivingLicence(self, drivingLicense):
        self.__drivingLicense = drivingLicense

    def getDrivingLicence(self):
        return self.__drivingLicense