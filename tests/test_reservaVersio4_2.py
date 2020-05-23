import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV4_2(unittest.TestCase):
     @mock.patch('scripts.reserva.Skyscanner')
     def test_ReservaV4_2(self, mock_Skyscanner, ):
         R42 = reserva(preu=0, usuaris=[], nUsuaris=0, llistaVols=[], llistaVehicles=[], pagament=PaymentData("","","","",""), allotjament=[], Destins=[])
         R42.afegirUsuari("", "", "", "", "")
         R42.afegirUsuari("", "", "", "", "")
         R42.afegirDesti("Madrid", "151", 80)
         R42.afegirDesti("Barcelona", "232", 120)
         mock_Skyscanner.confirm_reserve.return_value= False
         a, b = R42.ConfirmarReservaVols("", "")
         assert b > 1
         mock_Skyscanner.confirm_reserve.side_effect = [False, True, False, False, False, ]
         a, b = R42.ConfirmarReservaVols("", "")
         assert b == 2 and a == "Reserva realitzada correctament"
         mock_Skyscanner.confirm_reserve.side_effect = [False, False, False, False, False]
         a, b = R42.ConfirmarReservaVols("", "")
         assert b == 5 and a == "Error en la reserva"