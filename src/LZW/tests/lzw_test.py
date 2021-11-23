import os
import unittest
from LZW.lzw_coding import LzwCoding


class TestLempelZivWelchCoding(unittest.TestCase):

    def setUp(self):
        self.lzw = LzwCoding()
        self.text = "ttthisistheeestitthe"
        self.output = self.lzw.create_output(self.text)

    def test_create_output(self):
        self.assertEqual(self.output, [116, 256, 104, 105, 115,
                         259, 116, 104, 101, 264, 115, 116, 105, 257, 101])

    def test_output_to_bits(self):
        bits = self.lzw.output_to_bits(self.output)
        self.assertEqual(
            bits, "00001001001110100100000000001101000001101001001110011100000011001110100001101000001100101100001000001110011001110100001101001100000001001100101")
    
    def test_bits_to_output(self):
        bits = self.lzw.output_to_bits(self.output)
        in_bytes = self.lzw.bits_to_bytes(bits)
        bits = ""
        for byte in in_bytes:
            bits += bin(byte)[2:].rjust(8, "0")
        output = self.lzw.bits_to_output(bits)
        self.assertEqual(output, self.output)
    
    def test_output_to_text(self):
        text = self.lzw.output_to_text(self.output)
        self.assertEqual(text, self.text)
