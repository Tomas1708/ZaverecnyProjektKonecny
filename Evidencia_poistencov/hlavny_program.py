"""Importy"""
from databaza_poistencov import DatabazaPoistencov, ZoznamPoistencov
from vstupy_pouzivatela import  EvidenciaPoistenca
from vyhladaj_poistenca import HladanyPoistenec, RozhranieHladanehoPoistenca
from validacia_vstupu import ValidaciaVstupu
from zobrazenie_menu import ZobrazenieMenu

"""Vytvorenie inštancií, pre zobrazene menu, databázy a validácií"""
ZobrazenieMenu().zobraz_menu()
databaza = DatabazaPoistencov()
validacia_vstupu = ValidaciaVstupu()

proces = True
while proces:
    moznost = validacia_vstupu.ziskaj_volbu()
    match moznost:
        case 1:
            """Akcia pridania poistenca do databázy"""
            vstupy = EvidenciaPoistenca(databaza)
            vstupy.pridaj_poistenca()
        case 2:
            """Akcia výpisu všetkých poistencov"""
            zoznam_poistencov = ZoznamPoistencov(databaza)
            zoznam_poistencov.vypis_poistencov()
        case 3:
            """Akcia vyhľadania konkretného poistenca na základe mena a priezviska"""
            rozhranie_hladaneho_poistenca = RozhranieHladanehoPoistenca()
            meno, priezvisko = RozhranieHladanehoPoistenca.ziskaj_hladaneho_poistenca()

            hladany_poistenec = HladanyPoistenec(databaza)
            vysledok = hladany_poistenec.vyhladaj_pouzivatela(meno, priezvisko)
        case 4:
            """Akcia pre ukončenie appky"""
            proces = False




