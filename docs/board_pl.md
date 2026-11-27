# Hayabusa – plansza do gier w wewnętrznym Układzie Słonecznym

*[English version](board.md)*

## Czym jest ta plansza

Plansza przedstawia wewnętrzny Układ Słoneczny – przestrzeń od Słońca do pasa planetoid. Zaprojektowana jest jako uniwersalna przestrzeń do gier twardej science fiction o tematyce eksploracji kosmosu: gracze poruszają się statkami między planetami, eksploatują zasoby pasa planetoid i mierzą się z wyzwaniami, jakie niesie ze sobą prawdziwa mechanika orbitalna. Fizyka jest prawdziwa, z przyszłości pochodzą tylko silniki statków.

Nazwa pochodzi od japońskiej sondy Hayabusa („sokół wędrowny”), która jako pierwsza przywiozła na Ziemię próbki planetoidy – z planetoidy Itokawa, w 2010 roku.

Plansza nie jest przypisana do konkretnej gry – stanowi gotową podstawę, na której można budować różne tytuły.

## Siatka i skala

Plansza opiera się na siatce heksagonalnej podzielonej na koncentryczne pierścienie wokół centralnie umieszczonego Słońca. Każdy kolejny pierścień jest oddalony od poprzedniego o **0,5 AU** (1 AU to średnia odległość Ziemi od Słońca – ok. 150 mln km).

Pierścień numer `x` zawiera dokładnie `6x` heksów.

### Wydruk

Planszę drukuje się na zwykłej drukarce, na kartkach A4, które skleja się w całość:

- **A2 z 4 kartek** (pliki `*_a2.pdf`) – format docelowy, w skali 1 : 2,5 bln (1 mm to ok. 2,5 mln km). Pole ma ok. 30 mm między bokami, a pionki 3D mieszczą się w jednym polu, jeśli mają najwyżej ok. 27 mm szerokości.
- **A3 z 2 kartek** (pliki `*_a3.pdf`) – w skali 1 : 3,2 bln. Pole ma ok. 23 mm, za mało dla pionków 3D, ale wystarczy dla płaskich żetonów.

Ziemia, Mars i Ceres obok planszy mają własną, wspólną skalę: 1 : 60 mln na A2, czyli 1 mm to 60 km (ok. 1 : 77 mln na A3). W tej skali Ziemia jest dwa razy większa od Marsa, a Ceres to mała kulka. Przerywane koła to niskie orbity: 400 km nad Ziemią (jak ISS) i nad Marsem, 385 km nad Ceres (najniższa orbita sondy Dawn). Obie skale są wypisane na planszy. [Pionki](../models/README_pl.md) mają jeszcze inną: statek długości 36 mm odpowiada prawdziwemu statkowi od ok. 70 m do blisko kilometra, czyli skali od ok. 1 : 2000 do ok. 1 : 30 000.

Kartki drukuje się w skali 100%, bez dopasowania do strony. Przy każdym łączeniu obie kartki przycina się wzdłuż przerywanych linii (odcina się margines), dosuwa brzegami i skleja taśmą od spodu. Łączenie działa wtedy jak zawias. Łączenia biegną między środkami pól, nigdy przez nie.

Plansza jest w dwóch wersjach kolorystycznych: ciemnej i jasnej (pliki `board-light…`), przyjaznej drukarce.

## Orbity planet

Cztery planety wewnętrznego Układu Słonecznego zajmują kolejne pierścienie:

| Planeta | Pierścień | Odległość od Słońca |
|---------|-----------|----------------------|
| Merkury i Wenus | 1 | ~0,5 AU |
| Ziemia | 2 | ~1 AU |
| Mars | 3 | ~1,5 AU |

Merkury i Wenus w tej skali leżą bardzo blisko siebie i zajmują wspólny pierścień. W grach opartych na planszy pełnią raczej rolę tła niż aktywnych lokacji.

## Pas planetoid

Pierścienie 4–6 (2–3 AU) to pas planetoid. Popularne wyobrażenia pasa jako cienkiego pierścienia wynikają z przekłamań proporcji na rysunkach popularnonaukowych – w rzeczywistości gęsta część pasa rozciąga się na setki milionów kilometrów. Jowisz w tej skali leżałby na pierścieniu ok. 10–11 (5,2 AU) – prawie dwukrotnie dalej niż krawędź planszy.

### Losowe rozmieszczenie obiektów

