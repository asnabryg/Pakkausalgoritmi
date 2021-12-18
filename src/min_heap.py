
class MinHeap:
    """Minimikeko tietorakenne.
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa listan ja keon koon.
        """
        # lista alustetaan yhdellä arvolla
        self.list = [0]
        self.size = 0

    def move_up(self, i):
        """Siirtää solmua ylösäin keossa ja säilyttää rakenteen minimikekona.

        Args:
            i (int): koko
        """
        # toistaa, kunnes solmu on juuri tai vasemmalla puolella
        while i // 2 > 0:
            if self.list[i] < self.list[i//2]:
                # jos solmu on vähemmän, kuin vanhempi solmu; vaihda solmut keskenään
                self.list[i], self.list[i//2] = self.list[i//2], self.list[i]

            # muuttaa indeksin vanhempaan solmuun
            i = i // 2

    def push(self, node):
        """Lisää solmun minimikekoon.

        Args:
            node: lisättävä solmu
        """
        # lisää solmu listaan
        self.list.append(node)

        # lisää keon kokoa
        self.size += 1

        # siirtää viimeisintä somua ylöspäin
        self.move_up(self.size)

    def move_down(self, i):
        """Siirtää solmua alaspäin ja säilyttää rakenteen minimikekona.

        Args:
            i (int): solmun indeksi listassa
        """
        # toistaa, kunnes nykyisellä solmulla ei ole lapsia
        while (i * 2) <= self.size:
            # pienimmän lapsen indeksi
            min_child = self.get_min_child(i)

            if self.list[i] > self.list[min_child]:
                # jos nykynen solmu on suurempi kuin pienin lapsi; vaihda solmut keskenään
                self.list[i], self.list[min_child] = self.list[min_child], self.list[i]
            i = min_child

    def get_min_child(self, i):
        """Palauttaa pienimmän lapsen.

        Args:
            i (int): solmun indeksi, jonka lapsia verrataan

        Returns:
            int: pienimmän lapsi solmun indeksi
        """
        if (i * 2) + 1 > self.size:
            # palauttaa solmun ainoan lapsen
            return i * 2
            # palauttaa pienimmän lapsen
        if self.list[i*2] < self.list[(i*2)+1]:
            return i * 2
        return (i * 2) + 1

    def pop(self):
        """Poistaa ja palauttaa pienimmän solmun keosta.

        Returns:
            node: pienin solmu
        """
        # jos keko tyhjä
        if len(self.list) == 1:
            print("EMPTY HEAP")
            return None

        # keon juuri / pienin solmu
        root = self.list[1]

        # siirtää viimeisimmän lisätyn solmun keon juureksi
        # ja poistaa sen listan lopusta
        self.list[1] = self.list[self.size]
        self.list.pop()

        # vähennä keon kokoa
        self.size -= 1

        # siirtää juurisolmua alaspäin
        self.move_down(1)

        # palauttaa pienimmän solmun
        return root
