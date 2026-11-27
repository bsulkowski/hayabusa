# Obliczenia

*[English version](README.md)*

Skrypty, którymi policzono liczby w [opisie modelu](../docs/model_pl.md). Każdy wypisuje tabele w tej samej postaci, w jakiej trafiły do dokumentacji. Skrypty wypisują wyniki po angielsku.

Model fizyczny: Słońce i statek (zagadnienie dwóch ciał), orbity kołowe i współpłaszczyznowe. Trasy między orbitami liczone są jako optymalne łuki (zagadnienie Lamberta) albo transfer Hohmanna, lot swobodny – przez numeryczne całkowanie ruchu.

| Skrypt | Co liczy | Rozdział opisu modelu |
|--------|----------|-----------------------|
| `orbits.py` | wspólne funkcje i parametry planszy (punkt synchronizacji, długość rundy) | – |
| `board_model.py` | punkt synchronizacji, ruch pierścieni, dryf pasa, okna transferowe i kąty startu | Układ odniesienia, Pas planetoid, Okna transferowe |
| `reference_model.py` | koszt zaplanowanych tras w tempie gry | Dlaczego model referencyjny ma sens |
| `coasting.py` | zakrzywienie toru przy locie swobodnym, koszt utrzymania kursu, sprawdzenie prostej zasady zakrzywiania | Dlaczego nie prosta linia dosłownie |
| `simplified_model.py` | kalibracja modelu uproszczonego, koszt przy jednakowym czasie lotu | Model uproszczony |
| `propulsion.py` | zasięg zbiornika, ciąg i moc dla różnych napędów, start z powierzchni, tankowanie wodą z planetoid | Napęd i paliwo, Start z powierzchni |

## Uruchomienie

Potrzebny jest Python 3 z bibliotekami `numpy` i `scipy`:

```
pip install numpy scipy
cd tools
python board_model.py
```

Skrypty `coasting.py` i `simplified_model.py` liczą się kilkadziesiąt sekund.

## Generator planszy

`board_svg.py` rysuje planszę i zapisuje wszystkie pliki w [`board/`](../board): całą planszę w SVG, PDF-y do druku na kartkach A4 (A2 z 4, A3 z 2, sklejanych na styk), podglądy i kody QR – w dwóch językach i dwóch wersjach kolorystycznych. Grafikę planszy zmienia się tutaj, nie w plikach.

Potrzebny jest Python 3 z biblioteką `segno` (kody QR), `rsvg-convert` (PDF i PNG; w Windows np. w WSL: `sudo apt install librsvg2-bin`) i kroje Exo 2 oraz Orbitron (Google Fonts):

```
pip install segno
cd tools
python board_svg.py
```

Zdjęcia Ziemi, Marsa, Ceres i Westy skrypt bierze z `board/images/` (`earth.jpg`, `mars.jpg`, `ceres.jpg`, `vesta.jpg` albo `.png`; kwadratowe, planeta wypełnia kadr); bez nich rysuje koła w jednolitych kolorach. Ostrzega też, gdy napis trafia na łączenie kartek.

Bez `rsvg-convert` skrypt zapisuje tylko pliki SVG (`--svg-only` robi to samo celowo).

## Licencja

Kod w tym folderze jest dostępny na licencji [MIT](LICENSE).
