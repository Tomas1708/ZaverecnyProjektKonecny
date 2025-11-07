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

