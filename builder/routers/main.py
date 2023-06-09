from flask import Blueprint, render_template, request, redirect

from builder.models.result import Result
from builder.extensions import db

main = Blueprint('main', __name__, static_folder='../static', template_folder='../templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {}
        for key, value in request.form.items():
            data[key] = value

        result = Result(data=data)
        db.session.add(result)
        db.session.commit()

        return redirect('/')

    context = {
    }

    return render_template('index.html', **context)


@main.route('/views/')
def view():
    context = {
        'result': Result.query.order_by('id')
    }
    return render_template('view.html', **context)
