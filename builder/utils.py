def check_inputs(form):
    for key, value in form.items():
        if key.startswith('input') and value.strip() != '':
            continue
        else:
            return False

    return True
