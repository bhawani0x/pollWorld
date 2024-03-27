from api.app import app
from api.connection import *
from api.routes import *

from api.Models import User

if __name__ == "__main__":
    app.run(host="0.0.0.0", )

    create_table = False
    if create_table:
        with app.app_context():
            db.create_all()
