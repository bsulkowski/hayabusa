# Synodic Board – model i decyzje projektowe

*[English version](model.md)*

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

### Skąd pochodzi ruch o 3/2/1/0 pól na rundę

Projektując prędkości orbitalne, szukano liczb całkowitych, które najlepiej oddają proporcje rzeczywistych prędkości kątowych. Prędkości kątowe Ziemi, Marsa i pasa planetoid są w przybliżeniu w proporcji **4 : 2 : 1**.

Plansza obraca się w kierunku obiegu planet z prędkością odpowiadającą tej jednostce „1”. Po odjęciu obrotu planszy widoczne prędkości wynoszą **3 : 1 : 0** – dokładnie to, co widzimy w tabeli ruchów. Taki obracający się układ odniesienia nazywa się w astrodynamice układem synodycznym – stąd nazwa planszy. Na planszy Ziemia przesuwa się co rundę o 60° (2 pola na 12-polowym pierścieniu), a Mars o 20° (1 pole na 18-polowym).

### Punkt odniesienia i skala czasu

Proporcja 4:2:1 jest tylko punktem wyjścia – rzeczywisty stosunek prędkości kątowych Ziemi i Marsa to 1,88, a nie 2. Mimo to proporcja **3:1 na planszy może być dokładna**: wystarczy dobrać prędkość obrotu planszy tak, żeby po jej odjęciu Ziemia poruszała się dokładnie trzy razy szybciej niż Mars.

Z tego warunku wynikają dwie wartości:

- plansza jest zsynchronizowana z orbitą o promieniu **2,24 AU** i okresie obiegu **3,36 roku** – w wewnętrznej części pasa planetoid, bliżej Słońca niż Ceres,
- jedna runda trwa ok. **87 dni** (nieco poniżej ćwierć roku).

Dzięki temu Ziemia i Mars poruszają się na planszy zgodnie z rzeczywistością – z dokładnością ograniczoną tylko zaokrągleniem długości rundy. Ani punkt synchronizacji, ani długość rundy nie były zakładane z góry; oba są wynikiem dopasowania. Ceną jest to, że plansza obraca się razem z wewnętrzną częścią pasa, a nie z jego środkiem – dalsze części pasa dryfują (patrz niżej).

Synchronizacja z Ceres dałaby rundę bliższą równej ćwiartce roku, ale proporcja Ziemia:Mars na planszy wynosiłaby wtedy ok. 2,5:1 zamiast 3:1. Wartość ¼ roku jest wygodna komunikacyjnie, ale lekko zawyża rzeczywisty czas rundy.

### Pierścień 1

Zgodnie z prawem Keplera orbita kołowa w odległości 0,5 AU przesuwałaby się na planszy o ok. 3,6 pola na rundę – model zaokrągla to do 3. Rzeczywiste planety tego pierścienia rozjeżdżają się w obie strony: Wenus przesuwałaby się o ok. 1,9 pola na rundę, Merkury o ok. 5,5. Jeden pierścień z jedną prędkością nie może oddać obu – co nie przeszkadza, skoro obie planety są tłem.

## Pas planetoid – dryf i losowość

### Nieuniknione uproszczenie

Pas planetoid nie jest tarczą obracającą się ze stałą prędkością – każda planetoida krąży z własną prędkością wynikającą z jej orbity. Obiekty bliżej Słońca krążą szybciej, obiekty dalej – wolniej. Plansza jest zsynchronizowana tylko z jedną orbitą (2,24 AU), więc obiekty na pozostałych pierścieniach pasa dryfowałyby względem planszy:

| Pierścień | Odległość | Dryf względem planszy |
|-----------|-----------|----------------------|
| 4 | 2,0 AU | +0,3 pola/rundę (do przodu) |
| – | 2,24 AU (synchronizacja) | 0 |
| 5 | 2,5 AU | −0,3 pola/rundę (do tyłu) |
| 6 | 3,0 AU | −0,9 pola/rundę (do tyłu) |

Ceres dryfowałaby o ok. −0,6 pola/rundę. W trakcie typowej gry (30–50 rund) przesunęłaby się o kilkanaście do kilkudziesięciu pól, a obiekty na zewnętrznym pierścieniu jeszcze więcej.

### Dryf w grze – opcjonalnie

Dryf da się śledzić w prosty sposób, zaokrąglając go do pełnych pól:

