import unittest
from Huffman.huffman_coding import Huffman_coding

class TestHuffman_coding(unittest.TestCase):

    def setUp(self):
        self.h = Huffman_coding()
    
    def test_getting_frequencies(self):
        freqs = self.h.get_frequencies("testi tekstin pätkä")
        self.assertEqual(freqs, {
            "t": 5, "e": 2, "s": 2, "i": 2, "k": 2, "n": 1, "p": 1, "ä": 2, " ": 2
        })
    
    def test_create_tree(self):
        tree = self.h.create_tree(
            "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp ")
        self.assertEqual(str(tree), "Node(C: None, L:Node(C: None, L:Node(C: i, L:None, R:None), R:Node(C: p, L:None, R:None)), R:Node(C: None, L:Node(C: e, L:None, R:None), R:Node(C: None, L:Node(C: None, L:Node(C: t, L:None, R:None), R:Node(C: None, L:Node(C:  , L:None, R:None), R:Node(C: s, L:None, R:None))), R:Node(C: a, L:None, R:None))))")
        
    def test_tree_to_bits(self):
        tree = self.h.create_tree(
            "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp ")
        tree_bits = self.h.tree_to_bits(tree)
        self.assertEqual(
            tree_bits, "001011010011011100000101100101001011101000100100000101110011101100001")
    
    def test_bits_to_tree(self):
        tree = self.h.create_tree(
            "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp ")
        tree_bits = self.h.tree_to_bits(tree)
        decoded_tree = self.h.bits_to_tree(tree_bits)
        self.assertEqual(str(decoded_tree), "Node(C: None, L:Node(C: None, L:Node(C: i, L:None, R:None), R:Node(C: p, L:None, R:None)), R:Node(C: None, L:Node(C: e, L:None, R:None), R:Node(C: None, L:Node(C: None, L:Node(C: t, L:None, R:None), R:Node(C: None, L:Node(C:  , L:None, R:None), R:Node(C: s, L:None, R:None))), R:Node(C: a, L:None, R:None))))")

    def test_get_char_bits(self):
        tree = self.h.create_tree(
            "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp ")
        chars = self.h.get_char_bits(tree)
        self.assertEqual(chars, {
            "i": "00", "p": "01", "e": "10", "t": "1100", " ": "11010", "s": "11011", "a": "111"
        })
    
    def test_text_to_bits(self):
        text = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp "
        tree = self.h.create_tree(text)
        text_bits = self.h.text_to_bits(text, tree)
        self.assertEqual(
            text_bits, "11111111111111111111111111111110101010101010101010101010101000000000000000000000000011011110111101111001100110011000101010101010101010101010111010")

    def test_bits_to_bytes(self):
        text = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp "
        tree = self.h.create_tree(text)
        bit_tree = self.h.tree_to_bits(tree)
        tree_info_bits = "{0:016b}".format(len(bit_tree))
        encoded_bit_text = self.h.text_to_bits(text, tree)
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
        text = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp "
        bits = "11111111111111111111111111111110101010101010101010101010101000000000000000000000000011011110111101111001100110011000101010101010101010101010111010"
        tree = self.h.create_tree(text)
        decoded_text = self.h.bits_to_text(bits, tree)
        self.assertEqual(
            decoded_text, text)
