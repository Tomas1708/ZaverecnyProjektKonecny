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

class ZoznamPoistencov:
    """Slúži na vypísanie poistencov z databazy."""

    def __init__(self,databaza):
        """Inicializuje triedu s odkazom na databázu poistencov."""
        self.databaza = databaza

    def vypis_poistencov(self) -> None:
        """Vypíše údaje všetkých poistencov nachádzajúcich v databáze"""
        if not self.databaza.poistenci:
            print("Databáza je prázdna.")
        else:
            for index, poistenec in enumerate(self.databaza.poistenci, start=1):
                print(f"{index}. {poistenec}")
        print("\nPokračujte ľubovoľnou klavesou.")