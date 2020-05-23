import unittest
from scripts.reserva import reserva
from scripts.Desti import  Desti
from scripts.Flights import Flights
from unittest import mock
from scripts.User import User
from scripts.PaymentData import PaymentData
class tests(unittest.TestCase):



    def test_ReservaV1(self):

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

        a,b= R.RealitzarPagament("p","l")
        assert a=="Pagament realitzat correctament"
        a, b = R.ConfirmarReservaVols("p", "l")
        assert a == "Reserva realitzada correctament"

    @mock.patch('scripts.reserva.Bank')
    @mock.patch('scripts.reserva.Skyscanner')
    def test_ReservaV2(self,mock_Bank,mock_Skyscanner):
        R = reserva()
        R.afegirUsuari("", "", "", "", "")
        R.afegirUsuari("", "", "", "", "")
        R.afegirDesti("Madrid", "151", 80)
        R.afegirDesti("Barcelona", "232", 120)
        R.seleccionar_metode_pagament("Visa")
        a=R.get_data_pagament()
        assert a.mostrar_tipus_targeta()=="Visa"
        mock_Bank.do_payment.return_value = False
        mock_Skyscanner.confirm_reserve.return_value = False
        a,b= R.RealitzarPagament("","")
        assert a=="Error en el pagament"
        a,b =R.ConfirmarReservaVols("","")
        assert a== "Error en la reserva"

    @mock.patch('scripts.reserva.Rentalcars')
    @mock.patch('scripts.reserva.Booking')
    def test_ReservaV3(self,mock_Rentalcars,mock_Booking):
        R = reserva()
        R.afegirUsuari("", "", "", "", "")
        R.afegirUsuari("", "", "", "", "")
        R.afegirVehicle("","45682484A","",3,25)
        assert R.get_preu()==75
        R.eliminarVehicle("45682484A")
        assert R.get_preu()==0
        R.afegirAllotjament("", 200, "", "","AUS 548" ,4)
        assert R.get_preu() == 800
        R.eliminarAllotjament("AUS 548")
        assert R.get_preu() == 0
        mock_Rentalcars.confirm_reserve.return_value = True
        mock_Booking.confirm_reserve.return_value = True
        a,b= R.ConfirmarReservaCoches("", "")
        assert a== "Reserva realitzada correctament"
        a,b= R.ConfirmarReservaAllotjaments("", "")
        assert a== "Reserva realitzada correctament"
        mock_Rentalcars.confirm_reserve.return_value = False
        mock_Booking.confirm_reserve.return_value = False
        a, b = R.ConfirmarReservaCoches("", "")
        assert a == "Error en la reserva"
        a, b = R.ConfirmarReservaAllotjaments("", "")
        assert a == "Error en la reserva"

    @mock.patch('scripts.reserva.Bank')
    def test_ReservaV4(self,mock_Bank):
        R = reserva()
        R.afegirUsuari("", "", "", "", "")
        R.afegirUsuari("", "", "", "", "")
        R.afegirDesti("Madrid", "151", 80)
        R.afegirDesti("Barcelona", "232", 120)
        mock_Bank.do_payment.return_value = 1245
        a,b = R.RealitzarPagament("", "")
        assert b>1
        mock_Bank.do_payment.side_effect = [False,True]
        a, b = R.RealitzarPagament("", "")
        assert b==2 and a=="Pagament realitzat correctament"
        mock_Bank.do_payment.return_value = False
        assert b == 5 and a == "Error en el pagament"