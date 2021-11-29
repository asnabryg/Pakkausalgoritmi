import os
import unittest
from LZW.lzw_coding import LzwCoding
from LZW.lzw_encoding import LzwEncoding
from LZW.lzw_decoding import LzwDecoding
from bit_conversion import bits_to_bytes, bytes_to_bits


class TestLempelZivWelchCoding(unittest.TestCase):

    def setUp(self):
        self.lzw = LzwCoding()
        self.lzw_encoding = LzwEncoding()
        self.text = "ttthisistheeestitthe"
        self.output = self.lzw.create_output(self.text)
        self.test_file_path = os.path.dirname(os.path.abspath(__file__))
        self.test_file_path += "/test_file.txt"

    def test_create_output(self):
        self.assertEqual(self.output, [116, 256, 104, 105, 115,
                         259, 116, 104, 101, 264, 115, 116, 105, 257, 101])

    def test_output_to_bits(self):
        bits = self.lzw.output_to_bits(self.output)
        self.assertEqual(
            bits, "00001001001110100100000000001101000001101001001110011100000011001110100001101000001100101100001000001110011001110100001101001100000001001100101")

    def test_bits_to_output(self):
        bits = self.lzw.output_to_bits(self.output)
        in_bytes = bits_to_bytes(bits)
        bits = bytes_to_bits(in_bytes)
        output = self.lzw.bits_to_output(bits)
        self.assertEqual(output, self.output)

    def test_output_to_text(self):
        text = self.lzw.output_to_text(self.output)
        self.assertEqual(text, self.text)

    def test_lzw_encode(self):
        encoded_file_path = self.lzw_encoding.encode(self.test_file_path)
        includes = True if "src/LZW/tests/test_file_lzw.bin" in encoded_file_path else False
        self.assertEqual(True, includes)

    def test_lzw_decoding(self):
        lzw_decoding = LzwDecoding()
        encoded_file_path = self.lzw_encoding.encode(self.test_file_path)
        decoded_file_path = lzw_decoding.decode(encoded_file_path)
        includes = True if "src/LZW/tests/test_file_decoded.txt" in decoded_file_path else False
        self.assertEqual(True, includes)
        with open(decoded_file_path, "r", encoding="utf-8") as file:
            text = file.read()
            self.assertEqual(self.text, text)
