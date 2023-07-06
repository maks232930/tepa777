from builder.models import Result


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


def check_result(form):
    result = None

    if len(form) == 0 or check_values(form):
        return False
    elif len(form) == 1:
        result = Result(data={'input': list(form.values())[0]})
    elif len(form) > 1:
        data = {}
        keys = generate_inputs_name(len(form))
        values = list(form.values())
        keys_values = [[keys[i], values[i]] for i in range(len(form))]

        for key, value in keys_values:
            data[key] = value

        result = Result(data=data)

    return result
