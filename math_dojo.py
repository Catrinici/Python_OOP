class MathDojo(object):
    def __init__(self,*args):
        self.result = 0

    def add(self, *args):
    # *args can take multiple arguments into one parameter
        for val in args:
            if type(val) == list or type(val) == tuple:
                for i in val:
                    self.result += i
            else:
                self.result += val
        
        print(self.result)
        return self

    def subtract(self, *args):
        for val in args:
            if type(val) == list or type(val) == tuple:
                for i in val:
                    self.result -= i
            else:
                self.result -= val
        print(self.result)
        return self

md = MathDojo()
# instance called md
md.add(2).add(2, 5).subtract(3, 2).result
# .result does not take parameters
md.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result
