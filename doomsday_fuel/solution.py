import fractions
# from fractions import Fraction

ABSORPTION = 'absorption'
PROBABILITY = 'probability'

def answer(m):
    # your code here
    terminal_s_values = get_terminal_s_values(m)
    probabilities = []

    transform_matrix(m)

    for i in terminal_s_values:
        probability = find_probability_recursive(m, i, 0)
        probabilities.append(probability)

    denominators = list(map(lambda x: x.denominator, probabilities))

    lcm = get_lcm(denominators)

    for i in range(len(probabilities)):
        probability = probabilities[i]
        probabilities[i] = probability.numerator*(lcm/probability.denominator)

    probabilities.append(lcm)
    return probabilities


def transform_matrix(m):
    for i in range(len(m)):
        row_sum = sum(m[i])
        for j in range(len(m[i])):
            m[i][j] = fractions.Fraction(m[i][j], row_sum or 1)
    return m


def find_probability_recursive(m, target_s_index, current_s_index,
                               probability_equation=None):
    if current_s_index == target_s_index:
        prob = probability_equation[PROBABILITY]
        prob /= (fractions.Fraction(1, 1) - probability_equation[ABSORPTION])
        return prob

    if not probability_equation:
        probability_equation = {
            PROBABILITY: m[current_s_index][target_s_index],
            ABSORPTION: m[current_s_index][current_s_index + 1]
        }
    else:
        if reduce(lambda x, y: x + y, m[current_s_index]) != 0:
            temp_probability = probability_equation[ABSORPTION]
            temp_probability *= m[current_s_index][target_s_index]
            probability_equation[PROBABILITY] += temp_probability
            probability_equation[ABSORPTION] = probability_equation[ABSORPTION] * m[current_s_index][current_s_index - 1]

    return find_probability_recursive(
        m,
        target_s_index,
        current_s_index + 1,
        probability_equation)


def get_lcm(numbers):
    lcm = numbers[0]
    for x in numbers:
        lcm = (lcm*x)/fractions.gcd(lcm, x)
    return lcm


def get_terminal_s_values(m):
    terminal_s_rows = []
    for i in range(0, len(m)):
        is_terminal = True if (reduce(lambda x, y: x + y, m[i]) == 0) else False
        if is_terminal:
            terminal_s_rows.append(i)

    return terminal_s_rows


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
print 'actual_outputs'
print actual_outputs
print 'expected_outputs'
print expected_outputs

test_inputs = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
expected_outputs = [7, 6, 8, 21]

actual_outputs = answer(test_inputs)
print 'actual_outputs'
print actual_outputs
print 'expected_outputs'
print expected_outputs

test_inputs = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]
expected_outputs = [0, 3, 2, 9, 14]

print 'actual_outputs'
print actual_outputs
print 'expected_outputs'
print expected_outputs