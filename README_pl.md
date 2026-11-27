# Hayabusa

**Plansza do gier w wewnętrznym Układzie Słonecznym**

*[English version](README.md)*

Heksagonalna plansza do gier twardej science fiction o początkach eksploracji kosmosu – od Słońca po pas planetoid. Fizyka jest prawdziwa, z przyszłości pochodzą tylko silniki statków. Odległości i prędkości orbitalne zachowują rzeczywiste proporcje, a sama plansza obraca się razem z pasem planetoid: planety bliżej Słońca co rundę przesuwają się po swoich orbitach, a statki graczy muszą się z tym liczyć.

Plansza nie jest przypisana do jednej gry – to przestrzeń, na której można budować różne gry.

## Plansza

| Plik | Opis |
|------|------|
| [board/board_pl_a2.pdf](board/board_pl_a2.pdf), [board/board_pl_a3.pdf](board/board_pl_a3.pdf) | plansza do druku, wersja polska: A2 z 4 kartek A4, A3 z 2 kartek A4 |
| [board/board_a2.pdf](board/board_a2.pdf), [board/board_a3.pdf](board/board_a3.pdf) | to samo, wersja angielska |
| [board/board-light_pl_a2.pdf](board/board-light_pl_a2.pdf), [board/board-light_pl_a3.pdf](board/board-light_pl_a3.pdf), [board/board-light_a2.pdf](board/board-light_a2.pdf), [board/board-light_a3.pdf](board/board-light_a3.pdf) | wersja jasna, przyjazna drukarce |
| [board/board_pl.svg](board/board_pl.svg), [board/board.svg](board/board.svg), [board/board-light_pl.svg](board/board-light_pl.svg), [board/board-light.svg](board/board-light.svg) | cała plansza na jednej stronie |
| [board/board_pl.png](board/board_pl.png), [board/board.png](board/board.png) | podgląd |
| [board/qrcode_pl.svg](board/qrcode_pl.svg), [board/qrcode.svg](board/qrcode.svg) | kody QR do strony projektu |
| [models/](models/README_pl.md) | pionki do druku 3D: statek transportowy i placówka na planetoidzie |

Wszystkie pliki w `board/` tworzy [`tools/board_svg.py`](tools/README_pl.md#generator-planszy) – żeby zmienić planszę, zmienia się skrypt, nie pliki. Druk i składanie kartek: [Jak działa plansza](docs/board_pl.md#wydruk). Poprzednie wersje grafiki planszy są w historii repozytorium (tagi `v0.1`–`v0.4.1`, patrz [historia wersji](#historia-wersji)). Eksperymentalna kolorystyka planszy jest na branchu `experimental-colors`.

## Dokumentacja

- [Jak działa plansza](docs/board_pl.md) – dla graczy i projektantów gier, którzy chcą wykorzystać gotową planszę
- [Model i decyzje projektowe](docs/model_pl.md) – jak plansza ma się do rzeczywistego Układu Słonecznego
- [Pomysły na gry](docs/ideas_pl.md) – motywy i elementy wynikające z fizyki planszy
- [Filozofia projektu](docs/design_pl.md) – zasady, według których plansza jest projektowana
- [Obliczenia](tools/README_pl.md) – skrypty, którymi policzono model

## Historia wersji

| Wersja | Data | Zmiany |
|---|---|---|
| 0.6 | 2026-11-27 | Grafika planszy z generatora (`tools/board_svg.py`)<br>Tytuł Hayabusa z podtytułem, kod QR do strony projektu<br>Druk na kartkach A4 sklejanych na styk, łączenia między środkami pól: A2 z 4, A3 z 2<br>Pola stacji Ziemi i Marsa, Ceres obok planszy – w skali, z niskimi orbitami<br>Skale na planszy: siatka 1 : 2,5·10<sup>12</sup>, planety 1 : 6·10<sup>7</sup> (A2)<br>Napisy poziomo, sektory jak na tarczy zegara (12 u góry), z pomarańczowymi granicami<br>Wersja jasna w obu językach |
| 0.5 | 2026-11-27 | Nazwa: Hayabusa<br>Opis planszy, model i decyzje projektowe, pomysły na gry, filozofia projektu (PL, EN)<br>Model referencyjny lotów (ruch wektorowy) i model uproszczony<br>Pionki do druku 3D<br>Skrypty obliczeniowe<br>Grafika planszy bez zmian (v0.4.1) |
| 0.4.1 | 2025-11-12 | Obrót planszy |
| 0.4 | 2025-11-03 | Nowy układ i kolory planszy<br>Alternatywna jasna plansza v0.4e (PL) |
| 0.3b | 2025-10-30 | Ciemna kolorystyka (PL) |
| 0.3 | 2025-10-29 | Wersja angielska<br>Pola pasa planetoid oznaczone do rzutu k12 + k8<br>Tytuł i kod QR |
| 0.2 | 2025-10-15 | Strefy w kolorach (PL) |
| 0.1 | 2025-10-15 | Pierwszy szkic: siatka, orbity planet, ruch orbitalny (PL) |

## Licencja

Plansza i dokumentacja: [CC BY 4.0](LICENSE) – Bartosz Sułkowski. Modele 3D w folderze `models/`: również CC BY 4.0. Kod w folderze `tools/`: [MIT](tools/LICENSE).
