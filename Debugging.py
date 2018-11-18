
class SumRatio:
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def get_ratio_sum(self):

        return sum(self.x)/sum(self.y)

    def get_ratio_elementwise(self):

        num_of_elements = len(self.x)

        sum = 0
        for i in range(1, num_of_elements):
            sum += self.x[i]/self.y[i]

        return sum


x = [1, 2, 3]
y = [-1, 4, 1]

sum_ratio = SumRatio(x=x, y=y)
print(sum_ratio.get_ratio_sum())
print(sum_ratio.get_ratio_elementwise())