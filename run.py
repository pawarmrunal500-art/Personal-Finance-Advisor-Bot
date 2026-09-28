from app import create_app, db
from app.models import User, Income, ExpenseCategory, Expense, Budget, SavingsGoal

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Income': Income,
        'ExpenseCategory': ExpenseCategory,
        'Expense': Expense,
        'Budget': Budget,
        'SavingsGoal': SavingsGoal
    }

if __name__ == '__main__':
    app.run(debug=True)
