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

### Dryf w grze – opcjonalnie

Dryf da się śledzić w prosty sposób, zaokrąglając go do pełnych pól:

| Pierścień | Dryf | Uproszczenie |
|-----------|------|--------------|
| 4 | +0,3 pola/turę | 1 pole do przodu co 3 tury |
| 5 | −0,3 pola/turę | 1 pole do tyłu co 3 tury |
| 6 | −0,9 pola/turę | 1 pole do tyłu co turę |

„Do przodu" oznacza zgodnie z kierunkiem ruchu planet. Sam rachunek jest prosty; kłopotem może być liczba obiektów do przesuwania – co trzecią turę wszystkie obiekty na pierścieniach 4 i 5, a co turę na pierścieniu 6.

Gra może więc dryf pominąć albo go realizować, zależnie od potrzeb:

- **Pominięcie** wystarcza, gdy obiekty w pasie pojawiają się losowo i nie trzeba długo śledzić ich dokładnej pozycji. Pas planetoid to miliony ciał na nieznacznie różnych orbitach, więc losowe rozmieszczenie rzutem kości oddaje go dobrze – dryf zostaje pochłonięty przez losowość.
- **Śledzenie** ma sens, gdy gra przez dłuższy czas potrzebuje dokładniej znać pozycję konkretnej planetoidy.

## Ruch statków a fizyka

Ruch statku na planszy składa się z ruchu wymuszonego (razem z pierścieniem) i ruchu własnego, napędzanego silnikiem. Plansza proponuje dwa modele lotów:

- **model referencyjny** – możliwie wierny fizyce, punkt odniesienia dla twardej science fiction,
- **model uproszczony** – prostszy w grze, kosztem kilku świadomych odstępstw od fizyki.

Każda gra może model lotów dalej rozluźniać. Ten rozdział pokazuje, co się wtedy traci.

### Ruch wymuszony to bezwładność

Statek bez napędu na danym pierścieniu leci po orbicie kołowej – czyli swobodnie, bez zużycia paliwa. Model ma więc bezwładność; jego naturalnym stanem nie jest stanie w miejscu, tylko krążenie po orbicie.

### W kosmosie płaci się za zmianę prędkości

W rzeczywistości paliwo zużywa się na zmianę prędkości: na zejście z orbity startowej i na wyrównanie z orbitą celu. Pomiędzy statek leci swobodnie, po łuku wyznaczonym przez grawitację. Długość trasy nie ma więc dużego znaczenia – liczy się, jak szybko trzeba się rozpędzić i ile potem wyhamować.

Jednostką na planszy jest prędkość 1 pola na turę – ok. **10 km/s** względem lokalnej orbity. To dużo: prędkość orbitalna w pasie planetoid wynosi ok. 20 km/s.

### Model referencyjny

1. Statek ma prędkość własną: 0–2 pola na turę w dowolnym kierunku. Najprościej zaznaczyć ją znacznikiem na polu, na które statek doleci w następnej turze, jak w klasycznym ruchu wektorowym.
2. Na początku tury statek może zmienić prędkość najwyżej o 2 pola. Każde pole zmiany prędkości kosztuje **1 jednostkę paliwa** (ok. 10 km/s).
3. Statek przesuwa się o swoją prędkość i razem z pierścieniem, na którym zaczął turę.
4. Przeskok: statek może przesunąć się o 1 pole i zatrzymać w tej samej turze (rozpędzenie i hamowanie, koszt 2).
5. Lądowanie, dokowanie i każda inna interakcja z planetą lub planetoidą wymagają prędkości 0.
6. Prędkość ponad 2 pola na turę jest zakazana przepisami – to ograniczenie umowne, nie fizyczne.
7. Pierścień 1 jest zamknięty dla statków.

### Dlaczego model referencyjny ma sens

Najtańsza zaplanowana trasa w tempie gry – ze startem i końcem na orbicie, po dowolnie zakrzywionym torze – kosztuje:

