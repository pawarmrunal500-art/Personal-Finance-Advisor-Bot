from flask import Blueprint

bp = Blueprint('finance', __name__)

@bp.route('/incomes')
def incomes():
    return "Incomes"

@bp.route('/expenses')
def expenses():
    return "Expenses"

@bp.route('/budgets')
def budgets():
    return "Budgets"
