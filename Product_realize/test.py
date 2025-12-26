# class A():
#     def __init__(self, a, b):
#         self.a = a 
#         self.b = b
#         c = 3

#         print(self.a)
#         print(self.b)

# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         # print(self.a)
    
# application = A(1, 2)

# b = B(3, 4)

li = ['a', 'b', 'c']
dict = {}

class A():
    def __init__(self, li, dict):
        self.li = li
        self.dict = dict
        
        count = 0

        for i in self.li:
            self.dict[i] = count
            count += 1
        
        self.value_print()
    
    def value_print(self):
        print(self.dict[self.li[2]])
        Wait.speak()

class B(A):
    def __init__(self, li, dict, price):
        print(self.dict['b'])
    
    

class Wait():
    def speak():
        print('wait!')

price = 10

b = B(li, dict, price)