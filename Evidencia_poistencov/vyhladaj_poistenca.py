class RozhranieHladanehoPoistenca:
    """Trieda zabezpečuje získanie mena a priezviska hľadaného poistenca od používateľa"""
    @staticmethod
    def ziskaj_hladaneho_poistenca() -> tuple[str, str]:
        """Metóda získa meno a priezvisko hľadaného poistenca a vrácia ich ako n-ticu"""

        meno_hladaneho = input(f"Zadajte meno hľadaného poistenca: ").strip()
        priezvisko_hladaneho = input(f"Zadajte priezvisko hľadaného poistenca: ").strip()
        return meno_hladaneho, priezvisko_hladaneho


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
