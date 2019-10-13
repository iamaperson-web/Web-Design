# Databases

**Description**
Databases are organised sets of data that is generally stored and accessed electronically. It has many uses, such as storing special 
information used to manage the data, storing data and providng facilities of searching specific record in given data, and managing access
rights (i.e. those that are allowed to have access to the data and are able to change it). Databases are important because it manages data 
efficiently and allows multiple users to perform tasks with ease as well as storing, organising and managing a large amount of information.
They have many uses in the real world (e.g. family management, business, etc.) 

**Creating databases**
1. Add the following code below:
![image](https://user-images.githubusercontent.com/56465665/66709672-ba4ca180-ed58-11e9-823f-d519c746c3b9.png)


*Make sure the values set for username, hostname and databasename to the values from the "Databases tab". Change the password to the one 
that you set.*

Connection timeouts occur when a website is really busy, in which the aggregate of the small amounts of time opening connections could lead to quite a slowdown. SQALchemy operates as a "connection pool" to keep a set of connections to the database and re-uses them. For example, if you want a connection, it gives you one from the pool, creating a new one if the pool is empty. When you are done with it, the connection is returned to the pool for further re-use. However, MySQL servers close unused connections after a particular amount of time to prevent people from hogging the database. The SQLALCHEMY_POOL_RECYCLE variable is set to 299 to tell SQLAlchemy that it should throw away connections that haven't been used for 299 seconds, so that it doesn't give them to you and cause your code to crash because it's trying to use a connection that has already been closed by the server.


2. Now that the code configures the database connection, add the following code after the code you just added to connect to the database connection. 
![image](https://user-images.githubusercontent.com/56465665/66709888-9ab77800-ed5c-11e9-9faa-ab1f6af7e512.png)

3. To make this work, add the extra import statement at the start of the code. 
![image](https://user-images.githubusercontent.com/56465665/66710001-2fbb7080-ed5f-11e9-9aa9-3c7a65ddd7f5.png)

4. Now you will need to create a model. A model is a Python class that specifies the information that you want to store into the database as SQAlchemy handles all the complexities of loading and storing information in MySQL. Here is an example of a model below:

![image](https://user-images.githubusercontent.com/56465665/66710016-685b4a00-ed5f-11e9-8ce4-b243f98fb156.png)

An SQL database is somewhat similar to a spreadsheet as it contains a number of tables just like when a spreadsheet contains a number sheets. Each table is formed of rows and columns. Each row serves as data records of information - in this case, each user would be a row. The columns serves as attributes of the class as for the database, two columns are specified: an integer id and a string of content, which in this case consists of the user's details. 

5. Now that the model has been defined, you will need SQLAlchemy to create database tables. Save your Python file, then start opening your bash console. Make sure you run python3.6 to start a Python interpreter. Once it is running, import the database manager from your code. 

Once you have done that, the table has been created in the database. 

6. To confirm this, go to the databases tab on PythonAnywhere page and start a new console by clicking on your database name. E.g. (yourusername$default). This will run the MySQL command line. 

7. Once it has loaded (it will display a mysql> prompt), run the command:

This should show that you have a table called 'AddUsers'.

8. To ensure that it contains the information you would expect, run the command:

You will have two columns: id and content

9. Now that you have the code in your Flask app to connect to the database, a Python definition of what information that you want to store in the database, and tables created in the database on the MySQL server to store the data, get rid of the line where you create the old in-memory storage for the comments. E.g. the one like this:

And change it into this: 


Keep in mind that the query attribute is something that SQLAlchemy added to your AddUser class, allowing you to make queries to the database, and its all method, just gets all users.

10. Next, add the following code after the code you have just added. 

Transactions batches up a bunch of changes into one, for efficiency and also so that if an error occurs you can easily abort and have none of them happen. 

11. Save your Python file, type and submit the details. Your details should now be displayed onto your webpage. 











