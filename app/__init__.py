from flask import Flask
import os
# app = Flask(__name__)

TEMPLATE_DIR = os.path.abspath('app/templates')
STATIC_DIR = os.path.abspath('app/static')
cwd = os.getcwd()
print(cwd)
# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
from app import routes