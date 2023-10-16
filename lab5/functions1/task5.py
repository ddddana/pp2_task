from itertools import permutations

def print_permutations(input_string):
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    for permuted_string in permuted_strings:
        print(permuted_string)

user_input = input()
print()
print_permutations(user_input)
