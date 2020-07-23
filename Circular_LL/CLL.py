class node :
    def __init__(self,data):
        self.data = data 
        self.next = None 
    
class CLL:
    def __init__(self):
        self.head = None 
        
    def append(self,data):
        newnode = node(data)

        if self.head == None :
            self.head = newnode 
            newnode.next = self.head 
            return 
        
        currnode = self.head 
        # print(newnode.data, "newnode")
        while currnode.next != self.head:
            
            currnode = currnode.next 
        
        currnode.next = newnode
        newnode.next = self.head
        # print(currnode.data,"currnode. data")0
        # print(currnode.next.data, 'currnode next data')
    
    def traverse(self):
        currnode = self.head.next 
        print(self.head.data)
        while currnode!=self.head :
            print(currnode.data)
            currnode = currnode.next
        
a = CLL()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.traverse()

        
