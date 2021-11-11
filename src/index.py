from Huffman.huffman_coding import Huffman_coding
from Huffman.huffman_encoding import Huffman_encoding
from Huffman.huffman_decoding import Huffman_decoding


def main():
    h_encoding = Huffman_encoding()
    file_path = "/home/asnabryg/tiralab/test_file.txt"
    h_encoding.encode(file_path)

    h_decoding = Huffman_decoding()
    file_path = "/home/asnabryg/tiralab/test_file_encoded.bin"
    h_decoding.decode(file_path)
    


if __name__ == '__main__':
    main()
