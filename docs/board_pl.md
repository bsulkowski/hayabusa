# Synodic Board – plansza wewnętrznego Układu Słonecznego

*[English version](board.md)*

## Czym jest ta plansza

Plansza przedstawia wewnętrzny Układ Słoneczny – przestrzeń od Słońca do pasa planetoid. Zaprojektowana jest jako uniwersalna przestrzeń do gier twardej science fiction o tematyce eksploracji kosmosu: gracze poruszają się statkami między planetami, eksploatują zasoby pasa planetoid i mierzą się z wyzwaniami, jakie niesie ze sobą prawdziwa mechanika orbitalna. Fizyka jest prawdziwa, z przyszłości pochodzą tylko silniki statków.

Nazwa pochodzi od układu synodycznego – układu odniesienia, który obraca się razem z orbitującymi ciałami. Na takim układzie opiera się cała mechanika ruchu na planszy.

Plansza nie jest przypisana do konkretnej gry – stanowi gotową podstawę, na której można budować różne tytuły.

## Siatka i skala

Plansza opiera się na siatce heksagonalnej podzielonej na koncentryczne pierścienie wokół centralnie umieszczonego Słońca. Każdy kolejny pierścień jest oddalony od poprzedniego o **0,5 AU** (1 AU to średnia odległość Ziemi od Słońca – ok. 150 mln km).

Pierścień numer `x` zawiera dokładnie `6x` heksów.

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

- pierścień 4: 1 pole do przodu co 3 tury,
- pierścień 5: 1 pole do tyłu co 3 tury,
- pierścień 6: 1 pole do tyłu co turę.

Pojedyncze znane ciała można śledzić osobno: Ceres leży na wewnętrznym skraju pierścienia 6 i przesuwa się o 2 pola do tyłu co 3 tury.

„Do przodu" oznacza zgodnie z kierunkiem ruchu planet. Gra może też dryf pominąć – szczegóły w [model_pl.md](model_pl.md#dryf-w-grze--opcjonalnie).

## Układ odniesienia – jak działa ruch na planszy

To najważniejsza i najbardziej oryginalna cecha planszy.

Plansza **nie jest nieruchoma** – obraca się wokół Słońca. Dzięki temu obiekty w pasie planetoid stoją na planszy praktycznie nieruchomo, a planety bliżej Słońca – które w rzeczywistości krążą szybciej – poruszają się po planszy wyraźnie w jednym kierunku co turę.

### Prędkości orbitalne

Jedna runda gry odpowiada ok. 87 dniom (nieco mniej niż ćwierć roku). Co turę wszystkie obiekty na danym pierścieniu – planety, statki graczy, wszystko – przesuwają się o:

| Pierścień | Obwód (pól) | Planeta | Ruch po orbicie (pola/turę) | Ruch kątowy |
|-----------|------------|---------|----------------------------|-------------|
| 1 | 6 | Merkury, Wenus | 3 pola | 180° |
| 2 | 12 | Ziemia | 2 pola | 60° |
| 3 | 18 | Mars | 1 pole | 20° |
| 4–6 | 24–36 | pas planetoid | 0 pól | 0° |

Ruch kątowy jest różny dla każdej orbity, bo pierścienie mają różny obwód. Ziemia przesuwa się o 2 pola na 12-polowym pierścieniu, co odpowiada 60° – czyli ⅙ pełnego obiegu na turę. Mars przesuwa się o zaledwie 20°, bo jego pierścień jest większy.

Ruch odbywa się w tym samym kierunku dla wszystkich (zgodnie z rzeczywistym kierunkiem obiegu wokół Słońca). Merkury i Wenus nie są śledzone jako aktywne lokacje w grze.

## Ruch statków

Każdy statek ma dwa składniki ruchu, które działają łącznie:

**Ruch wymuszony** – wynikający z pierścienia, na którym statek się znajduje (patrz tabela powyżej). Dotyczy wszystkich obiektów bez wyjątku.

**Ruch własny** – napędzany silnikiem statku. Jego prędkość (1–2 pola na turę) jest porównywalna z prędkościami orbitalnymi: mechaniki orbitalnej nie da się ignorować, ale aktywne manewrowanie pozwala ją wykorzystać lub jej przeciwdziałać.

### Model referencyjny

W kosmosie płaci się za zmianę prędkości, a nie za przebytą drogę. Proponowany model lotów:

1. Statek ma prędkość własną: 0–2 pola na turę w dowolnym kierunku (znacznik na polu, na które doleci w następnej turze).
2. Na początku tury statek może zmienić prędkość najwyżej o 2 pola. Każde pole zmiany prędkości kosztuje 1 jednostkę paliwa.
3. Statek przesuwa się o swoją prędkość i razem z pierścieniem, na którym zaczął turę.
4. Przeskok: statek może przesunąć się o 1 pole i zatrzymać w tej samej turze (koszt 2).
5. Dokowanie, lądowanie i każda inna interakcja wymagają prędkości 0. Silnik fuzyjny jest za słaby, żeby wystartować z powierzchni planety albo dużej planetoidy:
   - przy Ziemi i Marsie statek dokuje do stacji na orbicie, a na powierzchnię kursują promy stacji,
   - na Ceres i Westę potrzebny jest prom – miejscowy albo własny, na wyposażeniu frachtowca (kosztem zasięgu lub ładunku),
   - na małych planetoidach, o średnicy do kilku km, frachtowiec ląduje bezpośrednio.
