from types import NoneType


class Node:
    def __init__(self, value, prev=None, nxt=None) -> None:
        self.value = value
        self.prev = prev
        self.nxt = nxt
    
    def update_neighbors(self, follow=False, precede=False):
        if isinstance(follow, (Node, NoneType)):
            self.prev = follow
        if isinstance(precede, (Node, NoneType)):
            self.nxt = precede
    
    def check_pos(self):
        if self.prev == self.nxt == None:
            return None
        elif self.prev == None:
            return True
        elif self.nxt == None:
            return False
        else:
            return -1