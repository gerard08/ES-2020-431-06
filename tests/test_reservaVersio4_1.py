import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV4_1(unittest.TestCase):


    @mock.patch('scripts.reserva.Bank')
    def test_ReservaV4_1(self,mock_Bank,):
        R41 = reserva()
        R41.afegirUsuari("", "", "", "", "")
        R41.afegirUsuari("", "", "", "", "")
        R41.afegirDesti("Madrid", "151", 80)
        R41.afegirDesti("Barcelona", "232", 120)
        mock_Bank.do_payment.return_value = False
        a,b = R41.RealitzarPagament("", "")
        assert b>1
        mock_Bank.do_payment.side_effect = [False,True,False,False,False,]
        a, b = R41.RealitzarPagament("", "")
        assert b==2 and a=="Pagament realitzat correctament"
        mock_Bank.do_payment.side_effect = [False,False,False,False,False]
        a, b = R41.RealitzarPagament("", "")
        assert b == 5 and a == "Error en el pagament"
