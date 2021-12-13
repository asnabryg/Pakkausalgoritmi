from custom_expections import EmptyFileException


class LzwCoding:
    """Luokka, jossa on kaikki Lempel-Ziv-Welch algoritmiin tarvittavat metodit.
    """

    def create_output(self, text: str):
        """Luo pakatun listan merkkien ja merkkijonojen kokonaislukuesityksistä.

        Args:
            text (str): pakattava teksti

        Returns:
            list: lista kokonaislukuesityksistä
        """

        if text == "":
            raise EmptyFileException

        code_table = {}
        # tallennetaan yksittäiset kirjaimet ja niiden Unicode arvo sanakirjaan
        for char in text:
            if char not in code_table:
                code_table[char] = ord(char)

        value = 256
        current = text[0]
        output = []
        for i in range(len(text)):
            # seuraava merkki
            next = text[i+1] if i != len(text)-1 else ""

            new = current + next
            if new not in code_table:
                # lisää tulosteeseen nykyisen merkkijonon arvo
                output.append(code_table[current])

                # tallenna uusi merkkien yhdistelmä ja arvo sanakirjaan
                code_table[new] = value

                # kasvata seuraavan merkkijonon arvoa yhdellä
                value += 1

                # valitse seuraava tarkistettava merkki
                current = next
            else:
                # valitse seuraava tarkistettava merkkijono
                current = new

        # lisää viimeisen merkkijonon arvo tulosteeseen
        output.append(code_table[current])

        return output

    def output_to_bits(self, output: list):
        """Luo listan kokonaisluvuista bittiesityksen, jonka alussa on
        tieto tarvittavien bittien määrästä lukujen esittämiseksi.

        Args:
            output (list): lista kokonaislukuesityksistä

        Returns:
            str: valmis bittiesitys
        """
        # suurin luku listassa
        max_value = max(output)

        # tarvittavien bittien määrä lukujen esittämiseen
        max_bit_length = len("{:b}".format(max_value))

        # tarvittavien bittien määrä bitteinä
        bit_info = "{0:08b}".format(max_bit_length)

        bits = ""
        # luodaan bittiesitys luvuista
        for code in output:
            b = "{0:0" + str(max_bit_length) + "b}"
            bits += b.format(code)

        # lisätään bittiesityksen alkuun tarvittavienbittien määrä
        return bit_info + bits

    def bits_to_output(self, bits):
        """Poistaa bittiesityksestä extrabitit ja bittien pituus infon.
        Luo niiden perusteella kokonaislukuesitykset listana.

        Args:
            bits (str): bittiesitys

        Returns:
            list: lista kokonaislukuesityksistä
        """
        # poistetaan extra bitit
        extra_bits_count = int(bits[:8], 2)
        bits = bits[8 + extra_bits_count:]

        # poistetaan bitti info
        bit_length = int(bits[:8], 2)
        bits = bits[8:]

        # luo ja palauta tuloste
        return [int(bits[i:i+bit_length], 2) for i in range(0, len(bits), bit_length)]

    def output_to_text(self, output):
        """Purkaa pakatun tuloste listan alkuperäiseksi tekstiksi.

        Args:
            output (list): pakattu tuloste

        Returns:
            str: purettu teksti
        """

        code_table = {}
        # Luodaan sanakirja, jossa tekstin yksittäiset merkit ja
        # kokonaislukuesitykset lisätty
        for n in output:
            if n < 256:
                code_table[str(n)] = chr(n)

        value = 256
        current = str(output[0])
        text = code_table[current]

        for i in range(len(output)-1):
            # seuraava merkki
            next = str(output[i+1])
            c = code_table[next][0] if next in code_table else code_table[current]

            # lisätään merkkien yhdiste sanakirjaan
            chars = code_table[current] + c
            code_table[str(value)] = chars

            value += 1
            current = next

            # lisätään tekstiin purettu merkkiyhdiste
            text += code_table[current]

        return text
