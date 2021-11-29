# Käyttöohje

## Poetryn asennus
<sub>**HUOM!** Tee tämä, jos koneellesi ei ole vielä asennettu Poetryä.</sub>  
1. Asennus onnistuu seuraamalla Poetryn [asennusohjeita](https://python-poetry.org/docs/#installation).
2. Suorita asennuksen jälkeen komento ```export PATH="$HOME/.poetry/bin:$PATH"```.  
Tämä asettaa PATH-muuttujaan polun Poetryn binääriin.

## Ohjelman asennus
Suorita seuraavat komennot:  

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```  

2. Käynnista ohjelma komennolla:
```bash
poetry run invoke start
```

## Ohjelman käyttö
Käynnistämisen jälkeen termnaaliin tulee:
```
Komennot:
  1. Pakkaa tekstitiedosto
  2. Pura tiedosto
  3. Sulje ohjelma
> 
```

Valitse mitä haluat suorittaa painamalla "1", "2" tai "3" ja paina "enter".

### Pakkaaminen
Valitaan "pakkaa tekstitiedosto" painamalla "1" ja "enter" nappeja.  
Tämän jälkeen voit valita pakkausmenetelmän.
```
Valitse pakkausmenetelmä:
  1. Huffman
  2. Lempel Ziv Welch
> 
```  
Kun olet valinnut pakkausmenetelmän. Terminaali kysyy:
```
Syötä tiedoston polku:
```
Syötä tekstitiedoston polku, jonka haluat pakata.
Pakkauksen jälkeen terminaali kertoo, mihin tiedosto on pakattu ja pakkaustehon. Esim:
```
Tiedosto pakattu polkuun: /home/kayttaja/Documents/tiedosto_lzw.bin
Pakattutiedosto n. 48.28 % pienempi.
``` 

### Purku
Valitaan "pura tiedosto" painamalla "2" ja "enter" nappeja.  
Tämän jälkeen voit valita purkumenetelmän.
```
Valitse purkumenetelmä:
  1. Huffman
  2. Lempel Ziv Welch
>
```
Kun olet valinnut purkumenetelmän. Terminaali kysyy tiedoston polkua.
Anna tiedosto, joka on pakattu tällä ohjelmalla.  
- "_hm.bin" loppuinen tiedosto on pakattu Huffman menetelmällä ja voidaan purkaa sillä.
- "_lzw" loppuinen tiedosto on pakattu Lempel-Ziv-Welch menetelmällä ja voidaan purkaa sillä.

Tiedoson purun jälkeen terminaali kertoo, mihin tiedosto on purettu. Esim:
```
Tiedosto purettu polkuun: /home/kayttaja/Documents/tiedosto_decoded.txt
```
Purettu tiedosto saa nimensä loppuun "_decoded.txt", jotta voidaan helposti tunnistaa uusi tiedosto.

### Virheiden hallinta

Ohjelma kertoo, jos polku tai tiedosto on virheellinen ja kysyy uudelleen komentoa.
