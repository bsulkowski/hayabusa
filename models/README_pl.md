# Pionki 3D

*[English version](README.md)*

Uniwersalne pionki do druku 3D, do wykorzystania w dowolnej grze na tej planszy.

![Podgląd modeli](preview.png)

| Plik | Model | Wymiary |
|------|-------|---------|
| [ship.stl](ship.stl) | statek transportowy – modułowy kadłub na kręgosłupie, z dyszami na dole; inspirowany pośrednio statkiem Eagle 1 z serialu „Kosmos 1999” | 26 × 26 × 36 mm |
| [outpost.stl](outpost.stl) | placówka na planetoidzie – część przemysłowa: reaktor, przeróbka i magazyny, antena do dalekiej komunikacji, port | 30 × 30 × 24 mm |

## Statek – intencje projektowe

Od dołu do góry:

- **Zbiorniki i dysze.** Na dole są zbiorniki na „paliwo” – właściwie materiał pędny, odrzucany przez silnik – i dysze silników fuzyjnych.
- **Ładownia.** Podłużny kadłub to ładownia.
- **Habitat.** Trzy moduły wyżej służą do przewozu ludzi i innych istot żywych. Trzy niezależne moduły dają redundancję dla bezpieczeństwa. Obrót statku wokół jego osi wytwarza w nich pozorną grawitację.
- **Mostek.** Na dziobie jest mostek (sterownia).

Ścięty kształt dziobu i zbiorników przy dyszach nie służy opływowości – w próżni nie ma ona znaczenia – tylko widoczności z mostka: wizualnej oraz dla anten i czujników.

**Skala statku.** Obrót wokół osi, wzdłuż której działa ciąg, nie przeszkadza w locie. Pozorna grawitacja wymaga jednak dużego promienia, bo przy szybszym obrocie ludzie dostają choroby lokomocyjnej – bezpieczna granica to zwykle ok. 2–4 obrotów na minutę:

| Pozorna grawitacja | przy 4 obr./min | przy 2 obr./min |
|--------------------|-----------------|-----------------|
| 0,3 g | ok. 17 m od osi | ok. 67 m od osi |
| 1 g | ok. 56 m od osi | ok. 220 m od osi |

Na modelu moduły habitatu leżą od osi w odległości ok. 1/4 długości statku. Prawdziwy statek miałby więc od ok. 70 m długości (0,3 g przy szybkim obrocie) do blisko kilometra (1 g przy wolnym). „Podłoga” w habitacie jest po stronie odwróconej od osi statku.

## Placówka – intencje projektowe

Pionek przedstawia **przemysłową część placówki**. Część mieszkalna stoi osobno, z dala od niej – najlepiej po drugiej stronie planetoidy.

- **Reaktor.** W pasie planetoid światło słoneczne ma tylko 1/5–1/9 mocy przy Ziemi, a wydobycie i przeróbka urobku zużywają dużo energii. Odzysk wody to przede wszystkim podgrzewanie skały, więc reaktor obok przeróbki może dawać ciepło bezpośrednio. Reaktor potrzebuje dużych radiatorów – w próżni nie ma czym chłodzić; to ok. 500 m² na każdy 1 MW mocy elektrycznej.

  Na pionku reaktor siedzi we wgłębieniu – jak w koncepcjach NASA dla baz na Księżycu, gdzie reaktor stoi w wykopie, a grunt osłania przed promieniowaniem. Krzyż na reaktorze symbolizuje radiatory. W rzeczywistości byłyby to duże, cienkie płyty ustawione wysoko nad wykopem, bo radiator oddaje ciepło tylko wtedy, gdy „widzi” otwarte niebo. Na pionku zaznaczono je symbolicznie i masywnie – drobne żebra byłyby kłopotliwe w druku i w utrzymaniu w czystości.
- **Kopuły częściowo wkopane w teren** to zakłady przeróbki i magazyny wody oraz materiału pędnego. Wkopanie daje stałą temperaturę (lód się nie sublimuje) i osłonę przed mikrometeorytami.
- **Antena** stoi na szczycie skały dla lepszej widoczności. Przy reaktorze ma pod ręką moc dla nadajnika.
- **Port.** Statki tankują i ładują tam, gdzie wytwarza się wodę i materiał pędny. Pył i odłamki z silników przy starcie i lądowaniu lecą przy tak słabej grawitacji daleko, więc port powinien być z dala od ludzi.

**Habitat osobno.** Oddalenie chroni mieszkańców przed promieniowaniem reaktora (po drugiej stronie planetoidy zasłania je sama skała), przed skutkami awarii przemysłowych i przed pyłem z portu i wydobycia. Część przemysłowa powinna być w dużej mierze zautomatyzowana i sterowana z habitatu – z odległości kilometra opóźnienie jest pomijalne, w przeciwieństwie do sterowania z Ziemi. Ludzie przychodzą głównie do napraw, więc przyda się mały schron osłonięty od promieniowania na wypadek rozbłysku słonecznego.

**Łączność z Ziemią.** Antena o średnicy kilku metrów zasilana z reaktora daje teoretycznie od kilku do kilkudziesięciu Mb/s nawet przy największej odległości od Ziemi (ok. 3,2 AU); w praktyce straty obniżają to kilkukrotnie. Ograniczeniem jest raczej to, że:

- sygnał idzie 10–27 minut w jedną stronę – można wymieniać wiadomości, ale nie rozmawiać,
- gdy placówka znajdzie się za Słońcem, łączność urywa się na ok. 13 dni; zdarza się to co ok. 1,4 roku, czyli co 6 tur,
- mała planetoida obraca się w kilka godzin, więc z każdego miejsca na powierzchni Ziemię widać tylko przez część obrotu – stałą łączność dają anteny po kilku stronach albo satelita przekaźnikowy na orbicie.

**Słaba grawitacja.** Prędkość ucieczki z planetoidy o średnicy 1 km to ok. 0,5 m/s. Wszystko – maszt anteny, moduły, ludzie – musi być zakotwiczone. Regolit na kopułach osłania, ale niczego nie dociska: 3 m regolitu naciska z siłą ok. 1 Pa, a ciśnienie w module to ok. 100 000 Pa. Kopuły muszą same wytrzymać ciśnienie.

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
- Opcjonalnie, przy najbliższej edycji: wysunąć krzyż radiatorów wyżej ponad krawędź wgłębienia, w tej samej grubości.
