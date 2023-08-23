from flask import Flask
from flask import send_file
import pathlib

app = Flask(__name__)

SECRET_PATH = pathlib.Path("/etc/secrets/my_secret")

@app.route('/secret')
def hello_secret():
    return send_file(SECRET_PATH)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)