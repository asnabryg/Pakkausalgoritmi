from Huffman.huffman_node import Huffman_node as Node
from heapq import heapify, heappush, heappop

class Huffman_coding:

    def __init__(self):
        pass

    def get_frequencies(self, text):
        freqs = {}
        for char in text:
            if char not in freqs:
                freqs[char] = 0
            freqs[char] += 1
        return freqs
    
    def get_tree(self, text):
        # hae kirjainten lukumäärät
        freqs = self.get_frequencies(text)

        # lisää minimikekoon kirjaimet ja niiden lukumäärät
        heap = []
        heapify(heap)
        for char, freq in freqs.items():
            heappush(heap, Node(char, freq))

        # kokoa puu alkaen pienimmästä solmusta
        while len(heap) != 1:
            left_node = heappop(heap)
            right_node = heappop(heap)
            heappush(heap, Node(
                char = None,
                freq = left_node.freq + right_node.freq,
                left = left_node,
                right = right_node
            ))

        # palauta puu
        return heappop(heap)
    
    def tree_to_bits(self, tree):
        global bits
        bits = ""

        def recursion(node):
            global bits
            if node.left is None and node.right is None:
                bits += "1" + "{0:08b}".format(ord(node.char))
            else:
                bits += "0"
                recursion(node.left)
                recursion(node.right)
            return bits
        
        return recursion(tree)
    
    def bits_to_tree(self, bits):
        i = 1
        start_node = Node()
        old_node = start_node
        while i < len(bits):
            if bits[i] == "0":
                new_node = Node(prev=old_node)
                if old_node.left is None:
                    old_node.set_left(new_node)
                    old_node = new_node
                elif old_node.right is None:
                    old_node.set_right(new_node)
                    old_node = new_node
                else:
                    old_node = old_node.prev
                    i -= 1
            elif bits[i] == "1":
                char = chr(int(bits[i+1: i+9], 2))
                i += 8
                new_node = Node(char=char, prev=old_node)
                if old_node.left is None:
                    old_node.set_left(new_node)
                elif old_node.right is None:
                    old_node.set_right(new_node)
                else:
                    old_node = old_node.prev
                    i -= 9
            i += 1
        return start_node
    
    def get_char_bits(self, tree):
        global char_bits
        char_bits = {}

        def recursion(node, bits=""):
            global char_bits
            if node is None:
                return
            if node.char is not None:
                char_bits[node.char] = bits

            recursion(node.left, bits + "0")
            recursion(node.right, bits + "1")

        recursion(tree)

        return char_bits
    
    def text_to_bits(self, text, tree):
        char_bits = self.get_char_bits(tree)
        bits = ""
        for char in text:
            bits += char_bits[char]
        return bits
