from Huffman.huffman_node import HuffmanNode as Node
from min_heap import MinHeap
from custom_expections import EmptyFileException


class HuffmanCoding:
    """Luokka, jossa on kaikki Huffman koodaukseen tarvittavat metodit.
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa apumuuttujat char_bits ja bits.
        """
        self.char_bits = {}
        self.bits = ""

    def get_frequencies(self, text):
        """Luo sanakirjan, jossa on tekstin merkkien lukumäärät.

        Args:
            text (str): pakattava teksti

        Returns:
            sanakirja: valmis sanakirja
        """
        if text == "":
            raise EmptyFileException
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
        heap = MinHeap()
        for char, freq in freqs.items():
            heap.push(Node(char, freq))

        # kokoa puu alkaen pienimmästä solmusta
        # print("heap", heap.list)
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
        self.bits = ""

        def recursion(node):
            if node.left is None and node.right is None:
                # bitti 1:n oikealla puolella seuraavat 8 bittiä kertoo mikä merkki kyseessä
                self.bits += "1" + format(ord(node.char), "08b")
            else:
                # bitti 0:n oikealla puolella on solmun lapset
                self.bits += "0"
                recursion(node.left)
                recursion(node.right)
            return self.bits

        return recursion(tree)

    def bits_to_tree(self, bits):
        """Luo puumallin bittiesityksestä

        Args:
            bits (str): bitit merkkijonona

        Returns:
            Huffman_node: puun aloitus solmu
        """

        if len(bits) == 9:
            # kun tekstissä on vain yksi uniikki merkki
            return Node(
                char=chr(int(bits[1: 9], 2))
            )

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
        self.char_bits = {}

        def recursion(node, bits=""):
            if node is None:
                return
            if node.char is not None:
                self.char_bits[node.char] = bits

            recursion(node.left, bits + "0")
            recursion(node.right, bits + "1")

        recursion(tree)
        if len(self.char_bits) == 1:
            # kun tekstissä vain yksi uniikki kirjain
            self.char_bits = {tree.char: "0"}

        return self.char_bits

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
        if node.char is not None:
            # jos tekstissä vain yksi uniikki merkki
            return node.char * len(text_bits)

        for b in text_bits:
            node = node.left if b == "0" else node.right
            if node.left is None and node.right is None:
                text = text + node.char
                node = tree

        return text
