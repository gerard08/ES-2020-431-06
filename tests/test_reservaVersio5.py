import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class testsV5(unittest.TestCase):

    @mock.patch('scripts.reserva.Booking')
    @mock.patch('scripts.reserva.Rentalcars')
    def test_ReservaV5(self, mock_Rentalcars, mock_Booking ):
        R5 = reserva(preu=0, usuaris=[], nUsuaris=0, llistaVols=[], llistaVehicles=[], pagament=PaymentData("","","","",""), allotjament=[], Destins=[])
        R5.afegirUsuari("", "", "", "", "")
        R5.afegirUsuari("", "", "", "", "")
        R5.afegirDesti("Madrid", "151", 80)
        R5.afegirDesti("Barcelona", "232", 120)
        assert R5.rellenar_dades_Facturació("PEPE",1456871430214742,"Visa",543)=="Dades correctes"
        assert R5.rellenar_dades_Facturació("143", "Lele", "Visas", 543517) == "Dades invalides"
        R5.rellenar_dades_Facturació("PEPE",1456871430214742,"Visa",543)
        Dades= R5.get_data_pagament()
        assert Dades.get_nomtitular()=="PEPE"
        assert Dades.get_codiseguretat()==543
        assert Dades.mostrar_tipus_targeta()=="Visa"
        assert Dades.mostra_import()==400
        assert Dades.mostra_num_targeta()==1456871430214742
        mock_Booking.confirm_reserve.return_value = False
        a, b = R5.ConfirmarReservaAllotjaments("", "")
        assert b > 1
        mock_Booking.confirm_reserve.side_effect = [False, True, False, False, False, ]
        a, b = R5.ConfirmarReservaAllotjaments("", "")
        assert b == 2 and a == "Reserva realitzada correctament"
        mock_Booking.confirm_reserve.side_effect = [False, False, False, False, False]
        a, b = R5.ConfirmarReservaAllotjaments("", "")
        assert b == 5 and a == "Error en la reserva"
        mock_Rentalcars.confirm_reserve.return_value = False
        a, b = R5.ConfirmarReservaCoches("", "")
        assert b > 1
        mock_Rentalcars.confirm_reserve.side_effect = [False, True, False, False, False, ]
        a, b = R5.ConfirmarReservaCoches("", "")
        assert b == 2 and a == "Reserva realitzada correctament"
        mock_Rentalcars.confirm_reserve.side_effect = [False, False, False, False, False]
        a, b = R5.ConfirmarReservaCoches("", "")
        assert b == 5 and a == "Error en la reserva"