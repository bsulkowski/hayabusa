# Hayabusa

**Plansza do gier w wewnętrznym Układzie Słonecznym**

*[English version](README.md)*

Heksagonalna plansza do gier twardej science fiction o początkach eksploracji kosmosu – od Słońca po pas planetoid. Fizyka jest prawdziwa, z przyszłości pochodzą tylko silniki statków. Odległości i prędkości orbitalne zachowują rzeczywiste proporcje, a sama plansza obraca się razem z pasem planetoid: planety bliżej Słońca co rundę przesuwają się po swoich orbitach, a statki graczy muszą się z tym liczyć.

Plansza nie jest przypisana do jednej gry – to przestrzeń, na której można budować różne gry.

## Plansza

| Plik | Opis |
|------|------|
| [board/board_pl.pdf](board/board_pl.pdf) ([SVG](board/board_pl.svg)) | plansza, wersja polska (v0.4.1) |
| [board/board.pdf](board/board.pdf) ([SVG](board/board.svg)) | plansza, wersja angielska (v0.4.1) |
| [board/board-light_pl.pdf](board/board-light_pl.pdf) ([SVG](board/board-light_pl.svg)) | plansza alternatywna, wersja polska (v0.4e) |
| [board/qrcode_pl.svg](board/qrcode_pl.svg), [board/qrcode.svg](board/qrcode.svg) | kody QR do strony projektu |
| [models/](models/README_pl.md) | pionki do druku 3D: statek transportowy i placówka na planetoidzie |

Poprzednie wersje grafiki planszy są w historii repozytorium (tagi `v0.1`–`v0.4.1`, patrz [historia wersji](#historia-wersji)). Eksperymentalna kolorystyka planszy jest na branchu `experimental-colors`.

## Dokumentacja

- [Jak działa plansza](docs/board_pl.md) – dla graczy i projektantów gier, którzy chcą wykorzystać gotową planszę
- [Model i decyzje projektowe](docs/model_pl.md) – jak plansza ma się do rzeczywistego Układu Słonecznego
- [Pomysły na gry](docs/ideas_pl.md) – motywy i elementy wynikające z fizyki planszy
- [Filozofia projektu](docs/design_pl.md) – zasady, według których plansza jest projektowana
- [Obliczenia](tools/README_pl.md) – skrypty, którymi policzono model

## Historia wersji

| Wersja | Data | Zmiany |
|---|---|---|
| 0.5 | 2026-11-27 | Nazwa: Hayabusa<br>Opis planszy, model i decyzje projektowe, pomysły na gry, filozofia projektu (PL, EN)<br>Model referencyjny lotów (ruch wektorowy) i model uproszczony<br>Pionki do druku 3D<br>Skrypty obliczeniowe<br>Grafika planszy bez zmian (v0.4.1) |
| 0.4.1 | 2025-11-12 | Obrót planszy |
| 0.4 | 2025-11-03 | Nowy układ i kolory planszy<br>Alternatywna jasna plansza v0.4e (PL) |
| 0.3b | 2025-10-30 | Ciemna kolorystyka (PL) |
| 0.3 | 2025-10-29 | Wersja angielska<br>Pola pasa planetoid oznaczone do rzutu k12 + k8<br>Tytuł i kod QR |
| 0.2 | 2025-10-15 | Strefy w kolorach (PL) |
| 0.1 | 2025-10-15 | Pierwszy szkic: siatka, orbity planet, ruch orbitalny (PL) |

## Licencja

Plansza i dokumentacja: [CC BY 4.0](LICENSE) – Bartosz Sułkowski. Modele 3D w folderze `models/`: również CC BY 4.0. Kod w folderze `tools/`: [MIT](tools/LICENSE).
