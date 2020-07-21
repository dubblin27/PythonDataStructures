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
    
    def Push_Mid(self,data,aft_data):
        newnode = node(data)
        currnode = self.head
        while currnode != None:
            if currnode.data == aft_data:
                break
            currnode = currnode.next
        # print(currnode.data)
        newnode.next = currnode.next 
        currnode.next = newnode
        # print(newnode.next.data)
        newnode.prev = currnode
        # print(newnode.data)
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

while True:
    print("enter option :\n 1.Push_start\n 2.Push_Mid\n 3.Push_End\n 4.Print \n 9.Break")
    opt = int(input("enter option : "))
    if opt == 1:
        data = int(input("Enter data : "))
        a.Push_start(data)
    elif opt == 2:
        data = int(input("enter data : "))
        prev_node = int(input("enter previous node : "))
        a.Push_Mid(data,prev_node)
    elif opt == 3:
        data = int(input("enter data : "))
        a.Push_End(data)
    elif opt == 4:\
        a.print()
    elif opt == 9:
        break


# a.Push_start(1)
# a.Push_start(2)
# a.Push_start(3)
# a.Push_End(4)
# a.print()