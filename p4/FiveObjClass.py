class FiveObjClass:
    
    __classSum = 0
    
    def __new__(cls, *args, **kwargs):
        if cls.__classSum <= 5:
            cls.__classSum += 1
            return super().__new__(cls)
        else:
            return 'cannot create a new obj of this class - out of memory' # i.e.
    