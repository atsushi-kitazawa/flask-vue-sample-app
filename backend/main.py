import os
from flask import Flask, render_template
from api import api_bp
from models import get_all, init_db, insert

app = Flask(__name__, static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'.format(**{
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': os.environ['DATABASE_IPADDRESS'],
    'port': '15432',
    'name': 'flask_app_db'
})
app.register_blueprint(api_bp)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        init_db(app)
        if not get_all():
            insert(1, 'foo')
            insert(2, 'bar')
    app.run()
