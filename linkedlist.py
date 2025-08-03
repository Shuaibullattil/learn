class Node:
    def __init__(self,data):
        self.data = data
        self.Next = None
class LinkedList:
    def __init__(self):
        self.Head = None
    
    # def insert(self,data):

    #     new_node = Node(data)

    #     if self.Head is None:
    #         self.Head = new_node
    #         return
        
    #     current = self.Head
    #     while current.Next:
    #         current  = current.Next
    #     current.Next = new_node
    #     return

    def insert(self,data):

        new_node = Node(data)

        if self.Head is None or data >= self.Head.data:
            new_node.Next = self.Head
            self.Head = new_node
            return
        current = self.Head
        while current.Next and current.Next.data >= new_node.data:
            current = current.Next
        new_node.Next = current.Next
        current.Next = new_node
        return
    
    def display(self):
        current = self.Head
        while current:
            print(f"{current.data} ->" ,end=" ")
            current = current.Next
        print("None")

nums = [34,70,20,300,200,100,600]
l1 = LinkedList()
for i in nums:
    l1.insert(i)
    print(f"inserted {i}")
l1.display()