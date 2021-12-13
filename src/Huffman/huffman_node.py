
class HuffmanNode:
    """Luokka, jota käytetään solmuina Huffmanin puumallissa
    """

    def __init__(self, char=None, freq=None, left=None, right=None):
        """Luokan kostruktori, joka luo uuden solmun.

        Args:
            char (str, optional): solmun merkki. Defaults to None.
            freq (int, optional): merkin esiintymistiheys. Defaults to None.
            left (Huffman_node, optional): solmun vasen lapsi(solmu). Defaults to None.
            right (Huffman_node, optional): solmun oikea lapsi(solmu). Defaults to None.
            prev (Huffman_node, optional): solmun vanhempi(solmu). Defaults to None.
        """
        self.char = char
        self.freq = freq
        self.left, self.right = left, right
        self.code = ""

    def set_left(self, left_node):
        """Asettaa vasemman lapsisolmun

        Args:
            left_node (Huffman_node): asetettava solmu
        """
        self.left = left_node

    def set_right(self, right_node):
        """Asettaa oikean lapsisolmun

        Args:
            right_node (Huffman_node): asetettava solmu
        """
        self.right = right_node

    def __lt__(self, other):
        """Vertailu metodi, jota käytetään minimikeossa.

        Args:
            other (Huffman_node): verrattava solmu

        Returns:
            Huffman_node: solmu, jolla on pienempi merkin esiintymistiheys
        """
        return self.freq < other.freq

    def __str__(self):
        """Muodostaa solmuista / puusta merkkijono muotoisen esityksen

        Returns:
            str: solmupuu
        """
        return "Node(C: " + str(self.char) + ", L:" + \
            str(self.left) + ", R:" + str(self.right) + ")"
