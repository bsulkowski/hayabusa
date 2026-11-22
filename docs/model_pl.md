# Wewnętrzny Układ Słoneczny – model i decyzje projektowe

## Dla kogo jest ten dokument

Ten dokument jest przeznaczony dla osób zainteresowanych tym, jak plansza ma się do rzeczywistej fizyki Układu Słonecznego: co zostało zamodelowane wiernie, co uproszczono i dlaczego. Może być przydatny zarówno dla projektantów gier chcących zmodyfikować planszę lub zainspirować się przy tworzeniu własnej, jak i dla graczy ciekawych astronomicznego kontekstu.

## Skala odległości

Skok siatki 0,5 AU na pierścień daje bardzo dobre przybliżenie dla planet aktywnie obecnych w grze:

| Obiekt | Rzeczywistość | Model | Błąd |
|--------|--------------|-------|------|
| Ziemia | 1,00 AU | 1,0 AU | 0% |
| Mars | 1,52 AU | 1,5 AU | −2% |
| Wewn. krawędź pasa | ~2,1 AU | 2,0 AU | −5% |
| Ceres | 2,77 AU | ~2,5 AU | −10% |
| Zewn. krawędź pasa | ~3,3 AU | 3,0 AU | −9% |

Ziemia i Mars wychodzą niemal idealnie. Pas planetoid jest lekko ściśnięty (o ok. 5–10%), ale jego szerokość – trzy pierścienie – jest zachowana.

### Merkury i Wenus

Merkury leży realnie przy 0,39 AU, Wenus przy 0,72 AU. W modelu obie planety trafiają do pierścienia 1 (0,5 AU) – żadna nie wychodzi dobrze. To świadoma decyzja: obie planety są w grach tłem, a nie aktywnymi lokacjami, więc dokładność ich położenia nie ma znaczenia dla rozgrywki.

## Układ odniesienia i prędkości orbitalne

### Skąd pochodzi ruch o 3/2/1/0 pól na turę

Projektując prędkości orbitalne, szukano liczb całkowitych, które najlepiej oddają proporcje rzeczywistych prędkości kątowych planet. Rzeczywiste prędkości kątowe Ziemi, Marsa i pasa planetoid są w przybliżeniu w proporcji **4 : 2 : 1**. 

Plansza obraca się w kierunku obiegu planet z prędkością odpowiadającą tej jednostce „1". Po odjęciu obrotu planszy widoczne prędkości na planszy wynoszą **3 : 1 : 0** – dokładnie to, co widzimy w tabeli ruchów.

Proporcja 4:2:1 jest przybliżeniem. Rzeczywiste wartości to ok. 4,6 : 2,4 : 1, co oznacza błąd rzędu 13–18%. Jednak po odjęciu obrotu planszy proporcja widoczna w grze (Ziemia:Mars = 3:1) odpowiada rzeczywistości z dokładnością poniżej 1% – model jest wewnętrznie spójny.

### Punkt odniesienia planszy

Plansza jest zsynchronizowana nie z Ceres (najbardziej znany obiekt pasa), lecz z orbitą o promieniu **2,24 AU** i okresie obiegu **3,36 roku**. To wewnętrzna część pasa planetoid, nieco bliżej Słońca niż Ceres. Wybór tego punktu wynika z dopasowania proporcji prędkości: przy synchronizacji z Ceres model Ziemia/Mars byłby mniej spójny wewnętrznie. Synchronizacja z 2,24 AU sprawia, że prędkości Ziemi i Marsa na planszy pasują do siebie niemal idealnie.

### Skala czasu

Długość rundy nie była zakładana z góry – wynika z całego modelu jako rezultat. Przy przyjętych proporcjach prędkości jedna runda odpowiada ok. **87 dniom** (nieco poniżej ćwierć roku). Wartość ¼ roku jest wygodna komunikacyjnie, ale lekko zawyża rzeczywisty czas rundy.

## Pas planetoid – dryf i losowość

### Nieuniknione uproszczenie

Pas planetoid nie jest tarczą obracającą się ze stałą prędkością – każda planetoida krąży z własną prędkością wynikającą z jej orbity. Obiekty bliżej Słońca krążą szybciej, obiekty dalej – wolniej. Plansza jest zsynchronizowana tylko z jednym punktem (2,24 AU), więc obiekty na innych orbitach w pasie będą dryfować:

| Obiekt | Odległość | Dryf względem planszy |
|--------|-----------|----------------------|
| Wewn. krawędź pasa | 2,06 AU | +0,24 pola/turę (za szybki) |
| Punkt synchronizacji | 2,24 AU | 0 |
| Ceres | 2,77 AU | −0,64 pola/turę |
| Zewn. krawędź pasa | 3,28 AU | −1,21 pola/turę |

W trakcie typowej gry (30–50 rund) Ceres dryfowałaby o kilkanaście do kilkudziesięciu pól, a zewnętrzna krawędź pasa jeszcze więcej.

### Dlaczego to nie jest problem

Modelowanie dryfowania poszczególnych obiektów wymagałoby śledzenia ułamkowych przesunięć, co znacząco skomplikowałoby rozgrywkę bez żadnej korzyści dla jakości decyzji gracza. Co ważniejsze – pas planetoid w rzeczywistości nie jest zbiorem obiektów, które dałoby się sensownie śledzić na planszy. To miliony ciał na nieznacznie różnych orbitach.

Losowe rozmieszczenie zasobów rzutem kości jest bliższe prawdzie niż jakikolwiek deterministyczny ruch mógłby oddać. Dryf jest świadomie pochłonięty przez losowość mechaniki pasa.

## Wybór kości do losowania w pasie planetoid

Do losowania pozycji w pasie planetoid użyto pary kości **k12 + k8** zamiast bardziej standardowych kombinacji. Decyzja wynika z dwóch praktycznych powodów.

Po pierwsze, k12 i k8 są łatwo rozróżnialne na pierwszy rzut oka – różnią się kształtem i rozmiarem. Nie trzeba rzucać nimi po kolei ani oznaczać kolorami: wyniki od razu wiadomo, który jest którym (k12 → sektor, k8 → heks w sektorze).

Po drugie, pas planetoid ma 90 heksów (pierścienie 4–6, łącznie `6×4 + 6×5 + 6×6 = 90`). Przy standardowej k6 losowanie z 90 pól wymagałoby trzech rzutów i nietrywialnego mapowania wyniku. Para k12 × k8 daje 96 kombinacji, co pokrywa 90 heksów z minimalną nadwyżką i prostym schematem: jeden rzut, dwa wyniki, jedna pozycja na planszy.

## Walor edukacyjny

Mimo uproszczeń model przekazuje rzeczy, których popularne wizualizacje Układu Słonecznego w ogóle nie pokazują:

- Planety poruszają się z różnymi prędkościami – i różnica jest odczuwalna podczas gry.
- Transfer między orbitami wymaga planowania w czasie: trzeba przewidzieć, gdzie będzie cel w momencie przybycia.
- Pas planetoid jest szeroki, nie cienki.
- Układ inercjalny to nie jedyna możliwość opisu ruchu – wybór układu odniesienia ma konsekwencje.

Błędy proporcji rzędu 15–30% są przy tym zupełnie nieistotne. Gracz bez wiedzy astronomicznej spotka model spójny i intuicyjny. Gracz z tą wiedzą rozpozna, że mechanika jest prawdziwa – tylko zaokrąglona do liczb, z którymi da się grać.
