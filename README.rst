Flask Appbuilder Practice Project - Mskim
--------------------------------------------------------------

- Python Virtualenv::

    # install and setting virtualenv
    $ pip install virtualenv
    $ python3 -m venv venv

    # activate virtualenv
    $ source venv/bin/activate
    (if os is windows, use call instead of source. $ call venv/scripts/activate)

    # install require packages
    $ pip install -r requirements.txt

- Run it::

    # Create an admin user
    $ flask fab create-admin

    # Start a development web server on port 8080
    $ python run.py
