import os
from Huffman.huffman_coding import HuffmanCoding
from Huffman.huffman_encoding import HuffmanEncoding
from Huffman.huffman_decoding import HuffmanDecoding
from LZW.lzw_encoding import LzwEncoding
from LZW.lzw_decoding import LzwDecoding


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


def encoding():
    print()
    while True:
        print("Valitse pakkausmenetelmä:")
        print("  1. Huffman")
        print("  2. Lempel Ziv Welch")
        cmd = input("> ")
        file_path = input("Syötä tiedoston polku: ")
        if cmd == "1":
            # Huffmann
            print()
            try:
                h_encoding = HuffmanEncoding()
                og_size = os.path.getsize(file_path)
                encoded_file_path = h_encoding.encode(file_path)
                encoded_size = os.path.getsize(encoded_file_path)
                precent = round((1 - encoded_size / og_size) * 100, 2)
                print("...")
                print("Tiedosto pakattu polkuun: " + encoded_file_path)
                print("Pakattutiedosto n. " + str(precent) + " % pienempi.")
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
                print()
        elif cmd == "2":
            # LZW
            print()
            try:
                lzw_encoding = LzwEncoding()
                og_size = os.path.getsize(file_path)
                encoded_file_path = lzw_encoding.encode(file_path)
                encoded_size = os.path.getsize(encoded_file_path)
                precent = round((1 - encoded_size / og_size) * 100, 2)
                print("...")
                print("Tiedosto pakattu polkuun: " + encoded_file_path)
                print("Pakattutiedosto n. " + str(precent) + " % pienempi.")
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
                print()
        else:
            print("Virheellinen syöte.")
            print()


def decoding():
    print()
    while True:
        print("Valitse purkumenetelmä:")
        print("  1. Huffman")
        print("  2. Lempel Ziv Welch")
        cmd = input("> ")
        file_path = input("Syötä tiedoston polku: ")
        if cmd == "1":
            # Huffman
            print()
            try:
                h_decoding = HuffmanDecoding()
                decoded_file_path = h_decoding.decode(file_path)
                print("...")
                print("Tiedosto purettu polkuun: " + decoded_file_path)
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
            except (ValueError, AttributeError):
                print("Virheellinen tiedosto.")
            print()
        elif cmd == "2":
            # LZW
            print()
            try:
                lzw_decoding = LzwDecoding()
                decoded_file_path = lzw_decoding.decode(file_path)
                print("...")
                print("Tiedosto purettu polkuun: " + decoded_file_path)
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
            except ValueError:
                print("Virheellinen tiedosto.")
            print()
        else:
            print("Virheellinen syöte.")
            print()


# def test():
#     text = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp"
#     h = HuffmanCoding()
#     tree = h.create_tree(text)
#     bits = h.tree_to_bits(tree)
#     tree_old = h.bits_to_tree(bits)
#     tree_new = h.bits_to_tree_new(bits)
#     print(str(tree_old) == str(tree_new))
#     print()
#     print(tree_old)
#     print()
#     print(tree_new)


if __name__ == '__main__':
    main()
    # test()
