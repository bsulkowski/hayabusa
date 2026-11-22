# Synodic Board – model i decyzje projektowe

## Dla kogo jest ten dokument

Ten dokument jest przeznaczony dla osób zainteresowanych tym, jak plansza ma się do rzeczywistej fizyki Układu Słonecznego: co zostało zamodelowane wiernie, co uproszczono i dlaczego. Może być przydatny zarówno dla projektantów gier chcących zmodyfikować planszę lub zainspirować się przy tworzeniu własnej, jak i dla graczy ciekawych astronomicznego kontekstu.

## Skala odległości

Skok siatki 0,5 AU na pierścień daje bardzo dobre przybliżenie dla planet aktywnie obecnych w grze:

| Obiekt | Rzeczywistość | Model | Błąd |
|--------|--------------|-------|------|
| Ziemia | 1,00 AU | pierścień 2 (1,0 AU) | 0% |
| Mars | 1,52 AU | pierścień 3 (1,5 AU) | −2% |

### Pas planetoid

Pierścień to nie linia, tylko pas o szerokości jednego pola – od −0,25 do +0,25 AU wokół swojej odległości nominalnej. Pierścienie 4–6 obejmują więc obszar **1,75–3,25 AU**.

Główny pas planetoid leży między dwiema lukami Kirkwooda – pustymi pasmami wyczyszczonymi przez rezonanse z Jowiszem: 4:1 (2,06 AU) i 2:1 (3,27 AU). Zewnętrzna krawędź pasa na planszy zgadza się z nim praktycznie idealnie. Wewnętrzna sięga ok. 0,3 AU bliżej Słońca, ale ten obszar (1,78–2,0 AU) zajmuje grupa Hungaria – najbardziej wewnętrzne gęste skupisko planetoid w Układzie Słonecznym.

Ceres (2,77 AU) wypada na granicy pierścieni 5 i 6.

### Merkury i Wenus

Merkury leży realnie przy 0,39 AU, Wenus przy 0,72 AU. W modelu obie planety trafiają do pierścienia 1 (0,5 AU) – żadna nie wychodzi dobrze. To świadoma decyzja: obie planety są w grach tłem, a nie aktywnymi lokacjami, więc dokładność ich położenia nie ma znaczenia dla rozgrywki.

## Układ odniesienia i prędkości orbitalne

### Skąd pochodzi ruch o 3/2/1/0 pól na turę

Projektując prędkości orbitalne, szukano liczb całkowitych, które najlepiej oddają proporcje rzeczywistych prędkości kątowych. Prędkości kątowe Ziemi, Marsa i pasa planetoid są w przybliżeniu w proporcji **4 : 2 : 1**.

Plansza obraca się w kierunku obiegu planet z prędkością odpowiadającą tej jednostce „1". Po odjęciu obrotu planszy widoczne prędkości wynoszą **3 : 1 : 0** – dokładnie to, co widzimy w tabeli ruchów. Taki obracający się układ odniesienia nazywa się w astrodynamice układem synodycznym – stąd nazwa planszy. Na planszy Ziemia przesuwa się co turę o 60° (2 pola na 12-polowym pierścieniu), a Mars o 20° (1 pole na 18-polowym).

### Punkt odniesienia i skala czasu

Proporcja 4:2:1 jest tylko punktem wyjścia – rzeczywisty stosunek prędkości kątowych Ziemi i Marsa to 1,88, a nie 2. Mimo to proporcja **3:1 na planszy może być dokładna**: wystarczy dobrać prędkość obrotu planszy tak, żeby po jej odjęciu Ziemia poruszała się dokładnie trzy razy szybciej niż Mars.

Z tego warunku wynikają dwie wartości:

- plansza jest zsynchronizowana z orbitą o promieniu **2,24 AU** i okresie obiegu **3,36 roku** – w wewnętrznej części pasa planetoid, bliżej Słońca niż Ceres,
- jedna runda trwa ok. **87 dni** (nieco poniżej ćwierć roku).

Dzięki temu Ziemia i Mars poruszają się na planszy zgodnie z rzeczywistością – z dokładnością ograniczoną tylko zaokrągleniem długości rundy. Ani punkt synchronizacji, ani długość rundy nie były zakładane z góry; oba są wynikiem dopasowania. Ceną jest to, że plansza obraca się razem z wewnętrzną częścią pasa, a nie z jego środkiem – dalsze części pasa dryfują (patrz niżej).

Synchronizacja z Ceres dałaby rundę bliższą równej ćwiartce roku, ale proporcja Ziemia:Mars na planszy wynosiłaby wtedy ok. 2,5:1 zamiast 3:1. Wartość ¼ roku jest wygodna komunikacyjnie, ale lekko zawyża rzeczywisty czas rundy.

### Pierścień 1

