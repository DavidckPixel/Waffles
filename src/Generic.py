def create_dict_of_entries(entries, prop):
    new_dict = dict()

    for entry in entries:
        val = vars(entry)[prop]
        if val in new_dict.keys():
            cur = new_dict[val]
            new_dict[val] = cur + [entry]
        else:
            new_dict[val] = [entry] 

    return new_dict


def count_property_values(entries, prop):
    new_dict = dict()

    for entry in entries:
        val = vars(entry)[prop]
        if val in new_dict:
            new_dict[val] += 1
        else:
            new_dict[val] = 1

    return new_dict
