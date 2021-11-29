import os
from LZW.lzw_coding import LzwCoding
from bit_conversion import bytes_to_bits


class LzwDecoding():
    """Luokka, jossa puretaan LZW menetelmällä pakattu tiedosto.
    """

    def __init__(self):
        pass

    def decode(self, file_path):
        """Metodi purkaa pakatun tiedoston.

        Args:
            file_path (str): polku purettavaan tiedostoon.

        Returns:
            str: polku purettuun tiedostoon
        """

        file_name = os.path.splitext(file_path)[0]
        file_name = file_name.replace("_lzw", "_decoded")
        file_name += ".txt"

        lzw = LzwCoding()

        with open(file_path, "rb") as file, \
                open(file_name, "w", encoding="utf-8") as decoded_file:
            in_bytes = file.read()

            # muunnetaan tavut bittiesitykseksi
            bits = bytes_to_bits(in_bytes)

            # muunnetaan bittiesitys tulosteeksi
            output = lzw.bits_to_output(bits)

            # muunnetaan tuloste tekstiksi ja tallennetaan se tiedostoon
            text = lzw.output_to_text(output)
            decoded_file.write(text)

            # palautetaan puretun tiedoston polu
            return file_name
