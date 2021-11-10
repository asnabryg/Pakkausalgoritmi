from Huffman.huffman_coding import Huffman_coding

def main():
    huffman = Huffman_coding()
    tree = huffman.get_tree("aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp ")
    print(tree)
    print()
    bits = huffman.tree_to_bits(tree)
    print(bits)
    print()
    print(huffman.bits_to_tree(bits))


if __name__ == '__main__':
    main()
    