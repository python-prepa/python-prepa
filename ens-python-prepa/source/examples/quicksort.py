"""
Quick sort
"""
def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop() # this modifies the initial list!!
    # to avoid this, do
    # copy_array = array[:]; pivot = copy_array.pop()
    less_than, greater_than = [], []
    for element in array:
        if element < pivot:
            less_than.append(element)
        else:
            greater_than.append(element)
    return quicksort(less_than) + [pivot] + quicksort(greater_than)
