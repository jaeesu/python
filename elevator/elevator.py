class node :
    def __init__(self) :
        self.rlink=0
        self.llink=0
        self.data=0

class deque :
    def __init__(self) :
        self.front=None
        self.rear=None
    def createdeque(self) -> self:
        self.front=None
        self.rear=None
        return self

    def isEmpty(self) -> int :
        if(self.front==None) :
            print("Empty!")
            return 1
        return 0
    def pushF(self, item : node.data) -> None :
        new_node=node()
        new_node.data=item
        if(self.front==None) :
            self.front = new_node
            self.rear = new_node
            new_node.rlink = None
            new_node.llink = None
        else :

    
    def pushR(self) -> None :
        print()
    
    def popF(self) -> node.data :
        print()

        return node.data
    
    def popR(self) -> node.data :

        return node.data

    def peekF(self) -> node.data :

        return node.data

    def peekR(self) -> node.data :

        return node.data
    
    def printdeque(self) -> None :
        print()
