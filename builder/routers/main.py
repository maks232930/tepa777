from flask import Blueprint, render_template, request, redirect, flash

from builder.models.result import Result
from builder.extensions import db
from builder.utils import check_result

main = Blueprint('main', __name__, static_folder='../static', template_folder='../templates')


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form

        result = check_result(form)

        if not result:
            flash('Не трогай!!!')
            return redirect('/')

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
