from webapp import create_app
from webapp.db import db

app = create_app()

with app.app_context():
    db.create_all()