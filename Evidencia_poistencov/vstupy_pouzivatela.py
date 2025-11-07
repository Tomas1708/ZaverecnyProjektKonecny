from poistenec import Poistenec
from validacia_vstupu import ValidaciaVstupu

class VstupyUzivatela:
    """Ziskáva vstúpne údaje poistenca"""
    @staticmethod
    def ziskaj_udaje() -> tuple[str, str, str, int]:
        """Získa údaje poistenca zadané používateľom a následne ich vráti."""
        meno = ValidaciaVstupu.validacia_prazdneho_textu().strip()
        priezvisko = input("Zadáj priezvisko: ").strip()
        telefonne_cislo = ValidaciaVstupu.validacia_telefonneho_cisla().strip()
        vek = ValidaciaVstupu.validacia_veku_poistenca()
        return meno, priezvisko, telefonne_cislo, vek

class EvidenciaPoistenca:
    def __init__(self,databaza):
        self.databaza = databaza

    def pridaj_poistenca(self) -> None:
        """Vytvorí nového poistenca"""
        meno, priezvisko, telefonne_cislo, vek = VstupyUzivatela.ziskaj_udaje()
        poistenec = Poistenec(meno, priezvisko, telefonne_cislo, vek)
        self.databaza.pridaj_poistenca(poistenec)
        print(f"Poistenec: {poistenec}\nBol úspešne pridaný.\nPokračujte ľubovoľnou klavesou.")





