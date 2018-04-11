import fractions
# from fractions import Fraction

ABSORPTION = 'absorption'
PROBABILITY = 'probability'
visited_states = set()

def answer(m):
    global visited_states
    # your code here
    terminal_s_values = get_terminal_s_values(m)
    probabilities = []

    transform_matrix(m)

    for i in terminal_s_values:
        visited_states = set()
        probability = find_prob_equ_recursive(m, i)
        probability = calculate_probability(probability)
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


def calculate_probability(probability_equation):
    if probability_equation:
        prob = probability_equation[PROBABILITY]
        if prob != fractions.Fraction(0, 1):
            prob /= (fractions.Fraction(1, 1) - probability_equation[ABSORPTION])
    else:
        prob = fractions.Fraction(0, 1)
    return prob


def combine_probability_equations(equ_1, equ_2):
    new_prob = {}
    new_prob[PROBABILITY] = equ_1[PROBABILITY] + equ_2[PROBABILITY]
    new_prob[ABSORPTION] = (equ_1[ABSORPTION] + equ_2[ABSORPTION])
    return new_prob


def add_absorptions(equ_1, equ_2):
    new_equ = {}
    new_equ[PROBABILITY] = equ_1[PROBABILITY] + equ_2[PROBABILITY]
    new_equ[ABSORPTION] = equ_1[ABSORPTION] + equ_2[ABSORPTION]
    return new_equ

def find_prob_equ_recursive(m, target_s_index, current_s_index=0,
                            multiplier=fractions.Fraction(1, 1),
                            first_pass=True, probability_equation=None):
    global visited_states

    if first_pass:
        probability_equation = {
            PROBABILITY: m[0][target_s_index],
            ABSORPTION: fractions.Fraction(0, 1)
        }
        first_pass = False

    if current_s_index == target_s_index:
        return {
            PROBABILITY: fractions.Fraction(0, 1),
            ABSORPTION: fractions.Fraction(1, 1) * multiplier
        }
        return multiplier
    elif reduce(lambda x, y: x + y, m[current_s_index]) == 0:
        return {
            PROBABILITY: fractions.Fraction(0, 1),
            ABSORPTION: fractions.Fraction(0, 1)
        }
        return fractions.Fraction(0, 1)
    elif current_s_index in visited_states:
        return {
            PROBABILITY: fractions.Fraction(0, 1),
            ABSORPTION: multiplier
        }
        return multiplier
    else:
        visited_states.add(current_s_index)
        non_zero_indices = set(get_none_zero_indices(m[current_s_index]))
        non_zero_indices = non_zero_indices - set([target_s_index])

        probability = multiplier * m[current_s_index][target_s_index]
        absorption_equation = {
            PROBABILITY: fractions.Fraction(0, 1),
            ABSORPTION: fractions.Fraction(0, 1)
        }

        for i in non_zero_indices:
            temp_absorption = find_prob_equ_recursive(
                m,
                target_s_index,
                current_s_index=i,
                multiplier=m[current_s_index][i] * multiplier,
                probability_equation=probability_equation,
                first_pass=first_pass)
            absorption_equation = add_absorptions(absorption_equation, temp_absorption)
            probability_equation[PROBABILITY] = probability
        new_equation = combine_probability_equations(probability_equation, absorption_equation)
        return new_equation


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


def get_none_zero_indices(m):
    indices = []
    for i in range(len(m)):
        if m[i] != fractions.Fraction(0, 1):
            indices.append(i)
    return indices


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
    [0, 1, 0, 1, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]
expected_outputs = [0, 3, 2, 9, 14]

test_inputs = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
expected_outputs = [0, 1, 0, 0, 1]

actual_outputs = answer(test_inputs)

print 'actual_outputs'
print actual_outputs
print 'expected_outputs'
print expected_outputs

