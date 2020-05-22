from Flights import *


if __name__ == '__main__':
    viatges = Flights(10)

    #intento eliminar un passatger sabent que no n'hi ha cap registrat
    viatges.EsborraPassatger(2)
    #afegeixo un passatger
    viatges.AfegeixPassatgers(2)
    #elimino un passatger
    viatges.EsborraPassatger(1)
    #miro el numero de passatger
    print(viatges.getNPassatgers())
    #afegeixo un vol amb preu negatiu
    viatges.AfegirDestí('Londres', -500)
    #afegeixo dos vols correctament
    viatges.AfegirDestí('Londres', 500)
    viatges.AfegirDestí('Madrid', 250)
    #elimino un vol que no existeix
    viatges.EliminarDestí('París', 300)
    #consulto preu total
    print(viatges.consultaPreu())
    #consulto llista vols
    print(viatges.ConsultarLlista())
    #elimino el destí correctament
    viatges.EliminarDestí('Londres', 500)
    #consulto llista vols (un altre cop)
    print(viatges.ConsultarLlista())
    #consulto preu total(un altre cop)
    print(viatges.consultaPreu())