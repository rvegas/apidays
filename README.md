# Madrid APIdays Flask-Restless workshop

- Install python 2.7
- Install virtualenv:
    `sudo apt-get install python-pip python-setuptools`
    `sudo pip install virtualenv`
- Create a new virtualenv:
    `virtualenv .apidays`
- Activate the virtualenv:
    `source .apidays/bin/activate`
- Install Flask-Restless and Flask SQLAlchemy:
    `pip install Flask-Restless`
    `pip install Flask-SQLAlchemy`
- Run the server:
    `python server.py`
- Open a browser and go to:
    - http://localhost:5000/api/coin