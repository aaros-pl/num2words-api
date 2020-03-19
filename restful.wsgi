activate_this = '/root/.virtualenvs/num2words-api/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys


# Install venv by `virtualenv --distribute venv`
# Then install depedencies: `source venv/bin/active`
# `pip install -r requirements.txt`


sys.path.insert(0, "/var/www/num2words-api/")


# The application object is used by any WSGI server configured to use this file.
#
# Ensure there is an app.py script in the current folder
from app import app as application
