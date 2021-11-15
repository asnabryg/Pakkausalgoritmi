import os
import unittest
from Huffman.huffman_coding import HuffmanCoding
from Huffman.huffman_encoding import HuffmanEncoding
from Huffman.huffman_decoding import HuffmanDecoding


class TestHuffmanCoding(unittest.TestCase):

    def setUp(self):
        self.h = HuffmanCoding()
        self.hm_encoding = HuffmanEncoding()
        self.text = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp "
        self.tree = self.h.create_tree(self.text)
        self.test_file_path = os.path.dirname(os.path.abspath(__file__))
        self.test_file_path += "/test_file.txt"

    def test_getting_frequencies(self):
        freqs = self.h.get_frequencies("testi tekstin pätkä")
        self.assertEqual(freqs, {
            "t": 5, "e": 2, "s": 2, "i": 2, "k": 2, "n": 1, "p": 1, "ä": 2, " ": 2
        })

    def test_create_tree(self):
        self.assertEqual(str(self.tree), "Node(C: None, L:Node(C: None, L:Node(C: i, L:None, R:None), R:Node(C: p, L:None, R:None)), R:Node(C: None, L:Node(C: e, L:None, R:None), R:Node(C: None, L:Node(C: None, L:Node(C: t, L:None, R:None), R:Node(C: None, L:Node(C:  , L:None, R:None), R:Node(C: s, L:None, R:None))), R:Node(C: a, L:None, R:None))))")

    def test_tree_to_bits(self):
        tree_bits = self.h.tree_to_bits(self.tree)
        self.assertEqual(
            tree_bits, "001011010011011100000101100101001011101000100100000101110011101100001")

    def test_bits_to_tree(self):
        tree_bits = self.h.tree_to_bits(self.tree)
        decoded_tree = self.h.bits_to_tree(tree_bits)
        self.assertEqual(str(decoded_tree), "Node(C: None, L:Node(C: None, L:Node(C: i, L:None, R:None), R:Node(C: p, L:None, R:None)), R:Node(C: None, L:Node(C: e, L:None, R:None), R:Node(C: None, L:Node(C: None, L:Node(C: t, L:None, R:None), R:Node(C: None, L:Node(C:  , L:None, R:None), R:Node(C: s, L:None, R:None))), R:Node(C: a, L:None, R:None))))")

    def test_get_char_bits(self):
        chars = self.h.get_char_bits(self.tree)
        self.assertEqual(chars, {
            "i": "00", "p": "01", "e": "10", "t": "1100", " ": "11010", "s": "11011", "a": "111"
        })

    def test_text_to_bits(self):
        text_bits = self.h.text_to_bits(self.text, self.tree)
        self.assertEqual(
            text_bits, "11111111111111111111111111111110101010101010101010101010101000000000000000000000000011011110111101111001100110011000101010101010101010101010111010")

    def test_bits_to_bytes(self):
        bit_tree = self.h.tree_to_bits(self.tree)
        tree_info_bits = "{0:016b}".format(len(bit_tree))
        encoded_bit_text = self.h.text_to_bits(self.text, self.tree)
        all_bits = tree_info_bits + bit_tree + encoded_bit_text
        bytes = self.h.bits_to_bytes(all_bits)
        self.assertEqual(
            bytes, b'\x01\x00"\x96\x9b\x82\xca]\x12\x0b\x9d\x87\xff\xff\xff\xfa\xaa\xaa\xaa\x80\x00\x007\xbd\xe6f*\xaa\xaa\xba')

    def test_get_additional_bits(self):
        count_in_bits, count = self.h.get_additional_bits("110")
        self.assertEqual(count_in_bits, "00000101")
        self.assertEqual(count, 5)

    def test_separate_bits(self):
        bits = "0000010100000000000000000010111111000111"
        tree_bits, text_bits = self.h.separate_bits(bits)
        self.assertEqual(tree_bits, "11111")
        self.assertEqual(text_bits, "000111")

    def test_bits_to_text(self):
        bits = "11111111111111111111111111111110101010101010101010101010101000000000000000000000000011011110111101111001100110011000101010101010101010101010111010"
        tree = self.h.create_tree(self.text)
        decoded_text = self.h.bits_to_text(bits, tree)
        self.assertEqual(
            decoded_text, self.text)

    def test_huffman_encode(self):
        encoded_file_path = self.hm_encoding.encode(self.test_file_path)
        includes = True if "src/Huffman/tests/test_file_hm.bin" in encoded_file_path else False
        self.assertEqual(True, includes)

    def test_huffman_decode(self):
        hm_decoding = HuffmanDecoding()
        encoded_file_path = self.hm_encoding.encode(self.test_file_path)
        decoded_file_path = hm_decoding.decode(encoded_file_path)
        includes = True if "src/Huffman/tests/test_file.txt" in decoded_file_path else False
        self.assertEqual(True, includes)
