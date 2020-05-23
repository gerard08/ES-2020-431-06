import unittest
from scripts.reserva import reserva
from scripts.Desti import Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV3(unittest.TestCase):

    @mock.patch('scripts.reserva.Booking')
    @mock.patch('scripts.reserva.Rentalcars')
    def test_ReservaV3(self, mock_Rentalcars, mock_Booking):
        R3 = reserva(preu=0, usuaris=[], nUsuaris=0, llistaVols=[], llistaVehicles=[], pagament=PaymentData("","","","",""), allotjament=[], Destins=[])
        R3.afegirUsuari("", "", "", "", "")
        R3.afegirUsuari("", "", "", "", "")
        R3.afegirVehicle("", "45682484A", "", 3, 25)
        assert R3.get_preu() == 75
        R3.eliminarVehicle("45682484A")
        assert R3.get_preu() == 0
        R3.afegirAllotjament("", 200, "", "", "AUS 548", 4)
        assert R3.get_preu() == 800
        R3.eliminarAllotjament("AUS 548")
        assert R3.get_preu() == 0
        mock_Rentalcars.confirm_reserve.return_value = True
        mock_Booking.confirm_reserve.return_value = True
        a, b = R3.ConfirmarReservaCoches("", "")
        assert a == "Reserva realitzada correctament"
        a, b = R3.ConfirmarReservaAllotjaments("", "")
        assert a == "Reserva realitzada correctament"
        mock_Rentalcars.confirm_reserve.return_value = False
        mock_Booking.confirm_reserve.return_value = False
        a, b = R3.ConfirmarReservaCoches("", "")
        assert a == "Error en la reserva"
        a, b = R3.ConfirmarReservaAllotjaments("", "")
        assert a == "Error en la reserva"
