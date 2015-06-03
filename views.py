"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebMyBlog import app
from flask import request
from flask_moment import Moment
moment = Moment(app)
       
@app.route('/')     
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/myproject')
def myproject():
    """Renders the contact page."""
    return render_template(
        'myproject.html',
        title='Project',
        year=datetime.now().year,
        message = 'HEHE'
    )

@app.route('/mysecurity')
def mysecurity():
    """Renders the about page."""
    return render_template(
        'mysecurity.html',
        title='Security',
        year=datetime.now().year,
        message='The security.'
    )


"""browser info : user-agent"""
@app.route('/mybrowser')
def mybrowser():
    user_agent = request.headers.get("User-Agent")
    return '<p>Your browser is %s</p>' % user_agent

"""dynamic argument"""
@app.route('/user/<name>') 
def user(name):    
    return '<h1>Hello, %s!</h1>' % name

"""return error page 404"""
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

"""get local time"""
@app.route('/mytime') 
def mytime():    
    return render_template('mytime.html',     
                           title='TIME',                      
                           current_time=datetime.utcnow(),
                           year=datetime.now().year
                           ) 
