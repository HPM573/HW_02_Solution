import warnings
import math


class SumRatio:
    def __init__(self, x, y):
        """
        :param x: (list) of numbers
        :param y: (list) of numbers
        """

        if len(x) != len(y):
            raise ValueError('x and y should have the same number of elements.')

        self.x = x
        self.y = y

    def get_sum_ratio(self):
        """
        :return: x_1/y_1 + x_2+y_2 + ...
        """

        # number of ratios to calculate
        num_of_elements = len(self.x)

        # sum all ratios
        sum = 0
        for i in range(0, num_of_elements):
            try:
                sum += self.x[i]/self.y[i]
            except:
                warnings.warn('Division by 0 in calculating the ratio in position ' + str(i))
                return math.nan

        return sum


# test 1:
def test1():
    x = [1, 2, 3]
    y = [2, 4, 1]
    correct_sum_ratio = 1/2 + 2/4 + 3/1

    # calculate the sum of ratios
    sum_ratio = SumRatio(x=x, y=y)
    result = sum_ratio.get_sum_ratio()

    if result == correct_sum_ratio:
        print('Test 1 passed.')
    else:
        print('Test 1 failed. Calculated sum of ratios: ', result, 'Correct sum of ratios: ', correct_sum_ratio)


# test 2:
def test2():
    x = [1, 2, 3]
    y = [2, 4]

    # calculate the sum of ratios
    sum_ratio = SumRatio(x=x, y=y)
    result = sum_ratio.get_sum_ratio()
    print(result)


# test 3:
def test3():
    x = [1, 2, 3]
    y = [2, 0, 1]
    correct_sum_ratio = math.nan

    # calculate the sum of ratios
    sum_ratio = SumRatio(x=x, y=y)
    result = sum_ratio.get_sum_ratio()

    if result is correct_sum_ratio:
        print('Test 2 passed.')
    else:
        print('Test 2 failed. Calculated sum of ratios: ', result, 'Correct sum of ratios: ', correct_sum_ratio)


# running the tests
test1()
test3()
test2()
