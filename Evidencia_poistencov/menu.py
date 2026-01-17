class ZobrazenieMenu:
    """Trieda, ktorá sa stará o zobrazenie menu"""

    MENU_TEXT = (
        "-------------------------------\n"
        "Evidencia poistených\n"
        "-------------------------------\n"
        "Vyberte si akciu:\n"
        "1 - Pridať nového poisteného\n"
        "2 - Vypisať všetkých poistených\n"
        "3 - Vyhľadať pisteného\n"
        "4 - Koniec\n")

    def zobraz_menu(self) -> None:
        """slúži na zobrazenie hlavného menu"""
        print(self.MENU_TEXT)

class RozhranieHladanehoPoistenca:
    """Trieda zabezpečuje získanie mena a priezviska hľadaného poistenca od používateľa"""
    @staticmethod
    def ziskaj_hladaneho_poistenca() -> tuple[str, str]:
        """Metóda získa meno a priezvisko hľadaného poistenca a vrácia ich ako n-ticu"""

        meno_hladaneho = input(f"Zadajte meno hľadaného poistenca: ").strip()
        priezvisko_hladaneho = input(f"Zadajte priezvisko hľadaného poistenca: ").strip()
        return meno_hladaneho, priezvisko_hladaneho


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

