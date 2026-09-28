from app import create_app, db
from app.models import ExpenseCategory

app = create_app()

default_categories = [
    'Rent', 'Food', 'Transport', 'Education', 'Healthcare',
    'Shopping', 'Entertainment', 'Bills', 'Utilities', 'Travel', 'Other'
]

def init_db():
    with app.app_context():
        db.create_all()
        print("Database tables created.")
        
        # Populate default categories if they don't exist
        for cat_name in default_categories:
            existing = ExpenseCategory.query.filter_by(name=cat_name, user_id=None).first()
            if not existing:
                cat = ExpenseCategory(name=cat_name, user_id=None)
                db.session.add(cat)
        
        db.session.commit()
        print("Default expense categories populated.")

if __name__ == '__main__':
    init_db()
