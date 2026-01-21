class DatabazaPoistencov:
    """Reprezentuje databázu poistencov."""

    def __init__(self):
        """Inicializujeme sukromný prázdny zoznam."""
        self._poistenci = []

    def pridaj_poistenca(self,poistenec):
        """Pridá poistenca do databázy."""
        self._poistenci.append(poistenec)

    @property
    def poistenci(self):
        """Pre spristupnenie iným metódam bez možnosti modifikácie."""
        return tuple(self._poistenci)

class HladanyPoistenec:
    """Vyhľadá poistenca v databáze podľa mena a priezviska"""

    def __init__(self,databaza):
        self.databaza = databaza

    def vyhladaj_pouzivatela(self,meno: str, priezvisko: str):
        """Vyhľada poistenca podľa mena a priezvíska a vypíše jeho údaje"""

        for poistenec in self.databaza.poistenci:
            if  poistenec.meno == meno and poistenec.priezvisko == priezvisko:
                print(f"\nÚdaje poistenca: {poistenec}\nPokračujte ľubovoľnou klavesou.")
                return
        print("Poistenec sa nenašiel.\nPokračujte ľuobovoľnou klavesou.")