| Trasa | Δv | W modelu referencyjnym |
|-------|----|------------------------|
| pas planetoid, 1–4 pola do przodu z prędkością 1 | 19–21 km/s | 2 |
| pas planetoid, 1–2 pierścienie dalej z prędkością 1 | 20–21 km/s | 2 |
| Ziemia → pierścień 4 albo 5 z prędkością 1 | 20–21 km/s | 2 |
| przeskok o 1 pole przy Ziemi lub Marsie | 20–26 km/s | 2 |
| trasy z prędkością 2 | 40–48 km/s | 4 |

Model trafia z dokładnością ok. ±25% w całej planszy: koszt nie zależy od długości trasy ani od miejsca, tylko od rozpędzenia i hamowania – dokładnie tak, jak w modelu.

Prawdziwy statek nie leci jednak po prostej, tylko po łuku. **Linia lotu na planszy to schemat zaplanowanej trasy**: początek, koniec, czas i koszt są prawdziwe, położenie w trakcie lotu – umowne. Ma to znaczenie tylko wtedy, gdy gra pozwala coś robić ze statkiem w locie (na przykład go przechwycić). Zmiana planu w trakcie lotu też jest liczona tymi samymi zasadami – to uczciwe przybliżenie.

### Dlaczego nie prosta linia dosłownie

Gdyby traktować prostą linię dosłownie, jako lot swobodny, model rozjeżdżałby się z fizyką. Przy prędkościach z gry grawitacja zakrzywia tor bardzo mocno: w pasie planetoid 1 pole na turę do przodu (+10 km/s) wystarcza, żeby uciec z Układu Słonecznego, a 2 pola na turę do tyłu (−20 km/s) prawie zatrzymują statek względem Słońca, który zaczyna na nie spadać.

Błąd położenia statku lecącego swobodnie z prędkością 1 pola na turę, w porównaniu z prostą linią w grze (w polach):

| Gdzie | po 1 turze | po 2 turach | po 3 turach |
|-------|-----------|-------------|-------------|
| przy Ziemi | 1,1–1,9 | 2–6 | 2–8 |
| przy Marsie | 0,7–1,0 | 1,6–4 | 2–8 |
| pas planetoid (2,24 AU) | 0,3–0,6 | 1,0–2,3 | 1,6–5 |
| pas planetoid (3 AU) | 0,2–0,4 | 0,7–1,5 | 1,1–3,4 |

Główny mechanizm jest jednym z najbardziej nieintuicyjnych zjawisk mechaniki orbitalnej: rozpędzenie do przodu wzdłuż orbity podnosi orbitę. Statek lecący w pasie do przodu po 3 turach jest ok. 3 pierścienie dalej od Słońca i wcale nie przesunął się do przodu.

Prosty kurs da się utrzymać ciągiem, ale koszt mocno zależy od kierunku. Koszt na turę przy prędkości 1 pola na turę:

| Gdzie | do przodu | do tyłu | na zewnątrz | do środka |
|-------|-----------|---------|-------------|-----------|
| przy Ziemi | 3,5 | 2,5 | 0,5 | – |
| przy Marsie | 2,0 | 1,3 | 0,3 | 0,5 |
| pas planetoid | 1,1 | 0,7 | 0,2 | 0,3 |

Lot od Słońca i do Słońca jest prawie darmowy, lot wzdłuż orbity – drogi. Sprawdzono też prostą zasadę zakrzywiania toru (prędkość do przodu zamienia się w prędkość na zewnątrz: w pasie 1, przy Marsie 2, przy Ziemi 3 pola na turę). Poprawia ona lot do przodu, ale psuje lot do tyłu – nie jest warta dodatkowej zasady. Ujęcie linii lotu jako schematu zaplanowanej trasy jest prostsze i daje poprawne koszty.

### Okna transferowe

**Częstotliwość okien jest dokładna.** Planety poruszają się na planszy zgodnie z rzeczywistością, więc korzystne ustawienia powtarzają się co tyle samo tur co w rzeczywistości: Ziemia–Mars co 9 tur (ok. 26 miesięcy), Ziemia–pas planetoid co 6 tur, Mars–pas planetoid co 18 tur.

