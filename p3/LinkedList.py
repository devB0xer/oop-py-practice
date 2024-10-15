

class LinkedList:

    def __init__(self, start_obj, end_obj):
        self.start = start_obj
        self.end = end_obj

    def len(self):
        obj = self.start
        count = 0 
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
            elif obj.next:
                obj = obj.next
            else:
                return 'not found'

    
    def append(self, obj):
        self.end.next = obj
        self.end = obj

    def remove(self, index):
        obj = self.start
        for obj_i in range(index):
            if index == 0:
                self.start = self.start.next
                break
            elif obj_i == (index - 1) and obj != self.end:
                if obj.next == self.end:
                    self.end = obj
                obj.next = obj.next.next
                break
            elif obj == self.end:
                print('out of range')
                break
            else:
                obj = obj.next

