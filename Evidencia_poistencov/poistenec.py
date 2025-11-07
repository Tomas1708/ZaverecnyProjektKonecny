class Poistenec:
    """Reprezentuje poistenca a jeho osobné údaje."""
    def __init__(self, meno: str, priezvisko: str, telefonne_cislo: str, vek: int) -> None:
        """Inicializuje poistenca so zadaným menom a priezviskom, tel. číslom a vekom"""
        self.meno = meno
        self.priezvisko = priezvisko
        self.telefonne_cislo = telefonne_cislo
        self.vek = vek

    def __str__(self) -> str:
        """Vratí textovú reprezentáciu poistenca"""
        return f"{self.meno} {self.priezvisko} | Tel. číslo: {self.telefonne_cislo} | Vek: {self.vek}"
