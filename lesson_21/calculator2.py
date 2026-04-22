class Calculator2:

    @staticmethod
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        return num * Calculator2.factorial(num - 1)

    @staticmethod
    def pi():
        return 22/7
