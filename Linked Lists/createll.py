class node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Linkedlist:

    def __init__(self):
        self.head = None


    def append_start(self,data):
        newnode = node(data)
        newnode.next = self.head
        self.head = newnode

    def append_mid(self, d,data):
        prev_node = node(d)
        x_node = self.head 
        while x_node:
            if prev_node.data == x_node.data :
                prev_node = x_node
                break 
            x_node = x_node.next
            if not prev_node:
                print("data not in the list")
                return
        newnode = node(data)
        newnode.next =prev_node.next 
        prev_node.next = newnode

    def append_last(self,data):
        newnode = node(data)

        if self.head == None:
            self.head = newnode 
            return 
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode
    

    def del_start(self):
        currnode = self.head
        self.head = currnode.next

    def del_mid(self,d):
        # print("hi")
        tofind_node = node(d)
        currnode = self.head
        dummynode = node(0)
        while currnode:
            
            xnode = currnode.next
            if xnode.data == tofind_node.data:
                # print(currnode.data, tofind_node.data)
                # currnode.next  = None
                break
            currnode = currnode.next
        print(currnode.data, tofind_node.data)

        currnode.next = tofind_node.next
        currnode.next  = dummynode
        # tofind_node.next = None

    def del_middle(self,d):
        
        currnode = self.head
        # dummynode = node(0)
        while currnode:
            if currnode.data != d:
                break
            currnode = currnode.next
        print(currnode.data)
        currnode.next = currnode.next.next
        
          
           
            
       
                

    def del_end(self):
        currnode = self.head
        while currnode:
            if currnode.next is not None:
                prevnode = currnode
            currnode = currnode.next
        prevnode.next = None

    def printll(self):
        currentnode = self.head
        count = 0
        arr = []
        while currentnode:
            count+=1
            arr.append(currentnode.data)
            currentnode = currentnode.next
        print(*arr)
        print("count:", count)
        
#main code 
ll = Linkedlist()

while True:
    print("enter option :\n1.add\n2.print\n3.break")
    op = int(input("enter the option : "))
    if op == 1:
        data = int(input("enter value to append : "))
        ll.append_last(data)
    if op == 2 :
        ll.printll()
    if op == 3:
        break
    if op == 4:
        val = int(input("enter the node: "))
        ll.del_middle(val)

