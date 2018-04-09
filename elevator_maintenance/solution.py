def answer(l):
    # your code here
    elevators = list(map(seperate_rev, l))
    sorted_elevators = []

    while len(elevators) > 0:
        min_elevator = get_min_elevator(elevators)
        sorted_elevators.append(min_elevator)
        elevators.remove(min_elevator)

    sorted_elevators = list(map(combine_rev, sorted_elevators))
    return sorted_elevators


def get_min_elevator(l):
    min_elevator = l[0]
    for item in l:
        if item is min_elevator:
            continue
        if elevator_less_than(item, min_elevator):
            min_elevator = item
    return min_elevator

def elevator_less_than(elevator_1, elevator_2):
    if elevator_1['major'] < elevator_2['major']:
        return True
    if elevator_1['major'] > elevator_2['major']:
        return False
    if elevator_1['minor'] < elevator_2['minor']:
        return True
    if elevator_1['minor'] > elevator_2['minor']:
        return False
    if elevator_1['revision'] < elevator_2['revision']:
        return True
    if elevator_1['revision'] > elevator_2['revision']:
        return False
    return False

def seperate_rev(rev):
    split_rev = rev.split('.')
    elevator = {
        'major': int(split_rev[0]),
        'minor': -1,
        'revision': -1
    }
    if len(split_rev) >= 2:
        elevator['minor'] = int(split_rev[1])
    if len(split_rev) >= 3:
        elevator['revision'] = int(split_rev[2])
    return elevator

def combine_rev(rev):
    elevator = str(rev['major'])
    if rev['minor'] != -1:
        elevator += '.' + str(rev['minor'])
    if rev['revision'] != -1:
        elevator += '.' + str(rev['revision'])
    return elevator

l = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
print answer(l)

l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
print answer(l)