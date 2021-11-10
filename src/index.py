from Huffman.huffman_coding import Huffman_coding


def main():
    huffman = Huffman_coding()
    text = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiisssttttppppppppppppp "
    tree = huffman.get_tree(text)
    print(tree)
    print()
    bits = huffman.tree_to_bits(tree)
    print(bits)
    print()
    new_tree = huffman.bits_to_tree(bits)
    print(new_tree)
    print()
    og_bit_text = toBits(text)
    print("orginal text in bits: " + og_bit_text)
    print()
    encoded_bit_text = bits + huffman.text_to_bits(text, tree)
    print("encoded text in bits: " + encoded_bit_text)
    print()
    print("size different:", (1 - float(len(encoded_bit_text) / len(og_bit_text))) * 100, "% smaller")


def toBits(s):
    result = ""
    for c in s:
        bits = bin(ord(c))[2:]
        bits = "00000000"[len(bits):] + bits
        result += bits
    return result


if __name__ == '__main__':
    main()
