class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def add_and_multiply(self, a, b, c):
        # Adds a + b, then multiplies result by c
        sum_result = self.add(a, b)
        return self.multiply(sum_result, c)
    
    def show_info(self):
        info = "This is a really dumb example code, in order to demostrate that i can setup Github Actions!"
        return info
