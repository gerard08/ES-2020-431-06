import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV3(unittest.TestCase):

    @mock.patch('scripts.reserva.Booking')
    @mock.patch('scripts.reserva.Rentalcars')
    def test_ReservaV3(self, mock_Rentalcars, mock_Booking):
        R = reserva()
        R.afegirUsuari("", "", "", "", "")
        R.afegirUsuari("", "", "", "", "")
        R.afegirVehicle("", "45682484A", "", 3, 25)
        assert R.get_preu() == 75
        R.eliminarVehicle("45682484A")
        assert R.get_preu() == 0
        R.afegirAllotjament("", 200, "", "", "AUS 548", 4)
        assert R.get_preu() == 800
        R.eliminarAllotjament("AUS 548")
        assert R.get_preu() == 0
        mock_Rentalcars.confirm_reserve.return_value = True
        mock_Booking.confirm_reserve.return_value = True
        a, b = R.ConfirmarReservaCoches("", "")
        assert a == "Reserva realitzada correctament"
        a, b = R.ConfirmarReservaAllotjaments("", "")
        assert a == "Reserva realitzada correctament"
        mock_Rentalcars.confirm_reserve.return_value = False
        mock_Booking.confirm_reserve.return_value = False
        a, b = R.ConfirmarReservaCoches("", "")
        assert a == "Error en la reserva"
        a, b = R.ConfirmarReservaAllotjaments("", "")
        assert a == "Error en la reserva"