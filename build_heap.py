swaps = []

def swap_nodes(data, i):
    n = len(data)
    left_child, right_child = 2 * i + 1, 2 * i + 2
    
    largest_value = i

    if left_child < n and data[left_child] < data[largest_value]:
        largest_value = left_child

    if right_child < n and data[right_child] < data[largest_value]:
        largest_value = right_child

    if largest_value != i:
        data[i], data[largest_value] = data[largest_value], data[i]
        swaps.append((i, largest_value))
        swap_nodes(data, largest_value)


def build_heap(data):

    n = len(data)
    last_non_leaf = n // 2 - 1

    for i in range(last_non_leaf, -1, -1):
        swap_nodes(data, i)

    print(data)
    return swaps


def main():
    
    input_type = input()

    if 'I' in input_type:
        n = int(input())
        data = list(map(int, input().split(' ')))

    elif 'F' in input_type:
        filename = input()
        if 'a' in filename:
            raise Exception('Filename cannot contain character "a"')

        with open('tests/{filename}') as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split(' ')))

    else:
        raise Exception('Invalid input type')

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