| Pierścień | Dryf | Uproszczenie |
|-----------|------|--------------|
| 4 | +0,3 pola/rundę | 1 pole do przodu co 3 rundy |
| 5 | −0,3 pola/rundę | 1 pole do tyłu co 3 rundy |
| 6 | −0,9 pola/rundę | 1 pole do tyłu co rundę |

„Do przodu” oznacza zgodnie z kierunkiem ruchu planet. Sam rachunek jest prosty; kłopotem może być liczba obiektów do przesuwania – co trzecią rundę wszystkie obiekty na pierścieniach 4 i 5, a co rundę na pierścieniu 6.

Gra może więc dryf pominąć albo go realizować, zależnie od potrzeb:

- **Pominięcie** wystarcza, gdy obiekty w pasie pojawiają się losowo i nie trzeba długo śledzić ich dokładnej pozycji. Pas planetoid to miliony ciał na nieznacznie różnych orbitach, więc losowe rozmieszczenie rzutem kości oddaje go dobrze – dryf zostaje pochłonięty przez losowość.
- **Śledzenie** ma sens, gdy gra przez dłuższy czas potrzebuje dokładniej znać pozycję konkretnej planetoidy.

Pojedyncze znane ciała można śledzić osobno, nawet gdy gra pomija dryf reszty pasa. Ceres (2,77 AU) leży na wewnętrznym skraju pierścienia 6, ale krąży szybciej niż reszta tego pierścienia: dryfuje o ok. −0,6 pola/rundę, czyli **2 pola do tyłu co 3 rundy**. Połączone z wymogiem lądownika (patrz „Start z powierzchni”) daje to wyprawę na Ceres, którą trzeba zaplanować: cel się przesuwa, a na miejscu potrzebny jest lądownik.

## Ruch statków a fizyka

Ruch statku na planszy składa się z ruchu po orbicie (razem z pierścieniem) i ruchu własnego, napędzanego silnikiem. Plansza proponuje dwa modele lotów:

- **model referencyjny** – możliwie wierny fizyce, punkt odniesienia dla twardej science fiction,
- **model uproszczony** – prostszy w grze, kosztem kilku świadomych odstępstw od fizyki.

Każda gra może model lotów dalej rozluźniać. Ten rozdział pokazuje, co się wtedy traci.

### Ruch po orbicie to bezwładność

Statek bez napędu na danym pierścieniu leci po orbicie kołowej – czyli swobodnie, bez zużycia paliwa. Model ma więc bezwładność; jego naturalnym stanem nie jest stanie w miejscu, tylko krążenie po orbicie.

### W kosmosie płaci się za zmianę prędkości

W rzeczywistości paliwo zużywa się na zmianę prędkości: na zejście z orbity startowej i na wyrównanie z orbitą celu. Pomiędzy statek leci swobodnie, po łuku wyznaczonym przez grawitację. Długość trasy nie ma więc dużego znaczenia – liczy się, jak szybko trzeba się rozpędzić i ile potem wyhamować.

Jednostką na planszy jest prędkość 1 pola na rundę – ok. **10 km/s** względem lokalnej orbity. To dużo: prędkość orbitalna w pasie planetoid wynosi ok. 20 km/s.

### Model referencyjny

