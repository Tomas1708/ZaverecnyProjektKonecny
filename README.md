# Evidencia poistencov
Projekt evidencie poistencov implementovaný v programovacom jazyku Python.
Obsahuje dve verzie aplikácie: 
- **Konzolová aplikácia** - jednoduché textové menu v termináli
- **Webová aplikácia (Django)** - webové rozhranie s databázou 

## Funkcionalita
### Konzolová aplikácia
- Pridanie nového poistenca
- Výpis všetkých poistencov
- Vyhľadávanie poistenca podľa mena a priezviska
- Validácia vstupov

### Webová aplikácia (Django)
- Správa poistencov
- Vytváranie a úprava poistení
- Autentifikácia používateľov
- Obmedzenie prístupu podľa používateľa

## Architektúra projektu
```
Evidencia_poistencov/
│
├── console_app/
│   ├── evidencia.py    # Správa databázy poistencov a aplikačná logika
│   ├── menu.py         # Konzolové menu a výpisy pre používateľa
│   ├── poistenec.py    # Dátový model poistenca
│   ├── validacia.py    # Validácia vstupov používateľa
│   ├── vstupy.py       # Získavanie údajov o poistencovi od používateľa
│   └── main.py         # Vstupný bod aplikácie
│
├── web_app/
│   ├── accounts/       # Autentifikácia používateľov
│   ├── policyholders/  # Správa poistencov a poistení
│   ├── web_app/        # Django projekt (settings, urls)  
│   └── manage.py
│
└── README.md
```
## Princípy návrhu
Projekt je navrhnutý podľa základných princípov, ktoré zabezpečujú čistý a udržiavateľný kód:
- **Separation of Concerns (SoC):** oddelenie jednotlivých časti aplikácie
- **Single Responsibility Principle (SRP):** Každý modul má jednu zodpovednosť
- **OOP** - využitie objektovo orientovaného programovania

## Použítie technológie 
- Python
- Django
- HTML
- Bootstrap
- SQLite
- Git

## Spustenie aplikácie
### Konzola
- Uistite sa, že máte nainštalovaný Python. 
- V koreňovom priečinku projektu spustite príkaz: python main.py 
- Aplikácia sa spustí v termináli a zobrazí hlavné menu. 
### Django
- Uistite sa, že ste v koreňovom priečinku web_app
- Server spustíte príkazom v terminali: python manage.py runserver
- Aplikácia bude dostupná na: http://127.0.0.1:8000

## Autor
Projekt je ukážkou vývoja aplikácie v Pythone - najprv konzolovej verzie a následne rozšírenej o webové rozhranie 
pomocou frameworku Django.
