def check_values(form):
    for value in form.values():
        if value.strip() != '':
            continue
        else:
            return True

    return False


def generate_inputs_name(count):
    result_list = [f'input{i}' for i in range(1, count)]
    result_list.insert(0, 'input')
    return result_list
