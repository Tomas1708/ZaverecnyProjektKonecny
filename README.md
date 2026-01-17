## Evidencia poistencov - konzolová aplikácia v Pythone
Projekt je navrhnutý podľa princípov **Separation of Concerns (SoC)** a s využitím **Objektovo orientovaného 
programovania (OOP)**. 
Aplikácia umožňuje používateľoví spravovať zoznam poistencov prostredníctvom textového menu v termináli.

## Funkcionalita
- Pridanie nového poistenca
- Výpis všetkých poistencov
- Vyhľadávanie poistencia na základe mena a priezviska
- Konzolové menu s validáciou vstupov

## Architektúra projektu
```
Evidencia_poistencov/
├── evidencia.py    # Správa databázy poistencov a aplikačná logika
├── menu.py         # Konzolové menu a výpisy pre používateľa
├── poistenec.py    # Dátový model poistenca
├── validacia.py    # Validácia vstupov používateľa
├── vstupy.py       # Získavanie údajov o poistencovi od používateľa
└── main.py         # Vstupný bod aplikácie
```
## Princípy návrhu
Projekt je navrhnutý podľa základných princípov, ktoré zabezpečujú čistý a udržiavateľný kód:
- **Separation of Concerns (SoC):** Každý modul rieši samostatnú časť funkcionality.
- **Single Responsibility Principle (SRP):** Triedy a moduly majú len jednu zodpovednosť.
- **Objektovo orientované programovanie (OOP):** Kód je organizovaný pomocou tried.

## Spustenie aplikácie
1. Uistite sa, že máte nainštalovaný Python.
2. V koreňovom priečinku projektu spustite príkaz: python main.py
3. Aplikácia sa spustí v termináli a zobrazí hlavné menu.

## Autor
Projekt bol vytvorený ako ukážka jednoduchej konzolovej aplikácie v programovacom jazyku Python s dôrazom 
na správnu architektúru a best practices.
