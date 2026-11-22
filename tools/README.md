# Obliczenia

Skrypty, którymi policzono liczby w [opisie modelu](../docs/model_pl.md). Każdy wypisuje tabele w tej samej postaci, w jakiej trafiły do dokumentacji.

Model fizyczny: Słońce i statek (zagadnienie dwóch ciał), orbity kołowe i współpłaszczyznowe. Trasy między orbitami liczone są jako optymalne łuki (zagadnienie Lamberta) albo transfer Hohmanna, lot swobodny – przez numeryczne całkowanie ruchu.

| Skrypt | Co liczy | Rozdział opisu modelu |
|--------|----------|-----------------------|
| `orbits.py` | wspólne funkcje i parametry planszy (punkt synchronizacji, długość rundy) | – |
| `board_model.py` | punkt synchronizacji, ruch pierścieni, dryf pasa, okna transferowe i kąty startu | Układ odniesienia, Pas planetoid, Okna transferowe |
| `reference_model.py` | koszt zaplanowanych tras w tempie gry | Dlaczego model referencyjny ma sens |
| `coasting.py` | zakrzywienie toru przy locie swobodnym, koszt utrzymania kursu, sprawdzenie prostej zasady zakrzywiania | Dlaczego nie prosta linia dosłownie |
| `simplified_model.py` | kalibracja modelu uproszczonego, koszt przy jednakowym czasie lotu | Model uproszczony |
| `propulsion.py` | zasięg zbiornika, ciąg i moc dla różnych napędów | Napęd i paliwo |

## Uruchomienie

Potrzebny jest Python 3 z bibliotekami `numpy` i `scipy`:

```
pip install numpy scipy
cd tools
python board_model.py
```

Skrypty `coasting.py` i `simplified_model.py` liczą się kilkadziesiąt sekund.
