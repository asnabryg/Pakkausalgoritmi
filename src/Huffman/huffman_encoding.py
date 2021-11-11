from Huffman.huffman_coding import Huffman_coding
import os

class Huffman_encoding():

    def __init__(self):
        pass

    def encode(self, file_path):
        filename, type = os.path.splitext(file_path)

        h = Huffman_coding()

        with open(file_path, "r") as file, open(filename + "_encoded.bin", "wb") as encoded_file:
            text = file.read()

            tree = h.create_tree(text)
            bit_tree = h.tree_to_bits(tree)
            tree_info_bits = "{0:016b}".format(len(bit_tree))
            print("tree len:", tree_info_bits)

            encoded_bit_text = h.text_to_bits(text, tree)

            all_bits = tree_info_bits + bit_tree + encoded_bit_text

            bytes = h.bits_to_bytes(all_bits)

            encoded_file.write(bytes)
            

