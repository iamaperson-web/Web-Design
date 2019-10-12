# Databases

##Description
Databases are organised sets of data that is generally stored and accessed electronically. It has many uses, such as storing special 
information used to manage the data, storing data and providng facilities of searching specific record in given data, and managing access
rights (i.e. those that are allowed to have access to the data and are able to change it). Databases are important because it manages data 
efficiently and allows multiple users to perform tasks with ease as well as storing, organising and managing a large amount of information.
They have many uses in the real world (e.g. family management, business, etc.) 

##Creating databases
1. Add the following code below:
#Configuring database connection
git status
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="<the username from the 'Databases' tab>",
    password="<the password you set on the 'Databases' tab>",
    hostname="<the database host address from the 'Databases' tab>",
    databasename="<the database name you chose, probably yourusername$comments>",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

**Make sure the values set for username, hostname and databasename to the values from the "Databases tab". Change the password to the one 
that you set.**

2. 

