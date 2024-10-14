

class LinkedList:

    def __init__(self, start_obj, end_obj):
        self.start = start_obj
        self.end = end_obj

    def len(self):
        obj = self.start
        count = 0 # [iter:count] 1:1 2:2
        while True:
            count += 1
            if obj == self.end:
                break
            obj = obj.next
        return count
    
    def search(self, data):
        obj = self.start
        while True:
            if obj.data == data:
                return obj
            else:
                obj = obj.next

    
    def append(self, obj):
        pass
    def remove(self, index):
        pass
