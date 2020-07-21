class node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
        
    def Push_start(self,data):
        newnode = node(data)
        newnode.next = self.head
        if self.head != None:
            self.head.prev = newnode
        self.head = newnode
    
    def Push_End(self,data):
        newnode = node(data)
        if self.head ==None:
            self.head = newnode
            return
        currnode = self.head
        while currnode != None:
            if currnode.next ==None:
                break
            currnode = currnode.next 
        currnode.next = newnode
    
    def print(self):
        currnode = self.head
        while currnode != None:
            print(currnode.data)
            currnode = currnode.next
a = DLL()
a.Push_start(1)
a.Push_start(2)
a.Push_start(3)
a.Push_End(4)
a.print()