class Strategy(object):
    def algorithm(self, input_array):
        raise NotImplemented


class BubbleStrategy(Strategy):
    def algorithm(self, input_array):
        for _ in range(len(input_array) - 1):
            for n in range(len(input_array) - 1):
                if input_array[n] > input_array[n + 1]:
                    input_array[n], input_array[n + 1] = input_array[n + 1], input_array[n]
        return input_array


class MergeStrategy(Strategy):
    def algorithm(self, input_array):
        length = len(input_array)
        if length <= 1:
            return input_array
        else:
            left_part = input_array[:length // 2]
            right_part = input_array[length // 2:]
        return self.merge(self.algorithm(left_part), self.algorithm(right_part))

    def merge(self, left, right):
        res = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:] + right[j:]
        return res


class InsertionStrategy(Strategy):
    def algorithm(self, input_array):
        for i in range(1, len(input_array)):
            key = input_array[i]
            j = i - 1
            while j >= 0 and key < input_array[j]:
                input_array[j + 1] = input_array[j]
                j -= 1
                input_array[j + 1] = key
        return input_array


class Context(object):

    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, input_array):
        return self.strategy.algorithm(input_array)


if __name__ == '__main__':
    array = [10, 8, 15, 65, 23]

    if len(array) < 10:
        context = Context(InsertionStrategy())
    elif max(array) > 10:
        context = Context(MergeStrategy())
    else:
        context = Context(BubbleStrategy())

    result = context.execute_strategy(array)
    print result

