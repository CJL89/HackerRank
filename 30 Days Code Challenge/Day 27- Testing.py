def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

import random

class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        # complete this function
        return []

class TestDataUniqueValues(object):

    data = random.sample(range(0, 100), 10)

    @staticmethod
    def get_array():
        # complete this function
        return TestDataUniqueValues.data

    @staticmethod
    def get_expected_result():
        # complete this function
        val = TestDataUniqueValues.data
        return val.index(min(val))

class TestDataExactlyTwoDifferentMinimums(object):

    data = [random.sample(range(0, 100), 9)]
    data.append(min(data))

    @staticmethod
    def get_array():
        # complete this function
        return TestDataExactlyTwoDifferentMinimums.data

    @staticmethod
    def get_expected_result():
        # complete this function
        val = TestDataExactlyTwoDifferentMinimums.data
        return val.index(min(val))
