# Toteutusdokumentti

## Huffman koodaus
#### Pakkaus
Ensimmäisenä algoritmi tallentaa sanakirjaan tekstistä kaikki tarvittavat merkit ja niiden lukumäärät tiedostossa.
Sanakirjan avulla voidaan luoda Huffman puumalli, jossa aluksi lisätään minimikekoon jokainen esiintynyt merkki [Huffman solmuna](https://github.com/asnabryg/Pakkausalgoritmi/blob/main/src/Huffman/huffman_node.py),
johon tallennetaan merkki, merkin lukumäärä, vasen- ja oikea lapsi.
Nyt algoritmi kokoaa puun alkaen kahdesta pienimmästä solmusta ja luo niiden avulla uuden solmun, jolla ei ole merkkiä, mutta näiden kahden solmun esiintymis lukumäärän summa. Uusi solmu saa lapsikseen aikaisemmat kaksi solmua ja lisätään solmu minimikekoon.
Toistetaan algoritmiä toistetaan kunnes minimikeossa on enää yksi solmu jäljellä, joka on puun juuri solmu.
Puu esittää uutta bittiesitystä kaikille tarvittaville merkeille. Merkki, jolla on suurin esiintymismäärä tekstissä, saa lyhkäsimmän bittiesityksen jne.
  
Seuraavaksi luoddaan bittiesitys puumallista. Lisätään bitti 0, jos solmulla on lapsi(a), ja bitti 1, jos solmu on lehti ja tallenetaan lehtisolmun merkki bitteinä seuraavaksi.
Tätä toistetaan rekursiivisesti, kunnes jokainen solmu on käyty läpi.

Nyt voimme luoda lopullisen bittiesityksen, ensimmäiseksi tallennetaan puun bittiesityksen koko, sen jälkeen puun bittiesitys ja tiedoston teksti uusilla merkkien bittiesityksillä.
Tämän jälkeen tarkistetaan kuinka monta extra bittiä, pitää lisätä, että esitys voidaan tallentaa tavuina. Extra bittien määrä tallennetaan bittiesityksen alkuun + extra bitit.
Näin algoritmi pystyy purkamaan jatkossa pakatun binaaritiedoston.

#### Purku
Purkaessa aluksi poistamme extrabititien infon, extrabitit, puu bittien infon ja puu bittiesityksen bittiesityksestä.
Luomme puu bittiesityksestä puumallin ja sen perusteella saamme alkuperäisen tekstin näkyville.

#### Aikavaativuus
Puumallin luominen on O(n log n). Puun koko riippuu syötteen koosta, ja puun luominen toimii logaritmisessa ajassa, kun keon jäjestämistä käytetään.
Purku pitäisi toimia O(n).

## Lempel-Ziv-Welch
#### Pakkaus
Ensimmäiseksi tallennetaan sanakirjaan yksittäiset merkit ja niiden Unicode arvo.
Seuraavaksi käydään teskti läpi merkki kerralla, jos nykyinen ja seuraava merkki(jono) yhdistettynä ei ole sanakirjassa, lisätään se ja sen arvoksi 256. Arvo 256 siksi, että ohjelmassa oleva teksti käyttää arvoina 0-255.
Arvo kasvaa yhdellä.  
Koska merkkien yhdiste ei ollut sanakirjassa, lisätään se listaan, joka palautetaan metodin lopussa. Jatketaan looppia eteenpäin.
Jos merkkien yhdiste olisi ollut sanakirjassa, silloin nykyiseksi merkkijonoksi asetettaisiin niiden yhdiste ja jatketaan looppia.
Lista, joka palautettiin, on nyt lyhkäsempi kuin alkuperäinen tiedosto. Tässä algorimissä ei tarvitse tallentaa sanakirjaa bittiesitykseen, vaan se saadaan luotua listan perusteella.
  
Seuraaavaksi luodaan bittiesitys listasta, joka saatiin. Lisätään tarvittavat extrabitit ja niiden info bittiesityksen alkuun ja
tallennetaan se tavuiksi tiedostoon.

#### Purku
Aluksi poistetaan extra bittien info ja extra bitit. Luodaan lopuista biteistä lista, jossa bittien kokonaisluku esitykset.
  
Seuraavaksi luodaan sanakirja listasta, joiden kokonaislukuesitys on alle 256. Avaimena kokonaisluku ja arvona merkki.
Nyt pystymme purkamaan tekstin listan perusteella ja saamme alkuperisen tekstin näkyville.

#### Aikavaativuus
LZW toimii O(n). Algoritmissä ei tarvita järjestämistä kuten Huffman koodauksessa. Sama purkauksessa, joka on O(n).
