import os
from Huffman.huffman_encoding import HuffmanEncoding
from Huffman.huffman_decoding import HuffmanDecoding
from LZW.lzw_encoding import LzwEncoding
from LZW.lzw_decoding import LzwDecoding
from custom_expections import EmptyFileException


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
        print("  3. edellinen")
        cmd = input("> ")
        if cmd == "3":
            break
        if cmd == "1":
            # Huffmann
            print()
            try:
                file_path = input("Syötä tiedoston polku: ")
                h_encoding = HuffmanEncoding()
                og_size, encoded_file_path = os.path.getsize(
                    file_path), h_encoding.encode(file_path)
                encoded_size = os.path.getsize(encoded_file_path)
                precent = round((1 - encoded_size / og_size) * 100, 2)
                print("...")
                print("Tiedosto pakattu polkuun: " + encoded_file_path)
                print("Pakattutiedosto n. " + str(precent) + " % pienempi.")
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
                print()
            except EmptyFileException:
                print("Tyhjä tiedosto.")
                print()
        elif cmd == "2":
            # LZW
            print()
            try:
                file_path = input("Syötä tiedoston polku: ")
                lzw_encoding = LzwEncoding()
                encoded_file_path = lzw_encoding.encode(file_path)
                og_size, encoded_size = os.path.getsize(
                    file_path), os.path.getsize(encoded_file_path)
                precent = round((1 - encoded_size / og_size) * 100, 2)
                print("...")
                print("Tiedosto pakattu polkuun: " + encoded_file_path)
                print("Pakattutiedosto n. " + str(precent) + " % pienempi.")
                break
            except FileNotFoundError:
                print("Virheellinen polku tai tiedosto.")
                print()
            except EmptyFileException:
                print("Tyhjä tiedosto.")
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
        print("  3. edellinen")
        cmd = input("> ")
        if cmd == "3":
            break
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


if __name__ == '__main__':
    main()
