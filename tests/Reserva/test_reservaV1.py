import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock

class testMockV1(unittest.TestCase):
    @mock.patch('scripts.reserva')

    def test_ReservaV1(self,mock_reserva):

        R = reserva()
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
        b.append(Flights("","","151","","","","",""))
        assert R.get_llistatVols()==b
        R.afegirUsuari("", "", "", "", "")
        p=80*2
        assert p == R.get_preu()
        R.afegirDesti("Barcelona", "232", 120)
        R.eliminarDesti("232")
        assert p == R.get_preu()
        assert R.get_llistatVols() == b
        assert R.get_Destins() == a