**Ustawienie planet w chwili startu zależy od tempa lotu.** W modelu referencyjnym statki naprawdę lecą w tempie gry, więc ustawienia startowe na planszy są prawdziwe dla takich lotów. Różnią się od ustawień dla najtańszych, powolnych tras (transfer Hohmanna). Tabela pokazuje, o ile stopni cel musi wyprzedzać statek w chwili startu (minus – cel jest z tyłu):

| Trasa | W tempie gry | Najtańsza trasa | Różnica |
|-------|--------------|-----------------|---------|
| Ziemia → Mars | +39° | +43° | −4° |
| Ziemia → pierścień 4 | +72° | +63° | +8° |
| Mars → pierścień 4 | +16° | +33° | −16° |
| Mars → Ziemia | −39° | −72° | +33° |
| pierścień 4 → Ziemia | −94° | −151° | +57° |
| pierścień 5 → Ziemia | −158° | +123° | +79° |

Lot Ziemia → Mars w tempie gry wymaga niemal tego samego ustawienia co najtańsza trasa. Przy powrotach do Ziemi różnica jest duża: na najtańszej trasie statek okrąża pół Słońca, a w czasie długiego lotu szybka Ziemia przesuwa się dużo dalej. W modelu uproszczonym (niżej), który zakłada najtańsze trasy w skróconym czasie, kąty startu są więc tylko przybliżone.

W obu modelach gracz uczy się prawdziwej zasady: trzeba celować tam, gdzie cel będzie, i czekać na okno.

### Pierścień 1 – strefa zamknięta

Domyślnie statki nie wlatują na pierścień 1. Przemawiają za tym trzy powody:

- **Ciepło** – strumień promieniowania słonecznego jest tam cztery razy większy niż przy Ziemi, a przy Merkurym prawie siedem razy.
- **Sterowanie** – pierścień przesuwa się o pół obiegu na turę, a grawitacja zakrzywia tor jeszcze mocniej niż przy Ziemi. Statek o prędkości własnej 1–2 pola na turę praktycznie traci kontrolę nad tym, gdzie się znajdzie.
- **Koszt oszczędnych tras** – są tam 8–11 razy droższe niż w pasie planetoid. W rzeczywistości misje do Merkurego trwają latami i wymagają wielu przelotów obok planet: sonda MESSENGER wystartowała w 2004 roku, a na orbitę Merkurego weszła dopiero w 2011, po sześciu takich przelotach.

Zasada pasuje do roli Merkurego i Wenus jako tła. Gra, która chce tam latać, może ją zdjąć.

### Napęd i paliwo

Model referencyjny wymaga **napędu fuzyjnego**: przy jednostce 10 km/s inne napędy nie unoszą wystarczająco dużo paliwa.

**Ciąg.** Zmiana prędkości o 2 pola w ciągu tury to ok. 20 km/s w 87 dni – stałe przyspieszenie ok. 0,27 milli-g. Przy prędkości wylotu ok. 300 km/s wymaga to mocy rzędu 0,7 MW na tonę statku. To odległa przyszłość, ale fizyka pozostaje uczciwa: przyspieszenia są rzędu milli-g, a nie całego g, jak w mniej powściągliwej fantastyce naukowej.

**Zbiornik.** Zmiana prędkości, jaką da pełny zbiornik, zależy tylko od prędkości wylotu i od stosunku masy statku z paliwem do masy bez paliwa – nie od wielkości statku. Dla frachtowca liczy się przy tym ładunek, bo wchodzi do masy. Przykład: konstrukcja o masie 1, ładunek 1 (albo 2), pełny zbiornik o masie 2, prędkość wylotu ok. 300 km/s:

| Stan frachtowca | Stosunek mas | Δv | Jednostki w grze |
|-----------------|--------------|----|------------------|
| pusty | 3 | ok. 330 km/s | ok. 33 |
| z ładunkiem | 2 | ok. 210 km/s | ok. 21 |
| mocno obciążony | 1,7 | ok. 155 km/s | ok. 15 |

