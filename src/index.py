import os
from Huffman.huffman_encoding import HuffmanEncoding
from Huffman.huffman_decoding import HuffmanDecoding
from LZW.lzw_coding import LzwCoding


def main():
    print()
    print("TEKSTITIEDOSTON PAKKAUS/PURKU")
    while True:
        print()
        print("Komennot:")
        print("  1. Pakkaa tekstitiedosto")
        print("  2. Pura tiedosto")
        print("  3. Sulje ohjelma")
        cmd = input("> ")

        if cmd == "1":
            # pakkaa
            encoding()
        elif cmd == "2":
            # purkaa
            decoding()
        elif cmd == "3":
            print("Ohjelma sulkeutuu")
            break
        else:
            print("Virheellinen syöte.")
            print()

    # h_encoding = Huffman_encoding()
    # file_path = "/home/asnabryg/tiralab/text_file.txt"
    # h_encoding.encode(file_path)

    # h_decoding = Huffman_decoding()
    # file_path = "/home/asnabryg/tiralab/text_file_hm.bin"
    # h_decoding.decode(file_path)


def encoding():
    print()
    while True:
        print("Valitse pakkaus menetelmä:")
        print("  1. Huffman")
        print("  2. Lempel Ziv")
        cmd = input("> ")
        if cmd == "1":
            # Huffmann
            print()
            try:
                file_path = input("Syötä tiedoston polku: ")
                h_encoding = HuffmanEncoding()
                og_size = os.path.getsize(file_path)
                encoded_file_path = h_encoding.encode(file_path)
                encoded_size = os.path.getsize(encoded_file_path)
                precent = round((1 - encoded_size / og_size) * 100, 2)
                print("...")
                print("Tiedosto pakattu polkuun: " + encoded_file_path)
                print("Pakattutiedosto n. " + str(precent) + " % pienempi")
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
                print()
        elif cmd == "2":
            # LZ
            pass
        else:
            print("Virheellinen syöte.")
            print()


def decoding():
    print()
    while True:
        print("Valitse purku menetelmä:")
        print("  1. Huffman")
        print("  2. Lempel Ziv")
        cmd = input("> ")
        if cmd == "1":
            # Huffman
            print()
            try:
                file_path = input("Syötä tiedoston polku: ")
                h_decoding = HuffmanDecoding()
                decoded_file_path = h_decoding.decode(file_path)
                print("...")
                print("Tiedosto purettu polkuun: " + decoded_file_path)
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
                print()
        elif cmd == "2":
            # LZ
            pass
        else:
            print("Virheellinen syöte")
            print()


def test_lzw():
    lzw = LzwCoding()
    output = lzw.create_output("ttthisistheeestitthe")
    print(output)
    bits = lzw.output_to_bits(output)
    print(bits)
    in_bytes = lzw.bits_to_bytes(bits)
    print(in_bytes)

    bits = ""
    for byte in in_bytes:
        bits += bin(byte)[2:].rjust(8, "0")
    print(lzw.bits_to_output(bits))
    print(lzw.output_to_text(output))


if __name__ == '__main__':
    main()
    # test_lzw()
