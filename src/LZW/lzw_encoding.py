import os
from LZW.lzw_coding import LzwCoding
from bit_conversion import bits_to_bytes


class LzwEncoding():
    """Luokka, jossa pakataan LZW menetelmällä tiedosto.
    """

    def encode(self, file_path):
        """Metodi pakkaa annetun tiedoston.

        Args:
            file_path (str): polku pakattavaan tiedostonn

        Returns:
            str: polku pakattuun tiedostoon.
        """

        file_name = os.path.splitext(file_path)[0]
        file_name += "_lzw.bin"

        lzw = LzwCoding()

        with open(file_path, "r", encoding="utf-8") as file, \
                open(file_name, "wb") as encoded_file:
            text = file.read()

            # modostaa pakatun tulosteen tekstistä
            output = lzw.create_output(text)

            # luo bittiesityksen tulosteesta
            bits = lzw.output_to_bits(output)

            # muuttaa bittiesitykse tavuiksi ja tallennetaan tiedostoon
            in_bytes = bits_to_bytes(bits)
            encoded_file.write(in_bytes)

            # palauttaa pakatun tiedoston polun
            return file_name
