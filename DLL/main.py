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
        newnode.next = None
    
    def Pop_Start(self):
        self.head = self.head.next

    
    def Pop_Mid(self,data):
        currnode = self.head
        while currnode.data != data :
            if currnode.next.data == data:
                break
            currnode = currnode.next 
        x_node = currnode.next
        # print(currnode.data)
        # print(x_node.data)
        currnode.next = x_node.next
        
        x_node = None

    def Pop_End(self):
        currnode = self.head
        while currnode != None:
            # print(currnode.data,"currnode . data inside while")
            if currnode.next.next == None:
                break
            currnode = currnode.next 
        # print(currnode.data, "currnodedata")
        currnode.next = None 

    def print(self):
        currnode = self.head
        print("printing : ")
        while currnode != None:
            print(currnode.data)
            currnode = currnode.next
        print("printing end")

a = DLL()
while True:
    print("enter option :\n 1.Push_start\n 2.Push_Mid\n 3.Push_End\n 4. Pop_start\n 5.Pop_Mid\n 6.Pop_End\n 7.Print \n 8.Break")
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
    elif opt == 7:
        a.print()
    elif opt == 4:
        a.Pop_Start()
    elif opt == 6:
        a.Pop_End()
    elif opt == 5 :
        data =  int(input("enter data to pop : "))
        a.Pop_Mid(data)
    elif opt == 8:
        break

# a.Push_End(1)
# a.Push_End(2)
# a.Push_End(3)
# a.Push_End(4)
# a.Push_End(5)
# a.print()
# a.Pop_Mid(3)
# a.print()