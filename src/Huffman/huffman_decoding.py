import os
from Huffman.huffman_coding import HuffmanCoding


class HuffmanDecoding:
    """Luokka, jossa puretaan pakattu tiedosto.
    """

    def __init__(self):
        pass

    def decode(self, file_path):
        """Metodi purkaa annetun pakatun tiedoston.

        Args:
            file_path (str): polku purettavaan tiedostoon.
        """
        file_name = os.path.splitext(file_path)[0]
        file_name = file_name.replace("_hm", "")
        file_name += ".txt"

        h = HuffmanCoding()

        with open(file_path, "rb") as file, \
             open(file_name, "w", encoding="utf-8") as decoded_file:
            in_bytes = file.read()

            # muunnetaan tavut bittiesitykseksi
            bits = ""
            for byte in in_bytes:
                bits += bin(byte)[2:].rjust(8, "0")

            # erotetaan bittiesityksestä puun ja tekstin bitit
            tree_bits, text_bits = h.separate_bits(bits)

            # Luodaan puumalli bittiesityksestä
            tree = h.bits_to_tree(tree_bits)

            # purataan teksti alkuperäiseen mutoon puumallin avulla
            decoded_text = h.bits_to_text(text_bits, tree)
            print("DECODED TEXT", decoded_text)

            decoded_file.write(decoded_text)
            return file_name
