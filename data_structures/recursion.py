class Recursion:
    def __init__(self):
        self.result = None

    def factorial(self, n):
        if n == 1:
            return 1
        self.result = n * self.factorial(n - 1)
        return self.result


my_rec = Recursion()
print(my_rec.factorial(5))