Zgodnie z prawem Keplera orbita kołowa w odległości 0,5 AU przesuwałaby się na planszy o ok. 3,6 pola na turę – model zaokrągla to do 3. Rzeczywiste planety tego pierścienia rozjeżdżają się w obie strony: Wenus przesuwałaby się o ok. 1,9 pola na turę, Merkury o ok. 5,5. Jeden pierścień z jedną prędkością nie może oddać obu – co nie przeszkadza, skoro obie planety są tłem.

## Pas planetoid – dryf i losowość

### Nieuniknione uproszczenie

Pas planetoid nie jest tarczą obracającą się ze stałą prędkością – każda planetoida krąży z własną prędkością wynikającą z jej orbity. Obiekty bliżej Słońca krążą szybciej, obiekty dalej – wolniej. Plansza jest zsynchronizowana tylko z jedną orbitą (2,24 AU), więc obiekty na pozostałych pierścieniach pasa dryfowałyby względem planszy:

| Pierścień | Odległość | Dryf względem planszy |
|-----------|-----------|----------------------|
| 4 | 2,0 AU | +0,3 pola/turę (do przodu) |
| – | 2,24 AU (synchronizacja) | 0 |
| 5 | 2,5 AU | −0,3 pola/turę (do tyłu) |
| 6 | 3,0 AU | −0,9 pola/turę (do tyłu) |

Ceres dryfowałaby o ok. −0,6 pola/turę. W trakcie typowej gry (30–50 rund) przesunęłaby się o kilkanaście do kilkudziesięciu pól, a obiekty na zewnętrznym pierścieniu jeszcze więcej.

### Dlaczego to nie jest problem

Modelowanie dryfowania poszczególnych obiektów wymagałoby śledzenia ułamkowych przesunięć, co znacząco skomplikowałoby rozgrywkę bez żadnej korzyści dla jakości decyzji gracza. Co ważniejsze – pas planetoid w rzeczywistości nie jest zbiorem obiektów, które dałoby się sensownie śledzić na planszy. To miliony ciał na nieznacznie różnych orbitach.

Losowe rozmieszczenie zasobów rzutem kości jest bliższe prawdzie niż jakikolwiek deterministyczny ruch mógłby oddać. Dryf jest świadomie pochłonięty przez losowość mechaniki pasa.

## Ruch statków a fizyka

Ruch statku na planszy składa się z ruchu wymuszonego (razem z pierścieniem) i ruchu własnego (1–2 pola na turę w dowolnym kierunku, zużywającego paliwo). Na pierwszy rzut oka wygląda to jak uproszczenie wbrew fizyce – w kosmosie nie ma tarcia, więc raz rozpędzony statek powinien lecieć dalej za darmo. W rzeczywistości ten model da się dobrze obronić.

### Ruch wymuszony to bezwładność

Statek bez napędu na danym pierścieniu leci po orbicie kołowej – czyli swobodnie, bez zużycia paliwa. Model ma więc bezwładność; jego naturalnym stanem nie jest stanie w miejscu, tylko krążenie po orbicie.

### Ruch własny kosztuje stale

Każdy ruch własny oznacza lot kursem innym niż orbita kołowa. Taki tor nie jest balistyczny: grawitacja Słońca stale go zakrzywia (względem lokalnej orbity objawia się to jako siła Coriolisa i siły pływowe). Żeby utrzymać kurs z określoną prędkością względem lokalnej orbity, trzeba więc stale pracować silnikiem – i to tym mocniej, im szybciej statek leci.

Nie ma przy tym znaczenia, czy statek kończy trasę, czy leci dalej: koszt wynika z samego utrzymania kursu, a nie z hamowania i ponownego rozpędzania.

Rzędy wielkości (1 pole na turę to ok. 10 km/s):

| Gdzie | Zmiana prędkości (Δv) potrzebna na turę lotu z prędkością 1 pola/turę |
|-------|------------------------------------------------------------------------|
| orbita Ziemi | ok. 30 km/s |
| orbita Marsa | ok. 16 km/s |
| pas planetoid | ok. 6–9 km/s |

To szacunki – przybliżenie, z którego wynikają, jest dokładne tylko dla przesunięć małych w porównaniu z promieniem orbity, a 0,5 AU małe nie jest. Pokazują jednak dwie rzeczy: szybszy lot kosztuje proporcjonalnie więcej paliwa na turę, a manewrowanie bliżej Słońca jest droższe niż w pasie.

### Koszt a odległość od Słońca

Koszt manewrów maleje z odległością od Słońca mniej więcej jak odległość do potęgi 1,5. Dwa niezależne sposoby liczenia – utrzymanie kursu i przejście po spirali na sąsiedni pierścień (różnica prędkości orbitalnych) – dają podobny obraz:

