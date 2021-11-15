from Huffman.huffman_coding import Huffman_coding
import os

class Huffman_encoding():
    """ Luokka, jossa pakataan tiedosto.
    """

    def __init__(self):
        pass

    def encode(self, file_path):
        """Metodi pakkaa annetun tiedoston.

        Args:
            file_path (str): polku pakattavaan tiedostoon.
        """
        file_name, file_type = os.path.splitext(file_path)
        file_name += "_hm.bin"

        h = Huffman_coding()

        with open(file_path, "r") as file, open(file_name, "wb") as encoded_file:
            text = file.read()

            # luodaan puu
            tree = h.create_tree(text)

            # bittiesitys puusta
            bit_tree = h.tree_to_bits(tree)

            # puun koko bitteinä
            tree_info_bits = "{0:016b}".format(len(bit_tree))

            # pakattu teksti bittiesityksenä
            encoded_bit_text = h.text_to_bits(text, tree)

            # lisäbitit, puun koko, puun rakenne ja teksti bitteinä
            all_bits = tree_info_bits + bit_tree + encoded_bit_text

            # bitit muunnetaan tavuiksi ja tallennetaan uuteen tiedostoon
            bytes = h.bits_to_bytes(all_bits)
            encoded_file.write(bytes)
        
            return file_name


