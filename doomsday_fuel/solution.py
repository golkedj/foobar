from fractions import Fraction

def answer(m):
    # your code here
    terminal_s_values = get_terminal_s_values(m)
    print 'terminal_s_values'
    print terminal_s_values
    max_s_value = terminal_s_values[-1]
    print 'max_s_value'
    print max_s_value
    probabilities = [0] * len(terminal_s_values)
    for i in range(0, len(probabilities)):
        print 'i'
        print i
        probability_equation = {
            'probability': Fraction(1, 1),
            'absorbtion': Fraction(1, 1)
        }
        probability = find_probability_recursive(m, i, 0, probability_equation)
        print 'probability'
    # return recursive_check_index(m, terminal_s_values, [], 0)

def find_probability_recursive(m, target_s_index, current_s_index, probability_equation=None):
    print '*' * 100
    print 'm'
    print m
    print 'target_s_index'
    print target_s_index

    if current_s_index == target_s_index:
        print 's index found'
        print current_s_index
        print 'probability_equation'
        print probability_equation

    if current_s_index > len(m):
        return {
            'probability': Fraction(0, 1),
            'absorbtion': Fraction(0, 1)
        }


    find_probability_recursive()


    #
    # if current_s_index = :
    #     print 'returning s_index'
    #     print s_index
    #     return s_index
    #
    # non_zero_indices = get_none_zero_indices(m[s_index])
    # print 'non_zero_indices'
    # print non_zero_indices
    #
    # for non_zero_index in non_zero_indices:
    #     paths.append
    # m[s_index][non_zero_index] -= 1
    # recursive_check_index()
    # paths.append(recursive_check_index(m, terminal_s_values, paths, non_zero_index))


def get_terminal_s_values(m):
    terminal_s_rows = []
    for i in range(0, len(m)):
        is_terminal = True if (reduce(lambda x, y: x + y, m[i]) == 0) else False
        if is_terminal:
            terminal_s_rows.append(i)

    return terminal_s_rows


def get_none_zero_indices(m):
    return list(filter(lambda x: x != 0, m))


test_inputs = [
  [0, 1, 0, 0, 0, 1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0, 0, 0, 0, 0, 0],  # s2 is terminal, and unreachable (never observed in practice)
  [0, 0, 0, 0, 0, 0],  # s3 is terminal
  [0, 0, 0, 0, 0, 0],  # s4 is terminal
  [0, 0, 0, 0, 0, 0],  # s5 is terminal
]

expected_outputs = [0, 3, 2, 9, 14]

actual_outputs = answer(test_inputs)

test_inputs = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
expected_outputs = [7, 6, 8, 21]

test_inputs = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]
expected_outputs = [0, 3, 2, 9, 14]
