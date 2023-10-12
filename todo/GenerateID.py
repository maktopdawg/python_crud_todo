import random

def generate_id():
    id_set = set()
    while len(id_set) != 5:
        id_set.add(random.randint(0,9))

    id_list = [i for i in id_set]

    return ''.join([str(i) for i in id_list])