Na potrzeby gry wystarczy jedna wartość: **zbiornik rzędu 20 jednostek**. Przeskok kosztuje 2, a cała trasa z rozpędzeniem, poprawkami i hamowaniem ok. 3–6, więc paliwo realnie ogranicza – statki muszą tankować. Gra, która chce oddać wpływ ładunku, może pozwolić pustemu statkowi lecieć dalej – ok. 1,5 raza. Lżejsze statki pasażerskie mają większy stosunek mas, więc i większy zasięg.

Inne napędy nie wystarczają. Napęd jądrowo-elektryczny (prędkość wylotu ok. 40 km/s) dałby zbiornik na ok. 3 jednostki, jądrowy termiczny (ok. 9 km/s) – na mniej niż 1.

Rzeczywistą możliwością jest tankowanie w pasie planetoid: materiał pędny, na przykład wodę, można pozyskiwać z samych planetoid.

### Manewry w pasie planetoid

Pas planetoid jest bardzo pusty – średnia odległość między planetoidami to ok. miliona km, a sondy przelatują przez niego bez żadnych manewrów. Ominięcie przeszkód nie jest więc tym, co kosztuje. Kosztuje dopasowanie się do celu: żeby wylądować na konkretnej planetoidzie, trzeba wejść na jej orbitę, a każda planetoida ma własną. To zarazem rzeczywisty odpowiednik dryfu – gdy gra go pomija, jego koszt zawiera się w koszcie manewrów.

### Model uproszczony: koszt za pole

Model uproszczony nie śledzi prędkości statku – płaci się za każde pole ruchu własnego:

| Gdzie | Prędkość własna | Koszt |
|-------|-----------------|-------|
| pierścień 1 | zamknięty dla statków | – |
| pierścień 2 (Ziemia) | maks. 1 pole/turę | 3 |
| pierścień 3 (Mars) | maks. 1 pole/turę | 2 |
| pierścienie 4–6 (pas planetoid) | 1 albo 2 pola/turę | 1 za 1 pole, 3 za 2 pola |

Ruch przez granicę pierścieni podlega limitowi i kosztowi pierścienia najbliższego Słońcu, którego ten ruch dotyka.

**Interpretacja.** Model uproszczony odpowiada frachtowcom latającym najtańszymi trasami (transfer Hohmanna) z czasem przelotu skróconym dla grywalności. Jedna jednostka to wtedy ok. 1,8 km/s, a wystarcza napęd jądrowo-elektryczny (prędkość wylotu ok. 40 km/s) – zbiornik frachtowca z ładunkiem mieści ok. 15 jednostek.

**Skąd mnożniki.** Najtańsze trasy są tym droższe, im bliżej Słońca – koszt maleje mniej więcej jak odległość do potęgi 1,5:

| Pierścień | Przejście na pierścień dalej (najtańsza trasa) | Strumień ciepła ze Słońca |
|-----------|------------------------------------------------|---------------------------|
| 1 (0,5 AU) | 7,5× | 4× ziemskiego |
| 2 (Ziemia) | 3,3× | 1× |
| 3 (Mars) | 2× | 0,4× |
| 4 | 1,4× | 0,25× |
| 5 | 1 | 0,16× |

Mnożnik ×3 na pierścieniu 2, ×2 na pierścieniu 3 i ×1 w pasie planetoid dobrze to oddaje.

**Kalibracja.** Koszt w grze (z zasadą najbliższego pierścienia) i najtańsza trasa:

| z \ do | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| **2** (Ziemia) | – | 3 | 5 | 6 | 7 |
| **3** (Mars) | 3 | – | 2 | 3 | 4 |
| **4** | 5 | 2 | – | 1 | 2 |
| **5** | 6 | 3 | 1 | – | 1 |
| **6** | 7 | 4 | 2 | 1 | – |

| z \ do | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| **2** | 5,4 km/s (1,80) | 8,5 km/s (1,69) | 10,4 km/s (1,74) | 11,7 km/s (1,68) |
| **3** | | 3,2 km/s (1,62) | 5,4 km/s (1,80) | 6,9 km/s (1,73) |
| **4** | | | 2,2 km/s (2,22) | 3,8 km/s (1,91) |
| **5** | | | | 1,6 km/s (1,64) |

