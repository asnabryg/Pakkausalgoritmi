# Viikkoraportti 5

## Mitä olen tehnyt tällä viikolla?
- Implementoin LZW algoritmin käyttöliittymmän. Refaktoroin Huffman ja LZW koodeja, kun molemmissa oli samoja metodeita,
jotka tein erilliseen tiedostoon.
- Tein loput testit LZW algoritmille.
- Kirjoitin käyttöohjeen
- Tein lisää suorituskykytestejä, jotka on mainittu testausdokumentissa

## Miten ohjelma on edistynyt?
Käyttöliittymä toimii nyt kokonaan ja oikein. Lisäsin lisää virheiden hallintaa.

## Mitä opin tällä viikolla?
.

## Mikä jäi epäselväksi?
.

## Mitä teen seuraavaksi?
Parantelen vielä dokumentaatiota ja korjaan lint virheitä.
Jos aikaa jää, koitan tehdä oman tietorakenteen minimikeosta.

Huomasin myös, että metodin `bits_to_tree()` aikavaatimuus ei olekaan O(n), joten se tullaan korjaamaan.

### Käytetty aika:
5 tuntia
