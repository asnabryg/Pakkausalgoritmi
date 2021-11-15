# Testausdokumentti

Pakkausalgoritmit on yksikkötestattu Unittest-sovelluskehyksellä

## Huffman
Luokkaa `HuffmanCoding` testataan [TestHuffmanCoding](https://github.com/asnabryg/Pakkausalgoritmi/blob/main/src/Huffman/tests/huffman_coding_test.py)-testiluokalla.
Luokka alustaa alussa tekstin joka pakataan ja siihen Huffman puumallin. Yksikkötestaus testaa jokaisen metodin erikseen `HuffmanCoding`-luokassa. Testeissä käytetyt tekstit ja bittiesitykset
ovat yksinkertaisia, joten niitä on helppo testata.  

Luokassa `HuffmanEncoding` testataan, että [test_file.txt](https://github.com/asnabryg/Pakkausalgoritmi/blob/main/src/Huffman/tests/test_file.txt), purku onnistuu ja
luo uuden pakatuntiedoston alkuperäisen tiedoston viereen.  
Tämän jälkeen testataan `HuffmanDecoding`-luokkaa, että se purkaa pakatun tiedoston oikein ja teksti on sama kuin alkuperäinen.

## Lempel-Ziv-Welch
keskeneräinen

## Testauskattavuus
Ohjelman tämän hetkinen (15.11.2021) testauskattavuus on 100%.
