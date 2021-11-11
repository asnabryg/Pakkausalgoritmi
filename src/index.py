from Huffman.huffman_coding import Huffman_coding
from Huffman.huffman_encoding import Huffman_encoding


def main():
    h = Huffman_encoding()
    file_path = "/home/asnabryg/tiralab/test_file.txt"
    h.encode(file_path)


if __name__ == '__main__':
    main()
