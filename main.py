# RHS Lost & Found
# Sam Giddens
# This project is a lost and found page for Rangiora High School. This page will be used by Rangiora High School staff and students


from flask import Flask, render_template, abort, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'correcthorsebatterystaple'

db = SQLAlchemy(app)

WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = 'sup3r_secr3t_passw3rd'

# need db to import models
import models


# basic route
####### HOME ######
# home route - called by Home in the nav bar 
@app.route('/')
def root():
    return render_template('home.html', page_title='HOME')


###### ABOUT ######
# about route - called by About in the nav bar 
# returns information about the site
@app.route('/about')  
def about():
    return render_template('about.html', page_title='ABOUT')


###### LOST ITEMS ######
# lost item route - called Lost Items in the nav bar
# returns a table listing items that have been lost at RHS
@app.route('/lost_items')  
def lost_items():
  Lost_Items = models.Lost_Items.query.all()
  if len(Lost_Items) == 0:
    return render_template("no_lost.html", page_title='NO LOST ITEMS') # displays page telling user no lost items at that time
  else:
    return render_template("lost_items.html", page_title='LOST ITEMS', Lost_Items=Lost_Items) # displays page of table of lost items


###### FOUND ITEMS ######
# found item route - called Found Items in the nav bar
# returns a table listing items that have been Found at RHS
@app.route('/found_items')  
def found_items():
  Found_Items = models.Found_Items.query.all()
  return render_template("found_items.html", page_title='FOUND ITEMS', Found_Items=Found_Items) # displays page of table of found items


###### 404 ERROR ######
# This page will display when the user trys to access a page that doesn't exist
@app.errorhandler(404)
def page_not_found(e):
   return render_template("404.html", page_title = '404 ERROR')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