Heksy w pasie planetoid oznaczone są etykietami liczbowymi odpowiadającymi wynikom rzutu dwiema kośćmi: **k12** i **k8**. Kość k12 losuje sektor (12 sektorów wokół planszy), kość k8 – konkretny heks w sektorze. Mapowanie nie jest idealnie 1:1, stąd niektóre heksy obejmują kilka wyników (oznaczone np. `3-4`).

Ten mechanizm pozwala szybko umieszczać planetoidy, zasoby lub zdarzenia losowo, ale z zachowaniem rozkładu odpowiadającego prawdziwemu pasowi.

### Dryf (opcjonalnie)

Plansza obraca się razem z jedną orbitą w pasie, a pozostałe części pasa krążą trochę szybciej lub wolniej. Gra, która potrzebuje dłużej śledzić pozycję konkretnych planetoid, może to oddać:

- pierścień 4: 1 pole do przodu co 3 rundy,
- pierścień 5: 1 pole do tyłu co 3 rundy,
- pierścień 6: 1 pole do tyłu co rundę.

„Do przodu” oznacza zgodnie z kierunkiem ruchu planet. Pojedyncze znane ciała można śledzić osobno: Ceres leży na wewnętrznym skraju pierścienia 6 i przesuwa się o 2 pola do tyłu co 3 rundy.

