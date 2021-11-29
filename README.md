# Pakkausalgoritmi
Tiralabran harjoitustyö 2021

## Dokumentaatio
 - [käyttöohje](./Dokumentaatio/käyttöohje.md)
 - [määritelydokumentti](./Dokumentaatio/määrittelydokumentti.md)
 - [testausdokumentti](./Dokumentaatio/testaus.md)
 - [toteutusdokumentti](./Dokumentaatio/toteutusdokumentti.md)

## Viikkoraportit
- [Viikko 1](./Dokumentaatio/Viikkoraportti1.md)
- [Viikko 2](./Dokumentaatio/Viikkoraportti2.md)
- [Viikko 3](./Dokumentaatio/Viikkoraportti3.md)
- [Viikko 4](./Dokumentaatio/Viikkoraportti4.md)

## Komentorivikomennot
### Ohjelman suorittaminen:
```bash
poetry run invoke start
```
### Testaus:
```bash
poetry run invoke test
```
### Testikattavuus:
```bash
poetry run invoke coverage-report
```
Raportti generoituu ./htmlcov/index.html tiedostoon.

### Pylint:
Suorittaa tiedoston [.pylintrc](.pylintrc) määrittelemät tarkistukset:
```bash
poetry run invoke lint
```
