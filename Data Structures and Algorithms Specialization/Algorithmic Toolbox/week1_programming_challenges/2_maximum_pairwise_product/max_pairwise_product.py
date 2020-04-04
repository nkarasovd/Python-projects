# python3


def max_pairwise_product(numbers):
    el1, el2 = 0, 0

    for el in numbers:
        if el >= el1:
            el2 = el1
            el1 = el
        elif el > el2:
            el2 = el

    return el1 * el2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
