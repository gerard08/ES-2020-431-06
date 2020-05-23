import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV2(unittest.TestCase):
    @mock.patch('scripts.reserva.Bank')
    @mock.patch('scripts.reserva.Skyscanner')
    def test_ReservaV2(self, mock_Bank, mock_Skyscanner):
        R = reserva()
        R.afegirUsuari("", "", "", "", "")
        R.afegirUsuari("", "", "", "", "")
        R.afegirDesti("Madrid", "151", 80)
        R.afegirDesti("Barcelona", "232", 120)
        R.seleccionar_metode_pagament("Visa")
        a = R.get_data_pagament()
        assert a.mostrar_tipus_targeta() == "Visa"
        mock_Bank.do_payment.return_value = False
        mock_Skyscanner.confirm_reserve.return_value = False
        a, b = R.RealitzarPagament("", "")
        assert a == "Error en el pagament"
        a, b = R.ConfirmarReservaVols("", "")
        assert a == "Error en la reserva"