6. Prędkość ponad 2 pola na turę jest zakazana przepisami.
7. Pierścień 1 jest zamknięty dla statków – blisko Słońca jest za gorąco, a pierścień przesuwa się o pół obiegu na turę.

Zbiornik frachtowca mieści rzędu 20 jednostek. Linia lotu na planszy to schemat zaplanowanej trasy: początek, koniec, czas i koszt odpowiadają rzeczywistości, a prawdziwy tor jest zakrzywiony. Uzasadnienie: [model_pl.md](model_pl.md#model-referencyjny).

### Model uproszczony

Gry, które nie chcą śledzić prędkości statków, mogą płacić za każde pole ruchu własnego:

| Gdzie | Prędkość własna | Koszt |
|-------|-----------------|-------|
| pierścień 1 | zamknięty dla statków | – |
| pierścień 2 (Ziemia) | maks. 1 pole/turę | 3 |
| pierścień 3 (Mars) | maks. 1 pole/turę | 2 |
| pierścienie 4–6 (pas planetoid) | 1 albo 2 pola/turę | 1 za 1 pole, 3 za 2 pola |

Ruch przez granicę pierścieni podlega limitowi i kosztowi pierścienia najbliższego Słońcu, którego ten ruch dotyka. Zbiornik frachtowca mieści wtedy rzędu 15 jednostek. Ten model jest spójny sam w sobie, ale odchodzi od fizyki – co dokładnie traci, opisuje [model_pl.md](model_pl.md#model-uproszczony-koszt-za-pole).

## Planowanie trasy – serce mechaniki

Zmiana orbity wymaga ruchu własnego w kierunku radialnym (bliżej lub dalej od Słońca). Ale sam dolot to tylko połowa problemu – cel też się porusza.

### Transfer Ziemia–Mars

W rzeczywistości najtańszy energetycznie lot na Marsa to tzw. **manewr Hohmanna**: zamiast lecieć wprost, statek wykonuje dwa krótkie impulsy silnikowe i przez większość drogi "spada" po elipsie bez zużycia paliwa. Lot trwa kilka miesięcy – w tym czasie Mars przebywa dalej po swojej orbicie. Żeby się spotkali, Mars musi być w momencie startu ok. 44° "przed" statkiem. To okno transferowe otwiera się tylko raz na ok. 26 miesięcy.

Tak właśnie działała misja **Perseverance**: NASA wystartowała w lipcu 2020 roku, kiedy układ planet był odpowiedni, i łazik wylądował na Marsie w lutym 2021 – po dokładnie 7 miesiącach lotu. Gdyby rakieta nie wystartowała w tym oknie, kolejna szansa byłaby dopiero w 2022 roku.

Na planszy wygląda to analogicznie: statek lecący z pierścienia 2 na pierścień 3 potrzebuje czasu na zmianę orbity. Przez ten czas Mars przesuwa się po swojej orbicie – gracz musi zaplanować kurs tak, żeby znaleźć się na pierścieniu 3 dokładnie wtedy i tam, gdzie będzie Mars.

### Powrót z pasa planetoid

Lot w głąb pasa planetoid to dopiero połowa misji. Kiedy statek dotarł do celu, wydobył zasoby i jest gotowy do powrotu – Ziemia jest już zupełnie gdzie indziej. W czasie kilkunastu lub kilkudziesięciu rund spędzonych w pasie Ziemia przesunęła się po swojej orbicie o wiele pól. Lot powrotny też potrwa kilka rund, podczas których Ziemia nie stoi w miejscu.

Gracz, który skupi się wyłącznie na efektywnej eksploatacji w pasie i zapomni śledzić pozycję Ziemi, może stanąć przed trudnym wyborem: czekać na korzystniejsze okno powrotne (tracąc czas) albo lecieć na skos przez wiele pierścieni (tracąc paliwo). To napięcie między sukcesem misji a sprawnym powrotem jest jednym z kluczowych dramatów rozgrywki.

W rzeczywistości problem jest identyczny – i jeszcze ostrzejszy. Sonda **Dawn** NASA odwiedziła kolejno asteroidę Westę (2011–2012) i planetę karłowatą Ceres (2015–2018) w pasie planetoid, zużywając na manewry orbitalne niemal całe paliwo. Powrót na Ziemię nigdy nie wchodził w grę – całe paliwo zostało spalone na dotarcie do celu i zejście na niskie orbity badawcze. Dawn zakończyła misję w 2018 roku dokładnie tam gdzie była: na orbicie Ceres, gdzie pozostanie przez dziesiątki lat. Gracz, który wyda cały zapas paliwa na eksplorację pasa, może stanąć przed tym samym dylematem.

---

Jak ten model ma się do rzeczywistości i jakie decyzje projektowe za nim stoją: [model_pl.md](model_pl.md).
