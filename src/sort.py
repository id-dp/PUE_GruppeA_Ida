import numpy as np

def bubble_sort(the_array_to_sort):
    """A Function to sort an numpy array manually"""
    for i in range(len(the_array_to_sort)):
        for j in range(0, len(the_array_to_sort)-i-1):
            if the_array_to_sort[j] > the_array_to_sort[j+1]:
                # swap if the element found is greater than the next element
                the_array_to_sort[j], the_array_to_sort[j+1] = the_array_to_sort[j+1], the_array_to_sort[j]
    return the_array_to_sort

if __name__ == "__main__":
    test_array = [3,2,1]