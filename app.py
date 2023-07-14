from flask import Flask, render_template
from sqlalchemy import create_engine, text
from decouple import config


# The line `engine = create_engine(config('DB_CONNECTION_STRING'))` is creating a database engine
# using the SQLAlchemy library.
engine = create_engine(config('DB_CONNECTION_STRING'))


# `app = Flask(__name__)` creates an instance of the Flask class, which represents the Flask
# application. The `__name__` argument is a special Python variable that gets the name of the current
# module. This is necessary for Flask to know where to look for static files, templates, and other
# resources.
app = Flask(__name__)

# ---------------------------------- Routes ---------------------------------- #

# The index function returns the rendered index.html template.
# :return: the result of the `render_template` function, which is typically an HTML file.
@app.route('/')
def index():
    return render_template('index.html')


# ------------------------------ About Me Route ------------------------------ #
@app.route('/about')
def about():
    return render_template('about-me.html')


# -------------------------- Work and Projects Route ------------------------- #
@app.route('/work')
def work():
    with engine.connect() as conn:
        data = conn.execute(text('select * from projects'))
        projects = []
        
        # The code `for row in data.all(): projects.append(dict(zip(data.keys(), row)))` is iterating over
        # each row in the `data` object, which represents the result of the SQL query.
        for row in data.all():
            # the zip() function is used to combine the keys of the data object with the values ​​of each data row (row). Then, a dictionary is created using the dict() function to map the keys to their respective values ​​in each row. Finally, this dictionary is added to the projects list using the append() method.
            projects.append(dict(zip(data.keys(), row)))
            
        print(projects)
    return render_template('work.html', projects = projects)

# ------------------------------- Skills Route ------------------------------- #
@app.route('/skills')
def skills():
    return render_template('skills.html')


# --------------------------------- CV Route --------------------------------- #
@app.route('/resume')
def resume():
    return render_template('resume.html')


# ------------------------------- Contact Route ------------------------------ #
@app.route('/contact')
def contact():
    return render_template('contact.html')


# ------------------------------- Start App ------------------------------ #
if __name__ == '__main__':
    app.run(debug=True, port=3001)