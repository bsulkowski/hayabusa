# Pionki 3D

*[English version](README.md)*

Uniwersalne pionki do druku 3D, do wykorzystania w dowolnej grze na tej planszy.

![Podgląd modeli](preview.png)

| Plik | Model | Wymiary |
|------|-------|---------|
| [ship.stl](ship.stl) | statek transportowy – modułowy kadłub na kręgosłupie, z dyszami na dole; inspirowany pośrednio statkiem Eagle 1 z serialu „Kosmos 1999” | 26 × 26 × 36 mm |
| [outpost.stl](outpost.stl) | placówka na planetoidzie, z anteną do dalekiej komunikacji | 30 × 30 × 24 mm |

## Rozmiar

Plansza jest przeznaczona do druku w formacie A2. Pole ma wtedy ok. 30 mm między bokami, a pionek mieści się w jednym polu przy szerokości do ok. 27 mm.

- **Statek** mieści się bez skalowania. Nie ma podstawki – ma się dać swobodnie obracać w palcach, a podstawka zasłaniałaby dysze. Dobrze stoi również na boku.
- **Placówka** zajmuje prawie całe pole – warto ją drukować w skali ok. 0,9.

## Druk

- Statek potrzebuje podpór pod dolnymi modułami (najlepiej drzewiastych); placówka drukuje się bez podpór.
- Statek stoi na stole drukarki na trzech małych dyszach – pomóc może brim.

## Do poprawy

- Plik statku jest zapisany w metrach, placówki w milimetrach. Część slicerów wczyta statek w złej skali – trzeba go przeskalować ×1000 albo wyeksportować ponownie w milimetrach.
- Oba modele składają się z nachodzących na siebie brył. Slicery zwykle sobie z tym radzą, ale przed publikacją warto je połączyć (Boolean Union albo „Make Manifold” w Blenderze). W statku jest też zabłąkany podwójny trójkąt o zerowej grubości.
- Antena placówki ma miejsca grube na 0,1–0,5 mm – do pogrubienia do min. ok. 1 mm w docelowej skali.
