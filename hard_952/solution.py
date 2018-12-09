def greatest_common_factor(a, b):
    while b:
        a, b = b, a%b
    return a


class Solution:
    def largestComponentSize(self, A):
        if len(A) > 20_000:
            raise InvalidArraySizeException("Array size greater than 20000")
        for a in A:
            if a > 100_000:
                raise InvalidElementException("Element greater than 100000")
        largest_component_size = 0
        while len(A) > 0:
            largest_component = [A.pop(0)]
            for b in largest_component:
                rm_values = []
                for c in A:
                    if greatest_common_factor(b, c) > 1:
                        largest_component.append(c)
                        rm_values.append(c)
                for r in rm_values:
                    A.remove(r)
            largest_component_size = max(largest_component_size, len(largest_component))
        return largest_component_size


class InvalidElementException(Exception):
    def __init__(self, message):
        super(InvalidElementException, self).__init__(message)


class InvalidArraySizeException(Exception):
    def __init__(self, message):
        super(InvalidArraySizeException, self).__init__(message)