Pełne zasady modelu referencyjnego – przebieg rundy, ruch, dokowanie – są w [opisie planszy](board_pl.md#model-referencyjny). W skrócie: statek ma prędkość własną 0–2 pola na rundę, każde pole zmiany prędkości kosztuje 1 jednostkę paliwa (najwyżej 2 na turę), lot ze stałą prędkością jest darmowy, a dokowanie wymaga prędkości 0. Ten rozdział wyjaśnia, dlaczego zasady są takie.

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

Gdyby traktować prostą linię dosłownie, jako lot swobodny, model rozjeżdżałby się z fizyką. Przy prędkościach z gry grawitacja zakrzywia tor bardzo mocno: w pasie planetoid 1 pole na rundę do przodu (+10 km/s) wystarcza, żeby uciec z Układu Słonecznego, a 2 pola na rundę do tyłu (−20 km/s) prawie zatrzymują statek względem Słońca, który zaczyna na nie spadać.

Błąd położenia statku lecącego swobodnie z prędkością 1 pola na rundę, w porównaniu z prostą linią w grze (w polach):

| Gdzie | po 1 rundzie | po 2 rundach | po 3 rundach |
|-------|-----------|-------------|-------------|
| przy Ziemi | 1,1–1,9 | 2–6 | 2–8 |
| przy Marsie | 0,7–1,0 | 1,6–4 | 2–8 |
| pas planetoid (2,24 AU) | 0,3–0,6 | 1,0–2,3 | 1,6–5 |
| pas planetoid (3 AU) | 0,2–0,4 | 0,7–1,5 | 1,1–3,4 |

Główny mechanizm jest jednym z najbardziej nieintuicyjnych zjawisk mechaniki orbitalnej: rozpędzenie do przodu wzdłuż orbity podnosi orbitę. Statek lecący w pasie do przodu po 3 rundach jest ok. 3 pierścienie dalej od Słońca i wcale nie przesunął się do przodu.

Prosty kurs da się utrzymać ciągiem, ale koszt mocno zależy od kierunku. Koszt na rundę przy prędkości 1 pola na rundę:

| Gdzie | do przodu | do tyłu | na zewnątrz | do środka |
|-------|-----------|---------|-------------|-----------|
| przy Ziemi | 3,5 | 2,5 | 0,5 | – |
| przy Marsie | 2,0 | 1,3 | 0,3 | 0,5 |
| pas planetoid | 1,1 | 0,7 | 0,2 | 0,3 |

Lot od Słońca i do Słońca jest prawie darmowy, lot wzdłuż orbity – drogi. Sprawdzono też prostą zasadę zakrzywiania toru (prędkość do przodu zamienia się w prędkość na zewnątrz: w pasie 1, przy Marsie 2, przy Ziemi 3 pola na rundę). Poprawia ona lot do przodu, ale psuje lot do tyłu – nie jest warta dodatkowej zasady. Ujęcie linii lotu jako schematu zaplanowanej trasy jest prostsze i daje poprawne koszty.

### Przebieg rundy i dokowanie

**Ruch po orbicie na początku tury.** Ruch po orbicie liczy się z pierścienia, na którym statek naprawdę stoi; po ruchu własnym statek mógłby być już na innym pierścieniu, gdzie pole oznacza inny kąt. Planety przesuwają się w turze neutralnej, na początku rundy, więc gracze w swoich turach celują w aktualne położenia.

**Pola stacji przy Ziemi i Marsie.** Statek zadokowany przy planecie porusza się razem z nią. Gdyby stał na siatce, przez chwilę między turą neutralną a swoją turą „odstawałby” od planety. Pole stacji poza siatką usuwa ten problem i tłok przy planecie.

**Dokowanie wymaga tylko stabilizacji.** Zbliżenie i dokowanie trwają godziny, najwyżej dni, a runda to ok. 87 dni. Wystarczy więc, że statek ma prędkość 0 na polu celu w którymkolwiek momencie swojej tury. Inaczej z długimi działaniami: zmiana prędkości o 2 pola to praca silnika przez całą rundę (ok. 0,27 milli-g przez 87 dni). Postój w przelocie – zahamowanie i ponowne rozpędzenie w tej samej turze – zostawia czas tylko na krótkie działania, a wydobycie czy awaryjne tankowanie wymagają tury bez żadnej zmiany prędkości.

**Zmiana prędkości przed ruchem i po nim.** Silnik pracuje przez całą rundę, a 2 pola zmiany prędkości to jego możliwości w tym czasie. Przy stałym ciągu statek przebywa w rundzie drogę odpowiadającą średniej prędkości – prędkości z połowy rundy. Dlatego zmiana dzieli się na dwie połowy po najwyżej 1 polu: przed ruchem i po ruchu. Ruch między nimi odbywa się z prędkością z połowy rundy, tak jak przy ciągłej pracy silnika. To ta sama metoda (tzw. leapfrog), której używa się w numerycznych symulacjach ruchu orbitalnego. Zmiana całej prędkości przed ruchem zawyżałaby drogę, a po ruchu – zaniżała. Przeskok, rozpędzanie i hamowanie nie potrzebują przy tym osobnych zasad.

### Okna transferowe

**Częstotliwość okien jest dokładna.** Planety poruszają się na planszy zgodnie z rzeczywistością, więc korzystne ustawienia powtarzają się co tyle samo rund co w rzeczywistości: Ziemia–Mars co 9 rund (ok. 26 miesięcy), Ziemia–pas planetoid co 6 rund, Mars–pas planetoid co 18 rund.

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
- **Sterowanie** – pierścień przesuwa się o pół obiegu na rundę, a grawitacja zakrzywia tor jeszcze mocniej niż przy Ziemi. Statek o prędkości własnej 1–2 pola na rundę praktycznie traci kontrolę nad tym, gdzie się znajdzie.
- **Koszt oszczędnych tras** – są tam 8–11 razy droższe niż w pasie planetoid. W rzeczywistości misje do Merkurego trwają latami i wymagają wielu przelotów obok planet: sonda MESSENGER wystartowała w 2004 roku, a na orbitę Merkurego weszła dopiero w 2011, po sześciu takich przelotach.

Zasada pasuje do roli Merkurego i Wenus jako tła. Gra, która chce tam latać, może ją zdjąć.

### Napęd i paliwo

Model referencyjny wymaga **napędu fuzyjnego**: przy jednostce 10 km/s inne napędy nie unoszą wystarczająco dużo paliwa.

**Ciąg.** Zmiana prędkości o 2 pola w ciągu rundy to ok. 20 km/s w 87 dni – stałe przyspieszenie ok. 0,27 milli-g. Przy prędkości wylotu ok. 300 km/s wymaga to mocy rzędu 0,7 MW na tonę statku. To odległa przyszłość, ale fizyka pozostaje uczciwa: przyspieszenia są rzędu milli-g, a nie całego g, jak w mniej powściągliwej fantastyce naukowej.

**Zbiornik.** Zmiana prędkości, jaką da pełny zbiornik, zależy tylko od prędkości wylotu i od stosunku masy statku z paliwem do masy bez paliwa – nie od wielkości statku. Dla frachtowca liczy się przy tym ładunek, bo wchodzi do masy. Przykład: konstrukcja o masie 1, ładunek 1 (albo 2), pełny zbiornik o masie 2, prędkość wylotu ok. 300 km/s:

| Stan frachtowca | Stosunek mas | Δv | Jednostki w grze |
|-----------------|--------------|----|------------------|
| pusty | 3 | ok. 330 km/s | ok. 33 |
| z ładunkiem | 2 | ok. 210 km/s | ok. 21 |
| mocno obciążony | 1,7 | ok. 155 km/s | ok. 15 |

Na potrzeby gry wystarczy jedna wartość: **zbiornik rzędu 20 jednostek**. Przeskok kosztuje 2, a cała trasa z rozpędzeniem, poprawkami i hamowaniem ok. 3–6, więc paliwo realnie ogranicza – statki muszą tankować. Gra, która chce oddać wpływ ładunku, może pozwolić pustemu statkowi lecieć dalej – ok. 1,5 raza. Lżejsze statki pasażerskie mają większy stosunek mas, więc i większy zasięg.

Inne napędy nie wystarczają. Napęd jądrowo-elektryczny (prędkość wylotu ok. 40 km/s) dałby zbiornik na ok. 3 jednostki, jądrowy termiczny (ok. 9 km/s) – na mniej niż 1.

**Tankowanie w pasie planetoid.** Materiał pędny – wodę – można pozyskiwać z samych planetoid. Statek musi się w tym celu zatrzymać: wylądować na małej planetoidzie albo wejść na orbitę wokół niej.

- **Ile wody to jednostka.** Jedna jednostka to ok. 1/20 zbiornika. Dla frachtowca o konstrukcji 1000 t, z ładunkiem 1000 t i zbiornikiem 2000 t to ok. 100 t wody.
- **Ile skały trzeba przerobić.** Planetoidy węgliste zawierają zwykle ok. 5–20% wody, związanej w minerałach; odzyskuje się ją, podgrzewając urobek do kilkuset stopni. Przy 10% wody jedna jednostka to ok. 1000 t skały.
- **Co ogranicza tempo.** Nie energia: reaktor frachtowca ma moc rzędu kilku gigawatów, a odzyskanie 100 t wody na dobę wymaga ok. 12 MW. Ogranicza sprzęt – ile urobku da się wykopać i przerobić w mikrograwitacji. Prawdziwych danych nie ma, bo nikt jeszcze tego nie robił.

Proponowane wartości:

| Sposób | Wydajność | Pełny zbiornik |
|--------|-----------|----------------|
| awaryjny zestaw na pokładzie frachtowca (ok. 1–2,5 t skały na godzinę) | ok. 3 jednostki na rundę postoju | ok. 7 rund |
| stacja wydobywcza | cały zbiornik | 1 runda |

Zestaw awaryjny jest tak wolny, że to rzeczywiście rozwiązanie awaryjne – w czasie postoju Ziemia i okna transferowe uciekają. Jak lądownik, zestaw ma masę i zmniejsza zasięg statku.

Wody więcej jest w zewnętrznej części pasa: w wewnętrznej przeważają planetoidy kamienne, uboższe w wodę, w zewnętrznej – węgliste. Na planszy pierścienie 5–6 mogą więc dawać więcej wody niż pierścień 4.

Woda jest materiałem pędnym, a nie paliwem reakcji fuzyjnej. Paliwo fuzyjne, na przykład deuter, to znikoma część masy – a deuter także da się odzyskać z wody.

Te wartości – wydajność, zawartość wody, dostępność stacji – to dobre pokrętła do konfigurowania różnych scenariuszy gier.

### Start z powierzchni

Paliwo nie jest tu problemem: wejście z powierzchni Ziemi na niską orbitę to ok. 9,4 km/s (prędkość orbitalna 7,9 km/s plus straty na pokonanie grawitacji i oporu powietrza) – niecała jednostka. Problemem jest ciąg. Żeby wystartować, silnik musi dawać przyspieszenie większe niż grawitacja na powierzchni, w praktyce ok. 1,2–1,5 g. Napęd fuzyjny z modelu referencyjnego daje ok. 0,27 milli-g:

| Ciało | Grawitacja na powierzchni | Ciąg statku względem ciężaru | Prędkość orbitalna przy powierzchni |
|-------|---------------------------|------------------------------|-------------------------------------|
| Ziemia | 9,8 m/s² | 1/3700 | 7,9 km/s |
| Mars | 3,7 m/s² | 1/1400 | 3,6 km/s |
| Ceres | 0,28 m/s² | 1/106 | 0,37 km/s |
| Westa | 0,25 m/s² | 1/94 | 0,26 km/s |
| planetoida o średnicy 1 km | 0,0003 m/s² | 9,5 | ok. 0 |

Przy typowej gęstości planetoid (ok. 2 g/cm³) statek wystartuje z ciała o średnicy do ok. 6–10 km.

Mocniejszy silnik tego nie rozwiąże: przy danej mocy większa prędkość wylotu oznacza mniejszy ciąg, więc napęd oszczędny w paliwie z natury pcha słabo. Do startu z Ziemi potrzebna jest rakieta chemiczna o prędkości wylotu ok. 4 km/s. Wylot napędu fuzyjnego w atmosferze byłby zresztą strumieniem gorącej plazmy.

Wynikają z tego trzy rzeczy:

- Frachtowce fuzyjne latają z orbity na orbitę. Przy Ziemi i Marsie dokują do stacji orbitalnych, a na powierzchnię i z powrotem kursują osobne lądowniki, na przykład chemiczne. Podobnie wygląda większość dzisiejszych koncepcji transportu w Układzie Słonecznym: rakiety do niskiej orbity, a dalej osobne holowniki kosmiczne.
- Wejście na orbitę z Marsa (ok. 4 km/s) jest dużo tańsze niż z Ziemi (ok. 9,4 km/s), więc stację przy Marsie łatwiej zaopatrywać z powierzchni.
- Ceres i Westa też wymagają lądowników, ale tanich – prędkość ucieczki z Ceres to ok. 0,5 km/s. Na małych planetoidach frachtowiec ląduje bezpośrednio.

**Lądownik na wyposażeniu frachtowca.** Na Ceres i Weście lądownik potrzebuje niewiele: z niskiej orbity na powierzchnię i z powrotem to ok. 0,8 km/s na Ceres i ok. 0,6 km/s na Weście, bez atmosfery i przy słabej grawitacji. Wystarczy mały lądownik chemiczny, który frachtowiec może wozić ze sobą. Paliwo do niego – wodór i tlen z rozłożonej wody – można pozyskiwać w pasie planetoid. Masa lądownika liczy się jednak do masy statku bez paliwa, więc frachtowiec z lądownikiem ma mniejszy zasięg albo zabiera mniej ładunku.

Przy Marsie własny lądownik jest możliwy, ale ciężki (ok. 5 km/s na lądowanie i powrót na orbitę) i potrzebuje paliwa na powierzchni. Przy Ziemi samo wejście na orbitę wymaga dużej rakiety z infrastrukturą naziemną – tego frachtowiec nie zabierze.

Tam, gdzie powstała stała osada, naturalne jest utrzymywanie lądowników na miejscu, tak jak przy Ziemi i Marsie. Własny lądownik frachtowca to rozwiązanie na miejsca bez infrastruktury – czyli na początki eksploracji pasa planetoid.

### Manewry w pasie planetoid

Pas planetoid jest bardzo pusty – średnia odległość między planetoidami to ok. miliona km, a sondy przelatują przez niego bez żadnych manewrów. Ominięcie przeszkód nie jest więc tym, co kosztuje. Kosztuje dopasowanie się do celu: żeby wylądować na konkretnej planetoidzie, trzeba wejść na jej orbitę, a każda planetoida ma własną. To zarazem rzeczywisty odpowiednik dryfu – gdy gra go pomija, jego koszt zawiera się w koszcie manewrów.

### Model uproszczony: koszt za pole

Model uproszczony nie śledzi prędkości statku – płaci się za każde pole ruchu własnego, więcej bliżej Słońca. Zasady są w [opisie planszy](board_pl.md#model-uproszczony).

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

**Limity prędkości** wynikają z założenia, że w jednej rundzie statek może zużyć najwyżej ok. 3 jednostki: przy Ziemi to 1 pole, przy Marsie też 1 (2 pola kosztowałyby 4), w pasie 2 pola. **Kara za prędkość** (2 pola za 3) to dopłata za pośpiech. **Zasada najbliższego pierścienia** sprawia, że lot tam i z powrotem kosztuje tyle samo, tak jak w rzeczywistości.

**Co model uproszczony traci:**

- **Płaci się za drogę, a nie za zmianę prędkości.** Długie przeloty kosztują kilka razy za dużo: trasa o 4 pola kosztuje fizycznie tyle co o 1 pole, a w modelu 4 razy więcej. Kara za prędkość jest za to za mała – fizycznie dwa razy szybszy lot kosztuje dwa razy więcej.
- **Czas jest skrócony nierówno.** Najtańsza trasa Ziemia → Mars trwa ok. 3 rundy, a między sąsiednimi pierścieniami pasa 7–10 rund; w grze każda trwa rundę. Gra skraca więc czas w pasie kilka razy bardziej niż przy Ziemi – i stąd biorą się mnożniki. Przy jednakowym tempie koszt praktycznie nie zależy od pierścienia:

| Czas lotu (rundy) | 1 | 2 | 3 | Najtańsza trasa |
|------------------|---|---|---|-----------------|
| 2 → 3 (Ziemia → Mars) | 19 km/s | 7,9 km/s | 5,4 km/s | 5,4 km/s w 2,9 rundy |
| 3 → 4 | 20 km/s | 9,1 km/s | 5,5 km/s | 3,2 km/s w 4,9 rundy |
| 4 → 5 | 20 km/s | 9,6 km/s | 6,0 km/s | 2,2 km/s w 7,1 rundy |
| 5 → 6 | 20 km/s | 9,8 km/s | 6,3 km/s | 1,6 km/s w 9,6 rundy |

- **Kąty startu w oknach transferowych są przybliżone** (patrz „Okna transferowe”).

Model uproszczony jest spójny sam w sobie i dobrze nadaje się do gier, które nie chcą śledzić prędkości statków. Dalsze uproszczenia – na przykład stały koszt za pole na całej planszy – są możliwe, ale oddalają model od fizyki jeszcze bardziej.

**Geometria planszy.** W żadnym z modeli kosztów nie uwzględniono w samej planszy – na przykład przez pola tym mniejsze, im bliżej Słońca. Plansza pokazywałaby wtedy koszt zamiast przestrzeni i straciłaby to, co jest jej główną wartością: prawdziwe odległości i proporcje ruchu orbitalnego. Mapy zbudowane z kosztów manewrów istnieją (taką ma na przykład gra High Frontier), ale tracą wyczucie, gdzie co naprawdę leży.

Wszystkie liczby w tym rozdziale pochodzą ze skryptów w folderze [tools](../tools/README_pl.md) – każdy może je sprawdzić i przeliczyć dla zmienionej planszy.

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
