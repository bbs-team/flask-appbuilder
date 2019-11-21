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

- User infomation::

    +---------+-----------+----------+
    |Username | Password  |  role    |
    +=========+===========+==========+
    |admin    | admin1234 |  admin   |
    +---------+-----------+----------+
    |user1    | 1234      |  user    |
    +---------+-----------+----------+
    |user2    | 1234      |  manager |
    +---------+-----------+----------+
    |user3    | 1234      |  user    |
    +---------+-----------+----------+
    |user4    | 1234      |  user    |
    +---------+-----------+----------+
    
+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+