W nawiasach – km/s na jednostkę kosztu w grze. Wszystkie pary mieszczą się w 1,6–2,2 km/s na jednostkę, więc tabela kosztów jest spójna z najtańszymi trasami.

**Limity prędkości** wynikają z założenia, że w jednej turze statek może zużyć najwyżej ok. 3 jednostki: przy Ziemi to 1 pole, przy Marsie też 1 (2 pola kosztowałyby 4), w pasie 2 pola. **Kara za prędkość** (2 pola za 3) to dopłata za pośpiech. **Zasada najbliższego pierścienia** sprawia, że lot tam i z powrotem kosztuje tyle samo, tak jak w rzeczywistości.

**Co model uproszczony traci:**

- **Płaci się za drogę, a nie za zmianę prędkości.** Długie przeloty kosztują kilka razy za dużo: trasa o 4 pola kosztuje fizycznie tyle co o 1 pole, a w modelu 4 razy więcej. Kara za prędkość jest za to za mała – fizycznie dwa razy szybszy lot kosztuje dwa razy więcej.
- **Czas jest skrócony nierówno.** Najtańsza trasa Ziemia → Mars trwa ok. 3 tury, a między sąsiednimi pierścieniami pasa 7–10 tur; w grze każda trwa turę. Gra skraca więc czas w pasie kilka razy bardziej niż przy Ziemi – i stąd biorą się mnożniki. Przy jednakowym tempie koszt praktycznie nie zależy od pierścienia:

| Czas lotu (tury) | 1 | 2 | 3 | Najtańsza trasa |
|------------------|---|---|---|-----------------|
| 2 → 3 (Ziemia → Mars) | 19 km/s | 7,9 km/s | 5,4 km/s | 5,4 km/s w 2,9 tury |
| 3 → 4 | 20 km/s | 9,1 km/s | 5,5 km/s | 3,2 km/s w 4,9 tury |
| 4 → 5 | 20 km/s | 9,6 km/s | 6,0 km/s | 2,2 km/s w 7,1 tury |
| 5 → 6 | 20 km/s | 9,8 km/s | 6,3 km/s | 1,6 km/s w 9,6 tury |

- **Kąty startu w oknach transferowych są przybliżone** (patrz „Okna transferowe”).

Model uproszczony jest spójny sam w sobie i dobrze nadaje się do gier, które nie chcą śledzić prędkości statków. Dalsze uproszczenia – na przykład stały koszt za pole na całej planszy – są możliwe, ale oddalają model od fizyki jeszcze bardziej.

**Geometria planszy.** W żadnym z modeli kosztów nie uwzględniono w samej planszy – na przykład przez pola tym mniejsze, im bliżej Słońca. Plansza pokazywałaby wtedy koszt zamiast przestrzeni i straciłaby to, co jest jej główną wartością: prawdziwe odległości i proporcje ruchu orbitalnego. Mapy zbudowane z kosztów manewrów istnieją (taką ma na przykład gra High Frontier), ale tracą wyczucie, gdzie co naprawdę leży.

Wszystkie liczby w tym rozdziale pochodzą ze skryptów w folderze [tools](../tools/README.md) – każdy może je sprawdzić i przeliczyć dla zmienionej planszy.

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
- W kosmosie płaci się za zmianę prędkości, a nie za przebytą drogę.

Ziemia i Mars poruszają się na planszy zgodnie z rzeczywistością. Największe uproszczenia – wspólny pierścień Merkurego i Wenus oraz uproszczony albo pomijany dryf w pasie – dotyczą miejsc, w których dokładność nie wpływa na decyzje gracza. Gracz bez wiedzy astronomicznej spotka model spójny i intuicyjny. Gracz z tą wiedzą rozpozna, że mechanika jest prawdziwa – tylko zaokrąglona do liczb, z którymi da się grać.
