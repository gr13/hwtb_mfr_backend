# import sys
from src import app
from src.db import db

# flask logger
# sys.stdout = sys.stderr = open("log/api_log.txt", "w+")

db.init_app(app)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