| Pierścień | Utrzymanie kursu | Przejście na pierścień dalej | Strumień ciepła ze Słońca |
|-----------|------------------|------------------------------|---------------------------|
| 1 (0,5 AU) | 11× | 7,5× | 4× ziemskiego |
| 2 (Ziemia) | 4× | 3,3× | 1× |
| 3 (Mars) | 2,2× | 2× | 0,4× |
| 4 | 1,4× | 1,4× | 0,25× |
| 5 | 1 | 1 | 0,16× |
| 6 | 0,8× | – | 0,1× |

Koszty są względne (pierścień 5 = 1). Różnica między Ziemią a pasem planetoid – 3–4 razy – jest na tyle duża, że przy stałym koszcie ruchu manewrowanie w okolicach Ziemi wychodzi wyraźnie za tanio. Prosty mnożnik kosztu ruchu własnego dobrze oddaje oba wyliczenia: **×3 na pierścieniu 2, ×2 na pierścieniu 3, ×1 w pasie planetoid**. Czy go użyć, decyduje konkretna gra.

Kosztów nie uwzględniono w geometrii planszy – na przykład przez pola tym mniejsze, im bliżej Słońca. Plansza pokazywałaby wtedy koszt zamiast przestrzeni i straciłaby to, co jest jej główną wartością: prawdziwe odległości i proporcje ruchu orbitalnego. Mapy zbudowane z kosztów manewrów istnieją (taką ma na przykład gra High Frontier), ale tracą wyczucie, gdzie co naprawdę leży.

### Pierścień 1 – strefa zamknięta

Domyślnie statki nie wlatują na pierścień 1. Przemawiają za tym trzy powody:

- **Koszt** – manewry są tam 8–11 razy droższe niż w pasie planetoid. W rzeczywistości misje do Merkurego trwają latami i wymagają wielu przelotów obok planet: sonda MESSENGER wystartowała w 2004 roku, a na orbitę Merkurego weszła dopiero w 2011, po sześciu takich przelotach.
- **Ciepło** – strumień promieniowania słonecznego jest tam cztery razy większy niż przy Ziemi, a przy Merkurym prawie siedem razy.
- **Sterowanie** – pierścień przesuwa się o pół obiegu na turę. Statek o prędkości własnej 1–2 pola na turę praktycznie traci kontrolę nad tym, gdzie się znajdzie.

Zasada pasuje do roli Merkurego i Wenus jako tła. Gra, która chce tam latać, może ją zdjąć.

### Co pomijamy: lot balistyczny

Współczesne sondy na trasie Ziemia–Mars korzystają zwykle z transferu Hohmanna: dwa krótkie impulsy silnika, a pomiędzy nimi kilka miesięcy lotu po elipsie bez zużycia paliwa. Takiego „darmowego” lotu model nie przewiduje.

Statki w grze odpowiadają innemu rodzajowi napędu – o małym ciągu, ale pracującym bez przerwy. Tak latała sonda Dawn: jej silniki jonowe pracowały łącznie prawie 6 lat, prowadząc ją po spirali między orbitami. Dla bliskich orbit taka spirala kosztuje niemal tyle samo co transfer Hohmanna: z orbity Ziemi na orbitę Marsa ok. 5,7 km/s zamiast 5,6 km/s, do pasa planetoid (2,24 AU) ok. 9,9 km/s zamiast 9,5 km/s.

### Skala napędu

Utrzymanie kursu z prędkością 1 pola na turę wymaga ciągłego przyspieszenia rzędu 0,1–0,4 tysięcznej części przyspieszenia ziemskiego (milli-g) – kilkanaście do kilkudziesięciu razy więcej, niż dawały silniki Dawn. W grze na kilkadziesiąt rund statki potrzebowałyby łącznie setek km/s zmiany prędkości, podczas gdy Dawn przez całą misję uzyskała ok. 11,5 km/s.

To napęd z przyszłości – jądrowy lub fuzyjny o dużej mocy. Fizyka pozostaje jednak uczciwa: przyspieszenia są rzędu milli-g, a nie całego g, jak w mniej powściągliwej fantastyce naukowej.

### Manewry w pasie planetoid

Pas planetoid jest bardzo pusty – średnia odległość między planetoidami to ok. miliona km, a sondy przelatują przez niego bez żadnych manewrów. Ominięcie przeszkód nie jest więc tym, co kosztuje. Kosztuje dopasowanie się do celu: żeby wylądować na konkretnej planetoidzie, trzeba wejść na jej orbitę, a każda planetoida ma własną. To zarazem rzeczywisty odpowiednik pomijanego dryfu – jego koszt zawiera się w koszcie manewrów.

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

Ziemia i Mars poruszają się na planszy zgodnie z rzeczywistością. Największe uproszczenia – wspólny pierścień Merkurego i Wenus oraz pomijany dryf w pasie – dotyczą miejsc, w których dokładność nie wpływa na decyzje gracza. Gracz bez wiedzy astronomicznej spotka model spójny i intuicyjny. Gracz z tą wiedzą rozpozna, że mechanika jest prawdziwa – tylko zaokrąglona do liczb, z którymi da się grać.
