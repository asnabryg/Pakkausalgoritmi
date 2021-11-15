from Huffman.huffman_coding import Huffman_coding
import os


class Huffman_decoding:
    """Luokka, jossa puretaan pakattu tiedosto.
    """

    def __init__(self):
        pass

    def decode(self, file_path):
        """Metodi purkaa annetun pakatun tiedoston.

        Args:
            file_path (str): polku purettavaan tiedostoon.
        """
        file_name, file_type = os.path.splitext(file_path)
        file_name = file_name.replace("_hm", "")
        file_name += ".txt"

        h = Huffman_coding()

        with open(file_path, "rb") as file, open(file_name, "w") as decoded_file:
            bytes = file.read()

            # muunnetaan tavut bittiesitykseksi
            bits = ""
            for byte in bytes:
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