Gra może też dryf pominąć – szczegóły w [model_pl.md](model_pl.md#dryf-w-grze--opcjonalnie).

## Układ odniesienia – jak działa ruch na planszy

To najważniejsza i najbardziej oryginalna cecha planszy.

Plansza **nie jest nieruchoma** – obraca się wokół Słońca. Dzięki temu obiekty w pasie planetoid stoją na planszy praktycznie nieruchomo, a planety bliżej Słońca – które w rzeczywistości krążą szybciej – poruszają się po planszy wyraźnie w jednym kierunku co rundę.

### Prędkości orbitalne

Jedna runda gry odpowiada ok. 87 dniom (nieco mniej niż ćwierć roku). Co rundę wszystkie obiekty na danym pierścieniu – planety, statki graczy, wszystko – przesuwają się o:

| Pierścień | Obwód (pól) | Planeta | Ruch po orbicie (pola/rundę) | Ruch kątowy |
|-----------|------------|---------|----------------------------|-------------|
| 1 | 6 | Merkury, Wenus | 3 pola | 180° |
| 2 | 12 | Ziemia | 2 pola | 60° |
| 3 | 18 | Mars | 1 pole | 20° |
| 4–6 | 24–36 | pas planetoid | 0 pól | 0° |

Ruch kątowy jest różny dla każdej orbity, bo pierścienie mają różny obwód. Ziemia przesuwa się o 2 pola na 12-polowym pierścieniu, co odpowiada 60° – czyli ⅙ pełnego obiegu na rundę. Mars przesuwa się o 1 pole na 18-polowym pierścieniu, czyli o zaledwie 20°.

Ruch odbywa się w tym samym kierunku dla wszystkich (zgodnie z rzeczywistym kierunkiem obiegu wokół Słońca). Merkury i Wenus nie są śledzone jako aktywne lokacje w grze.

## Ruch statków

Każdy statek ma dwa składniki ruchu:

**Ruch po orbicie** – wynikający z pierścienia, na którym statek się znajduje (patrz tabela powyżej). Dotyczy wszystkich obiektów bez wyjątku.

**Ruch własny** – napędzany silnikiem statku. Jego prędkość (1–2 pola na rundę) jest porównywalna z prędkościami orbitalnymi: mechaniki orbitalnej nie da się ignorować, ale aktywne manewrowanie pozwala ją wykorzystać lub jej przeciwdziałać.

### Runda i tura

- **Runda** to jednostka organizacyjna gry: w każdej rundzie każdy gracz wykonuje swój ruch. Odpowiada upływowi niecałych 3 miesięcy (ok. 87 dni). Raz na rundę każdy obiekt na pierścieniu przesuwa się po orbicie.
- **Tura** to kolej danego gracza – albo ogólnie strony w grze – w ramach rundy.

Przebieg rundy:

1. **Tura neutralna**, na początku rundy:
   - Ziemia i Mars przesuwają się po orbitach,
   - obiekty pasa planetoid przesuwają się zgodnie z dryfem (jeśli gra go śledzi),
   - rozstrzygają się zdarzenia rundy, na przykład pojawianie się i znikanie ciekawych miejsc w pasie.
2. **Tury graczy**, po kolei. W swojej turze gracz dla każdego swojego statku:
   1. wykonuje **ruch po orbicie** – statek przesuwa się razem z pierścieniem, na którym stoi; znacznik prędkości przesuwa się razem z nim i zachowuje położenie względem statku,
   2. wykonuje **ruch własny** – według modelu lotów (niżej).

Ruch po orbicie liczy się z pierścienia, na którym statek naprawdę stoi – po ruchu własnym mógłby być już na innym pierścieniu. Gracze w swoich turach widzą, gdzie w tej rundzie są planety.

Między turą neutralną a turą gracza jego statki przez chwilę „odstają” od reszty planszy. W grze bez bezpośredniego konfliktu to nie problem. W grach z konfliktem lepszy jest wariant, w którym ruch po orbicie wszystkich statków wykonuje się w turze neutralnej – wtedy położenia są zawsze spójne, kosztem przesuwania wszystkich statków naraz.

### Model referencyjny

W kosmosie płaci się za zmianę prędkości, a nie za przebytą drogę.

1. Statek ma prędkość własną: 0–2 pola na rundę w dowolnym kierunku. Najprościej zaznaczyć ją znacznikiem na polu, na które statek doleci w następnej turze, jak w klasycznym ruchu wektorowym.
2. W swojej turze statek może dwa razy zmienić prędkość, za każdym razem najwyżej o 1 pole w dowolnym kierunku: raz przed ruchem i raz po ruchu. Każde pole zmiany prędkości kosztuje 1 jednostkę paliwa.
3. Między tymi zmianami statek przesuwa się o swoją prędkość. Lot ze stałą prędkością nic nie kosztuje.
4. Prędkość ponad 2 pola na rundę jest zakazana przepisami.
5. Pierścień 1 jest zamknięty dla statków – blisko Słońca jest za gorąco, a pierścień przesuwa się o pół obiegu na rundę.

Przykłady:

- **Przeskok** o 1 pole: +1 przed ruchem, ruch, −1 po ruchu. Koszt 2.
- **Rozpędzanie**: z postoju +1 przed ruchem, ruch o 1, +1 po ruchu – w następnej turze statek leci z prędkością 2. Koszt 2.
- **Hamowanie**: z prędkości 2: −1 przed ruchem, ruch o 1, −1 po ruchu – statek zatrzymuje się po jednym polu. Koszt 2.

Zbiornik frachtowca mieści rzędu 20 jednostek. Linia lotu na planszy to schemat zaplanowanej trasy: początek, koniec, czas i koszt odpowiadają rzeczywistości, a prawdziwy tor jest zakrzywiony. Uzasadnienie: [model_pl.md](model_pl.md#dlaczego-model-referencyjny-ma-sens).

### Dokowanie i lądowanie

- Statek jest **zadokowany**, gdy ma prędkość 0 na polu celu – na początku tury, na końcu tury albo pomiędzy. **Postój w przelocie** to na przykład: zahamowanie przed ruchem (−1), dokowanie, przyspieszenie na koniec tury (+1).
- **Krótkie działania** – handel, przeładunek, wymiana pasażerów – statek wykonuje od razu po zadokowaniu, także w postoju w przelocie.
- **Długie działania** – wydobycie, awaryjne tankowanie – wymagają **pełnej rundy postoju**: w danej turze statek ma prędkość 0 i w ogóle jej nie zmienia. Rozpędzanie i hamowanie trwają – zmiana prędkości o 2 pola to praca silnika przez całą rundę.
- **Ziemia i Mars:** zadokowany statek stawia się na **polu stacji** planety, poza główną siatką planszy. Statek na polu stacji porusza się razem z planetą. Odlatując, na początku swojej tury wraca na pole planety – zamiast ruchu po orbicie – i dalej porusza się normalnie. Pole stacji rozwiązuje też problem tłoku przy planecie. Pola stacji są po prawej stronie planszy: Ziemia u góry (mieści się tylko jej część), Mars na dole. Statek na polu stacji stawia się przy planecie: na niej, na jej orbicie albo obok.
- **Ceres** też jest obok planszy, na dole po lewej. Czy służy do czegoś poza klimatem, decyduje gra.
- Silnik fuzyjny jest za słaby, żeby wystartować z powierzchni planety albo dużej planetoidy:
  - przy Ziemi i Marsie statek dokuje do stacji na orbicie, a na powierzchnię kursują lądowniki stacji,
  - na Ceres i Westę potrzebny jest lądownik – miejscowy albo własny, na wyposażeniu frachtowca (kosztem zasięgu lub ładunku),
  - na małych planetoidach, o średnicy do kilku km, frachtowiec ląduje bezpośrednio.

### Model uproszczony

Gry, które nie chcą śledzić prędkości statków, mogą płacić za każde pole ruchu własnego:

| Gdzie | Prędkość własna | Koszt |
|-------|-----------------|-------|
| pierścień 1 | zamknięty dla statków | – |
| pierścień 2 (Ziemia) | maks. 1 pole/rundę | 3 |
| pierścień 3 (Mars) | maks. 1 pole/rundę | 2 |
| pierścienie 4–6 (pas planetoid) | 1 albo 2 pola/rundę | 1 za 1 pole, 3 za 2 pola |

Ruch przez granicę pierścieni podlega limitowi i kosztowi pierścienia najbliższego Słońcu, którego ten ruch dotyka. Przebieg rundy, dokowanie i pola stacji działają tak samo, z tą różnicą, że statek dokuje, kończąc ruch na polu celu. Zbiornik frachtowca mieści wtedy rzędu 15 jednostek. Ten model jest spójny sam w sobie, ale odchodzi od fizyki – co dokładnie traci, opisuje [model_pl.md](model_pl.md#model-uproszczony-koszt-za-pole).

## Planowanie trasy – serce mechaniki

Zmiana orbity wymaga ruchu własnego w kierunku radialnym (bliżej lub dalej od Słońca). Ale sam dolot to tylko połowa problemu – cel też się porusza.

### Transfer Ziemia–Mars

W rzeczywistości najtańszy energetycznie lot na Marsa to tzw. **manewr Hohmanna**: zamiast lecieć wprost, statek wykonuje dwa krótkie impulsy silnikowe i przez większość drogi „spada” po elipsie bez zużycia paliwa. Lot trwa kilka miesięcy – w tym czasie Mars przebywa dalej po swojej orbicie. Żeby się spotkali, Mars musi być w momencie startu ok. 44° „przed” statkiem. To okno transferowe otwiera się tylko raz na ok. 26 miesięcy.

Tak właśnie działała misja **Perseverance**: łazik wystartował w lipcu 2020 roku, kiedy układ planet był odpowiedni, i wylądował na Marsie w lutym 2021 – po niecałych 7 miesiącach lotu. Gdyby rakieta nie wystartowała w tym oknie, kolejna szansa byłaby dopiero w 2022 roku.

Na planszy wygląda to analogicznie: statek lecący z pierścienia 2 na pierścień 3 potrzebuje czasu na zmianę orbity. Przez ten czas Mars przesuwa się po swojej orbicie – gracz musi zaplanować kurs tak, żeby znaleźć się na pierścieniu 3 dokładnie wtedy i tam, gdzie będzie Mars.

### Powrót z pasa planetoid

Lot w głąb pasa planetoid to dopiero połowa misji. Kiedy statek dotarł do celu, wydobył zasoby i jest gotowy do powrotu – Ziemia jest już zupełnie gdzie indziej. W czasie kilkunastu lub kilkudziesięciu rund spędzonych w pasie Ziemia przesunęła się po swojej orbicie o wiele pól. Lot powrotny też potrwa kilka rund, podczas których Ziemia nie stoi w miejscu.

Gracz, który skupi się wyłącznie na efektywnej eksploatacji w pasie i zapomni śledzić pozycję Ziemi, może stanąć przed trudnym wyborem: czekać na korzystniejsze okno powrotne (tracąc czas) albo lecieć szybciej (tracąc paliwo). To napięcie między sukcesem misji a sprawnym powrotem jest jednym z kluczowych dramatów rozgrywki.

W rzeczywistości problem jest identyczny – i jeszcze ostrzejszy. Sonda **Dawn** NASA odwiedziła kolejno planetoidę Westę (2011–2012) i planetę karłowatą Ceres (2015–2018). Jej zapas materiału pędnego zaplanowano na dotarcie do obu celów i zejście na niskie orbity badawcze – powrót na Ziemię nigdy nie był w planach. Misja zakończyła się w 2018 roku, gdy skończyła się hydrazyna do sterowania położeniem sondy, a Dawn została tam, gdzie była: na orbicie Ceres, na której pozostanie przez dziesiątki lat. Gracz, który wyda cały zapas paliwa na eksplorację pasa, może stanąć przed tym samym dylematem.

---

Jak ten model ma się do rzeczywistości i jakie decyzje projektowe za nim stoją: [model_pl.md](model_pl.md).
