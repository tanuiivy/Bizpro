from flask import Flask
from config import Config
from extensions import db, migrate, bcrypt, jwt, ma, cors

#Models
from models.user import User
from models.Supplier import Supplier, Invoice, Payment, SupplierPosting

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    @app.route('/')
    def home():
        return "Hey Bizpro"

    return app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
