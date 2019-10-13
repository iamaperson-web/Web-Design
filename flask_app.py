from flask import Flask, render_template, flash, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy #imports SQLAlchemy

#Configures database connection. 
#These commands below sets a variable to the specifically-formatted string SQLAlchemy needs to connect to your database. 
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<the username from the 'Databases' tab>",
    password="<the password you set on the 'Databases' tab>",
    hostname="<the database host address from the 'Databases' tab>",
    databasename="<the database name you chose, probably yourusername$comments>",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI #Stashes commands in Flask's application configuration settings.
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299  #Tells SQAlchemy to throw away connections that haven't been used for 299 seconds. 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Disables a SQAlchemy feature that is not going to be used. 
db = SQAlchemy(app) #Creates a SQALchemy object using the connections that are put into Flask's app configuration. 

class AddUserModel(db.Model):
    __tablename__ = "addusersmodel"
    id = db.Column(db.Integer, primary_key="True") #Primary key 
    #Contents of the table. 
    givenname = db.Column(db.String(64), index=True)
    familyname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    profileimage = db.Column(db.String(64))

@app.route("/newuser", methods=["GET", "POST"])
def newuser():
    
    users = AddUserModel.query.all() #Allows to make queries to the database. 

    form = AddUserForm()

    if form.validate_on_submit():
        newuser = AddUserModel(
            givenname = request.form['givenname'],
            familyname = request.form['familyname'],
            username = request.form['username'],
            profileimage = request.form['profileimage'],
        )
        db.session.add(newuser) #Represents the newuser, but does not store it in the database. 
        db.session.commit() #Sends the command to the database to store it, but leaves the transaction open. 
        return redirect('/newuser')


    return render_template('adduser.html', form=form, users=users)










