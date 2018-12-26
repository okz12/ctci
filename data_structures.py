class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self, from_list = None):
        if(from_list and from_list != []):
            self.head = curr = ListNode(from_list[0])
            for val in from_list[1:]:
                curr.next = ListNode(val)
                curr = curr.next
        else:
            self.head = None
        
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next
            
    def as_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
    
    def get_len(self):
        curr = self.head
        c=1
        while(curr.next):
            curr = curr.next
            c+=1
        return c, curr
    
class Queue:
    def __init__(self):
        self.queuelist = []
        
    def pop(self):
        if self.queuelist != []:
            return self.queuelist.pop(0)
        return None
    
    def push(self, item):
        self.queuelist.append(item)
        
    def peek(self):
        return self.queuelist[0]
    
    def isEmpty(self):
        return self.queuelist == []
    
    
#pop push peek isEmpty
class Stack:
    def __init__(self):
        self.stacklist = []
        
    def pop(self):
        if self.stacklist != []:
            return self.stacklist.pop()
        return None
    
    def push(self, item):
        self.stacklist.append(item)
        
    def peek(self):
        return self.stacklist[-1]
    
    def isEmpty(self):
        return self.stacklist == []