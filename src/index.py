from Huffman.huffman_encoding import HuffmanEncoding
from Huffman.huffman_decoding import HuffmanDecoding


def main():

    print()
    print("TIEDOSTON PAKKAUS/PURKU")
    while True:
        print()
        print("Komennot:")
        print("  1. Pakkaa tiedosto")
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
            print()
            try:
                file_path = input("Syötä tiedoston polku: ")
                h_encoding = HuffmanEncoding()
                encoded_file_path = h_encoding.encode(file_path)
                print("...")
                print("Tiedosto pakattu polkuun: " + encoded_file_path)
                break
            except:
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
            print()
            try:
                file_path = input("Syötä tiedoston polku: ")
                h_decoding = HuffmanDecoding()
                decoded_file_path = h_decoding.decode(file_path)
                print("...")
                print("Tiedosto purettu polkuun: " + decoded_file_path)
                break
            except:
                print("Virheellinen polku tai tiedosto.")
                print()
        elif cmd == "2":
            # LZ
            pass
        else:
            print("Virheellinen syöte")
            print()


if __name__ == '__main__':
    main()
