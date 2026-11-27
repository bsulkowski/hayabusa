# Hayabusa – filozofia projektu

*[English version](design.md)*

Ten dokument zbiera zasady, według których plansza jest projektowana – czym ma być i co jest ważniejsze, gdy cele się kłócą. Jak poszczególne elementy mają się do rzeczywistości, opisuje [model planszy](model_pl.md).

## Plansza, nie gra

Plansza nie jest przypisana do jednej gry – to przestrzeń, na której można budować różne gry. Cel gry, zasoby, wydarzenia i reszta zasad należą do konkretnej gry.

Wynikają z tego trzy rzeczy:

- Plansza daje fizykę i model lotów, a nie fabułę. Kontekst to początki eksploracji kosmosu i zasoby pasa planetoid, ale świat dookoła buduje gra.
- [Pionki 3D](../models/README_pl.md) są uniwersalne – to statek transportowy i placówka, a nie bohaterowie konkretnej gry.
- [Pomysły na gry](ideas_pl.md) są materiałem do wykorzystania, a nie zasadami.

## Twarda science fiction

Fizyka jest prawdziwa, z przyszłości pochodzą tylko silniki statków. Odległości i prędkości orbitalne zachowują rzeczywiste proporcje, okna transferowe powtarzają się tak często jak w rzeczywistości, a statki płacą za zmianę prędkości, nie za przebytą drogę.

Zasada obowiązuje do końca, także w szczegółach: statki to duże frachtowce, a nie lekkie sondy, i każdy element pionków ma uzasadnienie w fizyce i technice opisanej w modelu.

## Punkt odniesienia, poluzowania świadomie

Model referencyjny trzyma się fizyki tak blisko, jak pozwala gra na planszy. Jest punktem odniesienia: gra może go uprościć, ale świadomie – wiedząc, co traci.

Przykładem jest [model uproszczony](board_pl.md#model-uproszczony): koszt za każde pole ruchu zamiast śledzenia prędkości. Jest spójny sam w sobie, ale luzuje twardą science fiction, a [model](model_pl.md#model-uproszczony-koszt-za-pole) opisuje dokładnie, co przy tym przepada.

## Grywalność

Ostatecznie ma powstać coś prostego, w co da się przyjemnie grać. Fizyka jest zaokrąglona do liczb, z którymi da się grać: odległości i prędkości są dobrane tak, żeby pasowały do siatki, a długość rundy jest ich wynikiem, nie założeniem.

## Dokładność tam, gdzie wpływa na decyzje

Ziemia i Mars poruszają się na planszy zgodnie z rzeczywistością. Największe uproszczenia – wspólny pierścień Merkurego i Wenus oraz uproszczony albo pomijany dryf w pasie planetoid – dotyczą miejsc, w których dokładność nie wpływa na decyzje gracza.

Gdy wierność fizyce kłóci się z praktyką, wygrywa praktyka, a odstępstwo jest opisane. Tak jest z dryfem pasa planetoid (opcjonalnym i zaokrąglonym) i z pionkami (radiatory reaktora placówki zaznaczone tylko symbolicznie).

## Wygoda przy stole

Plansza ma być wygodna w użyciu bez specjalnego sprzętu: do wydrukowania w domu i do gry zwykłymi kośćmi.

### Kości do losowania

Do losowania pozycji w pasie planetoid służy para kości **k12 + k8** zamiast bardziej standardowych kombinacji. Decyzja wynika z dwóch praktycznych powodów.

Po pierwsze, k12 i k8 są łatwo rozróżnialne na pierwszy rzut oka – różnią się kształtem i rozmiarem. Nie trzeba rzucać nimi po kolei ani oznaczać kolorami: wyniki od razu wiadomo, który jest którym (k12 → sektor, k8 → heks w sektorze).

Po drugie, pas planetoid ma 90 heksów (pierścienie 4–6, łącznie `6×4 + 6×5 + 6×6 = 90`). Przy standardowej k6 losowanie z 90 pól wymagałoby trzech rzutów i nietrywialnego mapowania wyniku. Para k12 × k8 daje 96 kombinacji, co pokrywa 90 heksów z minimalną nadwyżką i prostym schematem: jeden rzut, dwa wyniki, jedna pozycja na planszy. Nadwyżka – 4 na k8 w sektorze nieparzystym – oznacza ponowny rzut, średnio raz na 16 losowań; w zamian każde pole ma tę samą szansę. Wynik k8 mówi też od razu, który to pierścień: 1–2, 3–5, 6–8.

### Druk na domowym sprzęcie

Planszę da się wydrukować na zwykłej drukarce – w częściach, na kartkach A4, z których składa się planszę w formacie A2.

### Dwie wersje kolorystyczne

Plansza ma dwie wersje kolorystyczne: ciemną, bardziej kosmiczną, i jasną, przyjazną drukarce – zużywa mniej tuszu. Ciemna jest też na czarnym tle, na którym przestrzeń nie kończy się na brzegu planszy.

## Walor edukacyjny

Mimo uproszczeń model przekazuje rzeczy, których popularne wizualizacje Układu Słonecznego w ogóle nie pokazują:

- Planety poruszają się z różnymi prędkościami – i różnica jest odczuwalna podczas gry.
- Transfer między orbitami wymaga planowania w czasie: trzeba przewidzieć, gdzie będzie cel w momencie przybycia.
- Pas planetoid jest szeroki, nie cienki.
- Układ inercjalny to nie jedyna możliwość opisu ruchu – wybór układu odniesienia ma konsekwencje.
- W kosmosie płaci się za zmianę prędkości, a nie za przebytą drogę.

Gracz bez wiedzy astronomicznej spotka model spójny i intuicyjny. Gracz z tą wiedzą rozpozna, że mechanika jest prawdziwa – tylko zaokrąglona do liczb, z którymi da się grać.

## Otwartość

Plansza, dokumentacja i pionki są na licencji CC BY 4.0, a skrypty na MIT. Jawne jest nie tylko to, jak plansza działa, ale też dlaczego: uzasadnienie każdej decyzji jest w dokumentacji, a liczby pochodzą ze [skryptów](../tools/README_pl.md), którymi każdy może je sprawdzić i przeliczyć dla zmienionej planszy.

## Gdzie co jest

- [Jak działa plansza](board_pl.md) – zasady, bez uzasadnień.
- [Model i decyzje projektowe](model_pl.md) – uzasadnienia: jak plansza ma się do fizyki.
- [Pomysły na gry](ideas_pl.md) – materiał do wykorzystania.
- Ten dokument – zasady, według których powstaje reszta.
