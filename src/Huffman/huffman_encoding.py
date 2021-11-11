from Huffman.huffman_coding import Huffman_coding
import os

class Huffman_encoding():

    def __init__(self):
        pass

    def encode(self, file_path):
        filename, filetype = os.path.splitext(file_path)

        h = Huffman_coding()

        with open(file_path, "r") as file, open(filename + "_encoded.txt", "wb") as encoded_file:
            text = file.read()

            # luodaan puu
            tree = h.create_tree(text)

            # bittiesitys puusta
            bit_tree = h.tree_to_bits(tree)

            # puun koko bitteinä
            tree_info_bits = "{0:016b}".format(len(bit_tree))
            print("tree len:", int(tree_info_bits, 2))

            # pakattu teksti bittiesityksenä
            encoded_bit_text = h.text_to_bits(text, tree)

            # lisäbitit, puun koko, puun rakenne ja teksti bitteinä
            all_bits = tree_info_bits + bit_tree + encoded_bit_text
            print("TREE", bit_tree)
            print("TEXT", encoded_bit_text)

            # bitit muunnetaan tavuiksi ja tallennetaan uuteen tiedostoon
            bytes = h.bits_to_bytes(all_bits)
            print(bin(bytes[-1])[2:].rjust(8, "0"))
            encoded_file.write(bytes)


