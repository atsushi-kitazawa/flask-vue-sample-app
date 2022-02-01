from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AccountModel(db.Model):
    __tablename__ = 'account_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return AccountModel.query.order_by(AccountModel.id).all()

def insert(id, name):
    model = AccountModel(id=id, name=name)
    db.session.add(model)
    db.session.commit()