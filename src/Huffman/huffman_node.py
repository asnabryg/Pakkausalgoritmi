
class Huffman_node:
    
    def __init__(self, char=None, freq=None, left=None, right=None, prev=None):
        self.char = char
        self.freq = freq
        self.left, self.right = left, right
        self.prev = prev
        self.code = ""
    
    def set_char(self, char):
        self.char = char
    
    def set_left(self, left_node):
        self.left = left_node
    
    def set_right(self, right_node):
        self.right = right_node
    
    def set_prev(self, previous_node):
        self.prev = previous_node
    
    def __lt__(self, other):
        return self.freq < other.freq
    
    def __str__(self):
        return "Node(C: " + str(self.char) + ", L:"+ str(self.left) + ", R:" +  str(self.right) + ")"
