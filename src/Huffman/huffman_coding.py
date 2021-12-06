from Huffman.huffman_node import HuffmanNode as Node
from min_heap import MinHeap


class HuffmanCoding:
    """Luokka, jossa on kaikki Huffman koodaukseen tarvittavat metodit.
    """

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
        # heap = []
        # heapify(heap)
        heap = MinHeap()
        for char, freq in freqs.items():
            heap.push(Node(char, freq))

        # kokoa puu alkaen pienimmästä solmusta
        while heap.size != 1:
            left_node = heap.pop()
            right_node = heap.pop()
            heap.push(Node(
                char=None,
                freq=left_node.freq + right_node.freq,
                left=left_node,
                right=right_node
            ))

        # palauta puu
        return heap.pop()

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

        # juuri solmu
        start_node = Node()

        # viimisimmät solmut, joihin voidaan lisätä lapsia
        stack = [start_node]

        i = 1
        while i < len(bits):
            # viimeisin solmu, johon voi lisätä lapsia
            last = stack[-1]

            if bits[i] == "0":
                # luo uuden merkittömän solmun
                new_node = Node()

                # uusi solmu lisätään pinosta viimeisimmän lapseksi
                # ensin aina vasemmaksi
                if last.left is None:
                    last.set_left(new_node)

                    # lisätään pinoon uusi solmu
                    stack.append(new_node)

                else:
                    last.set_right(new_node)

                    # poistaa viimeisimmän solmun pinosta,
                    # koska siihen ei voida enää lisätä lapsia
                    stack.pop()
                    stack.append(new_node)
            else:
                # hakee merkin bittiesityksestä
                char = chr(int(bits[i+1: i+9], 2))

                # siirrytään bittiesityksessä merkin yli
                i += 8

                # merkillinen solmu lisätään solmun lapseksi
                # ensin aina vasemmaksi solmuksi
                new_node = Node(char=char)
                if last.left is None:
                    last.set_left(new_node)

                else:
                    last.set_right(new_node)

                    # poistaa viimeisimmän solmun pinosta,
                    # koska siihen ei voida enää lisätä lapsia
                    stack.pop()
            i += 1

        # palauttaa puumallin juuri solmun
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
        """Luo uuden bittiesityksen pakattavasta tekstistä.

        Args:
            text (str): pakattavateksti
            tree ([type]): [description]

        Returns:
            [type]: [description]
        """
        char_bits = self.get_char_bits(tree)
        bits = ""
        for char in text:
            bits += char_bits[char]
        return bits

    def separate_bits(self, bits):
        """Erottaa puun ja tekstin bittiesityksen biteistä ja palauttaa ne

        Args:
            bits (str): bittiesitys

        Returns:
            tuple(str, str): puu ja teksti bittiesitykset
        """
        # poistetaan extra bitit
        extra_bits_count = int(bits[:8], 2)
        bits = bits[8 + extra_bits_count:]

        # poistetaan puubittien määrä biteistä
        tree_bits_count = int(bits[:16], 2)
        bits = bits[16:]

        # erotellaan puu- ja tekstibitit
        tree_bits = bits[:tree_bits_count]
        text_bits = bits[tree_bits_count:]

        return tree_bits, text_bits

    def bits_to_text(self, text_bits, tree):
        """Kääntää tekstin bittiesityksen alkuperäiseksi tekstiksi.

        Args:
            text_bits (str): tekstin bittiesitys
            tree (Huffman_node): puun aloitus solmu

        Returns:
            str: alkuperäinen teksti
        """
        text = ""
        node = tree
        for bit in text_bits:
            node = node.left if bit == "0" else node.right
            if node.left is None and node.right is None:
                text += node.char
                node = tree
        return text
