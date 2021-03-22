"""Python demo for sorting using VS Code Debug Visualizer."""
import json


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return json.dumps(formatted)


def bubble_sort(arr):
    """Example sorting algorithm (bubble sort)"""
    global serialized
    sorted = False

    ### Put a breakpoint here for the debug visualizer ###
    while not sorted:
        # Was a swap made this time through?
        swap = False

        for i in range(0, len(arr)-1):
            # Compare two values
            if arr[i+1] < arr[i]:
                # Swap values
                swap = True
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp

                ### You need this line every time you modify arr ###
                serialized = serialize(arr)

        # When no swaps were made in a pass through, arr is sorted
        sorted = not swap

    return arr


# Test Case Example 1
arr = [2,5,3,7,4,2,5,6,3,9]
serialized = serialize(arr)
assert sorted(arr) == bubble_sort(arr)

# Test Case Example 2
arr = [10,20,-123,0,1234,4,3,2,5]
serialized = serialize(arr)
assert sorted(arr) == bubble_sort(arr)


# Implement your own sorting algorithm
"""
def your_sorting_algorithm(arr):
    global serialized
    # TODO logic
    return arr


arr = [2,5,3,7,4,2,5,6,3,9]
serialized = serialize(arr)
assert sorted(arr) == your_sorting_algorithm(arr)
"""