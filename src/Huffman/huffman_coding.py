from Huffman.huffman_node import Huffman_node as Node
from heapq import heapify, heappush, heappop
import pathlib

class Huffman_coding:
    """Luokka, jossa on kaikki Huffman koodaukseen tarvittavat metodit.
    """

    def __init__(self):
        pass

    def get_frequencies(self, text):
        """Luo sanakirjan, jossa on tekstin merkkien lukumäärät.

        Args:
            text (str): pakattava teksti

        Returns:
            sanakirja: valmis sanakirja
        """
        freqs = {}
        for char in text:
            if char not in freqs:
                freqs[char] = 0
            freqs[char] += 1
        return freqs
    
    def create_tree(self, text):
        """Luo Huffman puumallin

        Args:
            text (str): pakattava teksti

        Returns:
            [Huffman_node]: puun aloitus solmu
        """
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
        """ Koodaa puun bittiesityksen

        Args:
            tree (Huffman_node): puun aloitus solmu

        Returns:
            str: puu koodattuna bitteihin merkkijonona
        """
        global bits
        bits = ""

        def recursion(node):
            global bits
            if node.left is None and node.right is None:
                # bitti 1:n oikealla puolella seuraavat 8 bittiä kertoo mikä merkki kyseessä
                bits += "1" + "{0:08b}".format(ord(node.char))
            else:
                # bitti 0:n oikealla puolella on solmun lapset
                bits += "0"
                recursion(node.left)
                recursion(node.right)
            return bits
        
        return recursion(tree)
    
    def bits_to_tree(self, bits):
        """Luo puumallin bittiesityksestä

        Args:
            bits (str): bitit merkkijonona

        Returns:
            Huffman_node: puun aloitus solmu
        """
        i = 1
        start_node = Node()
        current_node = start_node
        while i < len(bits):
            if bits[i] == "0":
                # luo nykyiselle solmulle uuden merkittömän lapsen
                # ja nykyinen solmu muuttuu seuraavaksi solmuksi
                new_node = Node(prev=current_node)
                if current_node.left is None:
                    current_node.set_left(new_node)
                    current_node = new_node
                elif current_node.right is None:
                    current_node.set_right(new_node)
                    current_node = new_node
                else:
                    # jos haara jo käyty läpi, mennään bittiesityksessä taaksepäin,
                    # että löytyy solmu, jonka läpikäynti jäi kesken,
                    # ja nykyinen solmu muuttuu solmun vanhemmaksi
                    current_node = current_node.prev
                    i -= 1
            elif bits[i] == "1":
                # haetaan merkki bittiesityksestä
                char = chr(int(bits[i+1: i+9], 2))
                # siirytään bittiesityksessä merkin yli
                i += 8
                # merkillinen solmu lisätään nykyisen solmun lapseksi
                # ensin aina vasemmaksi solmuksi
                new_node = Node(char=char, prev=current_node)
                if current_node.left is None:
                    current_node.set_left(new_node)
                elif current_node.right is None:
                    current_node.set_right(new_node)
                else:
                    # jos haara jo käyty läpi, mennään bittiesityksessä taaksepäin,
                    # että löytyy solmu, jonka läpikäynti jäi kesken,
                    # ja nykyinen solmu muuttuu solmun vanhemmaksi
                    current_node = current_node.prev
                    i -= 9
            # mennään bitti esityksessä yksi eteenpäin
            i += 1
        
        # palauttaa puumallin aloitus solmun
        return start_node
    
    def get_char_bits(self, tree):
        """Luo sanakirjan, jossa on merkkien uusi pakattu bittiesitys

        Args:
            tree (Huffman_node): puun aloitus solmu

        Returns:
            sanakirja: merkkien pakatut bittiesitykset
        """
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
    
    def save_to_file(self, bytes):
        with open("huffman.bin", "wb") as f:
            f.write(bytes)
    
    def bits_to_bytes(self, bits):
        bytes = bytearray()
        for i in range(0, len(bits), 8):
            byte = (bits[i:i+8])
            bytes.append(int(byte, 2))
        return bytes
