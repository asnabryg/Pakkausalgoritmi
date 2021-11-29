import unittest
from bit_conversion import bits_to_bytes, bytes_to_bits, get_additional_bits


class TestBitConversion(unittest.TestCase):

    def test_bits_to_bytes(self):
        bits = "10001010001110100100011101011010"
        bytes = bits_to_bytes(bits)
        self.assertEqual(
            bytes, b'\x08\x00\x8a:GZ')

    def test_get_additional_bits(self):
        additional_bits = get_additional_bits("110")
        self.assertEqual(additional_bits, "0000010100000")

    def test_bytes_to_bits(self):
        in_bytes = b'\x08\x00\x8a:GZ'
        bits = bytes_to_bits(in_bytes)
        self.assertEqual(bits, "0000100000000000" +
                         "10001010001110100100011101011010")
