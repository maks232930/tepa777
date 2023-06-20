from flask import Blueprint, render_template, request, redirect, flash

from builder.models.result import Result
from builder.extensions import db
from builder.utils import generate_inputs_name, check_values

main = Blueprint('main', __name__, static_folder='../static', template_folder='../templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result = None
        form = request.form

        if len(form) == 0 or check_values(form):
            flash('Не трогай!!!')
            return redirect('/')
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

        db.session.add(result)
        db.session.commit()
        return redirect('/')

    return render_template('index.html')


@main.route('/views/')
def view():
    context = {
        'result': Result.query.order_by('id')
    }
    return render_template('view.html', **context)
