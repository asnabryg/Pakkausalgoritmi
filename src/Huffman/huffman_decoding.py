import os
from Huffman.huffman_coding import HuffmanCoding
from bit_conversion import bytes_to_bits


class HuffmanDecoding:
    """Luokka, jossa puretaan Huffman menetelmällä pakattu tiedosto.
    """

    def decode(self, file_path):
        """Metodi purkaa annetun pakatun tiedoston.

        Args:
            file_path (str): polku purettavaan tiedostoon.

        Returns:
            str: polku purettuun tiedostoon
        """
        file_name = os.path.splitext(file_path)[0]
        file_name = file_name.replace("_hm", "_decoded")
        file_name += ".txt"

        h = HuffmanCoding()

        with open(file_path, "rb") as file, \
                open(file_name, "w", encoding="utf-8") as decoded_file:
            in_bytes = file.read()

            # muunnetaan tavut bittiesitykseksi
            bits = bytes_to_bits(in_bytes)

            # erotetaan bittiesityksestä puun ja tekstin bitit
            tree_bits, text_bits = h.separate_bits(bits)

            # Luodaan puumalli bittiesityksestä
            tree = h.bits_to_tree(tree_bits)

            # purataan teksti alkuperäiseen mutoon puumallin avulla
            # ja tallennetaan se tiedostoon
            decoded_text = h.bits_to_text(text_bits, tree)

            decoded_file.write(decoded_text)

            # palauttaa puretun tiedoston polun
            return file_name
