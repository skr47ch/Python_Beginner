# Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.


def new_list(input_list):
    return set(input_list)


def new_list2(input_list):
    new = []
    for x in input_list:
        if x not in new:
            new.append(x)
    return new


print(new_list([1, 2, 4, 5, 1, 4, 3, 3]))
print(new_list2([1, 2, 4, 5, 1, 4, 3, 3]))
