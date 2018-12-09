def greatest_common_factor(a, b):
    while b:
        a, b = b, a%b
    return a


class Solution:
    def largestComponentSize(self, A: list):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) > 20_000:
            raise InvalidArraySizeException("Array size greater than 20000")
        for a in A:
            if a > 100_000:
                raise InvalidElementException("Element greater than 100000")
        largest_component_size = 0
        largest_component = []
        for a_idx, a in enumerate(A):
            largest_component.append(a)
            A.pop(a_idx)
            for b_idx, b in enumerate(largest_component):
                for c_idx, c in enumerate(A):
                    if greatest_common_factor(b, c) > 1:
                        largest_component.append(c)
                        A.pop(c_idx)
            largest_component_size = max(largest_component_size, len(largest_component))
            largest_component = []

        return largest_component_size
                        

class InvalidElementException(Exception):
    def __init__(self, message):
        super(InvalidElementException, self).__init__(message)


class InvalidArraySizeException(Exception):
    def __init__(self, message):
        super(InvalidArraySizeException, self).__init__(message)