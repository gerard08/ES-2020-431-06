import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV1(unittest.TestCase):



    def test_ReservaV1(self):

        R = reserva(preu=0, usuaris=[], nUsuaris=0, llistaVols=[], llistaVehicles=[], pagament=PaymentData("","","","",""), allotjament=[], Destins=[])
        R.afegirUsuari("","","","","")
        assert R.get_nUsuaris()== 1
        assert R.get_llistatVols() == []
        assert R.get_Destins() == []
        assert R.get_preu() == 0
        R.afegirDesti("Madrid","151",80)
        p=80
        assert p==R.get_preu()
        a=[]
        a.append(Desti("Madrid","151",80))
        assert R.get_Destins()==a
        b=[]
        b.append(Flights("","","151","","",""))
        assert R.get_llistatVols()==b
        R.afegirUsuari("", "", "", "", "")
        p=80*2
        assert p == R.get_preu()
        R.afegirDesti("Barcelona", "232", 120)
        R.eliminarDesti("232")
        assert p == R.get_preu()
        assert R.get_llistatVols() == b
        assert R.get_Destins() == a

        a,b= R.RealitzarPagament("p","l")
        assert a=="Pagament realitzat correctament"
        a, b = R.ConfirmarReservaVols("p", "l")
        assert a == "Reserva realitzada correctament"


