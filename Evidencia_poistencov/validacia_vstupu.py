class ValidaciaVstupu:
    """Reprezentuje validáciu výberu akcie používateľa."""

    def __init__(self) -> None:
        """Inicializuje rozsah možnosti výberu akcií."""
        self.min = 1
        self.max = 4

    def ziskaj_volbu(self) -> int:
        """Zabezpečuje, aby používateľ zadal číslo v platnom rozsahu."""

        while True:
            try:
                volba = int(input("Voľba: "))
                if self.min <= volba <= self.max:
                    return volba
                else:
                    print(f"Zadaj číslo od {self.min}-{self.max}!")
            except ValueError:
                print(f"Musíš zadať číslo od {self.min}-{self.max}!")

    @staticmethod
    def validacia_prazdneho_textu() -> str:
        """Zaisťuje, že používateľ nezada prázdny text."""

        meno = input("Zadáj meno poisteného: ").strip()
        while not meno:
            print("Meno nesmie byť prázdne!")
            meno = input("Zadáj meno poisteného: ").strip()
        return meno

    @staticmethod
    def validacia_veku_poistenca() -> int:
        """Zaisťuje zadanie platného nezáporného veku poistenca."""

        vek = input("Zadajte vek poisteného: ").strip()
        while True:
            if not vek:
                print("Vek nesmie byť prázdny!")
            else:
                try:
                    vek = int(vek)
                    if vek < 0:
                        print("Vek nesmie byť záporny!")
                    else:
                        return vek
                except ValueError:
                    print("Musíte zadať platné číslo!")
            vek = input("Zadajte vek poisteného: ").strip()

    @staticmethod
    def validacia_telefonneho_cisla() -> str:
        """Zaisťuje správny format telefonného čísla podľa slovenskej predvoľby."""

        predcislie_slovensko = "+421"
        telefonne_cislo = input("Zadajte telefónne číslo: ").strip()

        while True:
            if not telefonne_cislo:
                print("Telefónne číslo nesmie byť prázdne.")
            elif telefonne_cislo.startswith(predcislie_slovensko):
                orezat = telefonne_cislo[len(predcislie_slovensko)::]
                if len(orezat) == 9 and orezat.isdigit():
                    return telefonne_cislo
                else:
                    print("Telefónne číslo musí mať 9 číslic po predvoľbe +421!")
            elif telefonne_cislo.startswith("0") and len(telefonne_cislo) == 10 and telefonne_cislo.isdigit():
                orezat = telefonne_cislo[1::]
                return f"{predcislie_slovensko}{orezat}"
            else:
                print("Neplatný format, skúste to znova!")
            telefonne_cislo = input("Zadajte telefónne číslo: ").strip()




