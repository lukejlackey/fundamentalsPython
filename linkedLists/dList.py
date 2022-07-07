from node import Node

class DList:
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail
    
    def check_new_end(self, n):
        if n is None:
            return
        elif n.prev is None:
            self.head = n
        elif n.nxt is None:
            self.tail = n
    
    def append_nodes(self, *new_nodes):
        nodes = list(new_nodes)
        current_node = nodes.pop(0)
        if self.head is None:
            self.head = current_node
        else:
            nodes.insert(0, current_node)
        current_node = nodes.pop(0)
        if self.tail is None:
            self.head.update_neighbors(precede=current_node)
            current_node.update_neighbors(follow=self.head)
            self.check_new_end(current_node)
        else:
            nodes.insert(0, current_node)
        for n in nodes:
            self.tail.update_neighbors(precede=n)
            n.update_neighbors(follow=self.tail)
            self.check_new_end(n)
        return self
    
    def delete_node(self, target):
        if target.check_pos() is None:
            self.head = self.tail = None
        elif target.check_pos() is True:
            target.nxt.update_neighbors(follow=target.prev)
            self.check_new_end(target.nxt)
        elif target.check_pos() is False:
            target.prev.update_neighbors(precede=target.nxt)
            self.check_new_end(target.prev)
        elif target.check_pos() is -1:
            target.prev.update_neighbors(precede=target.nxt)
            target.nxt.update_neighbors(follow=target.prev)
        del target
        return self
    
    def insert_node(self, new_node, idx=None, follow=False, precede=False):
        if isinstance(idx, int):
            h = self.head
            for i in range(idx):
                h = h.nxt
            if h is None:
                print('No such index exists. Please try again.')
                return self
            else:
                follow, precede = h.prev, h.nxt
        elif follow:
            precede = follow.nxt
        elif precede:
            follow = precede.prev
        elif not idx or follow or precede:
            print('Could not insert node due to a lack of valid arguments. Please try again.')
            return self
        new_node.update_neighbors(follow=follow, precede=precede)
        self.check_new_end(new_node)
        if new_node.check_pos() is None:
            pass
        elif new_node.check_pos() is True:
            precede.update_neighbors(follow=new_node)
        elif new_node.check_pos() is False:
            follow.update_neighbors(precede=new_node)
        else:
            follow.update_neighbors(precede=new_node)
            precede.update_neighbors(follow=new_node)
        return self
    
    def display_nodes(self):
        print('|','-'*50,'|')
        i = 0
        if self.head is not None:
            current_node = self.head
            while current_node is not None and current_node.prev is not self.tail:
                print(f'| {i}: {current_node.value}')
                current_node = current_node.nxt
                i += 1
        else:
            print('No nodes in list.')
        print('|','-'*50,'|')
        return self
