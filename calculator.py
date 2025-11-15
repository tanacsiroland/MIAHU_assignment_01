class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def add_and_multiply(self, a, b, c):
        # Adds a + b, then multiplies result by c
        sum_result = self.add(a, b)
        return self.multiply(sum_result, c)