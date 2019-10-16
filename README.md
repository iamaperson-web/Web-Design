# Databases

**Description:**
Databases are organised sets of data that is generally stored and accessed electronically. It has many uses, such as storing special 
information used to manage the data, storing data and providng facilities of searching specific record in given data, and managing access
rights (i.e. those that are allowed to have access to the data and are able to change it). Databases are important because it manages data 
efficiently and allows multiple users to perform tasks with ease as well as storing, organising and managing a large amount of information.
They have many uses in the real world (e.g. family management, business, etc.) 

# Installation
**Setting up Flask:**

1. First, you will need to set up and configure PythonAnywhere. Go to pythonanywhere.com and sign in.
2. Click on the **Web** tab.

![image](https://user-images.githubusercontent.com/56465665/66878748-18061580-f007-11e9-8bdf-39529ac237d2.png)

3. Add a new web app. 

![image](https://user-images.githubusercontent.com/56465665/66880146-3ec74a80-f00d-11e9-8740-4e2b3c977d27.png)

Then select Flask.

![image](https://user-images.githubusercontent.com/56465665/66880155-51da1a80-f00d-11e9-99b1-cc8626d715ed.png)

4. Select a Python version (mainly Python 3.6)

![image](https://user-images.githubusercontent.com/56465665/66880182-73d39d00-f00d-11e9-863a-0373ff877130.png)

5. Leave it as default and proceed. 

Then go to the **Web** tab and click the hyperlink to your page. You should have a webpage.

![image](https://user-images.githubusercontent.com/56465665/66880248-db89e800-f00d-11e9-844d-0388ad57e12c.png)

6. Go back to your **Web** tab and find your source code section. Go to that directory.

![image](https://user-images.githubusercontent.com/56465665/66880330-2d327280-f00e-11e9-9ee2-74dc2381e065.png)

Then select flask_app.py:

![image](https://user-images.githubusercontent.com/56465665/66880373-5d7a1100-f00e-11e9-81b0-403e6c73f5c8.png)

You should be able to see something like this: 

![image](https://user-images.githubusercontent.com/56465665/66880398-75ea2b80-f00e-11e9-99e6-c1d5d24a3b7b.png)

**Setting up a database:**

1. Go to the **Databases** tab. You should already have these details below:

![image](https://user-images.githubusercontent.com/56465665/66830253-c460e100-efa0-11e9-8b99-533a6f2274fd.png)

![image](https://user-images.githubusercontent.com/56465665/66880475-d11c1e00-f00e-11e9-8311-29675cf0e04b.png)

2. Underneath Create a Database, add a database name called:

![image](https://user-images.githubusercontent.com/56465665/66880550-1d675e00-f00f-11e9-8def-b845eee23494.png)

**Make sure you use your username that you set up earlier!**

This should be displayed underneath your databases:

![image](https://user-images.githubusercontent.com/56465665/66880598-50a9ed00-f00f-11e9-852c-9d25a6e8ab5c.png)

3. Underneath MySQL password, create a password and then set it as your MySQL password. 

![image](https://user-images.githubusercontent.com/56465665/66880610-64555380-f00f-11e9-9ed1-fb6457958e49.png)


4. After you have done the steps above, you should be able to have all the following database details that you will need later on when you create a database:
* username 
* host name
* database name 
* password

# Usage
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

![image](https://user-images.githubusercontent.com/56465665/66830253-c460e100-efa0-11e9-8b99-533a6f2274fd.png)

![image](https://user-images.githubusercontent.com/56465665/66830688-cd9e7d80-efa1-11e9-8351-6ba8165b90c0.png)


Once you have done that, the table has been created in the database. 

6. To confirm this, go to the databases tab on PythonAnywhere page and start a new console by clicking on your database name. E.g. (yourusername$default). This will run the MySQL command line. 

![image](https://user-images.githubusercontent.com/56465665/66828276-57e3e300-ef9c-11e9-9bb3-e77c51cd756c.png)

![image](https://user-images.githubusercontent.com/56465665/66828430-bd37d400-ef9c-11e9-91c8-ce5d1e35603a.png)

7. Once it has loaded (it will display a mysql> prompt), run this command to show databases:

![image](https://user-images.githubusercontent.com/56465665/66831807-40105d00-efa4-11e9-8221-e057bc6f9822.png)

And then run this command:

![image](https://user-images.githubusercontent.com/56465665/66832206-20c5ff80-efa5-11e9-90a8-9b7a9efc3930.png)

It should display this message:

![image](https://user-images.githubusercontent.com/56465665/66832275-510d9e00-efa5-11e9-9bed-06a8184f4df8.png)

Then run this command:

![image](https://user-images.githubusercontent.com/56465665/66832340-73072080-efa5-11e9-8925-168fef759ef0.png)

This should show that you have a table called 'AddUsers'.

![image](https://user-images.githubusercontent.com/56465665/66832397-8e722b80-efa5-11e9-859e-dade78897e71.png)

8. To ensure that it contains the information you would expect, run this command:

![image](https://user-images.githubusercontent.com/56465665/66832517-cda07c80-efa5-11e9-8bb0-756875756924.png)

You will have two columns: id and content

![image](https://user-images.githubusercontent.com/56465665/66832579-ed37a500-efa5-11e9-9106-ae62c0ae0ecd.png)


9. Now that you have the code in your Flask app to connect to the database, a Python definition of what information that you want to store in the database, and tables created in the database on the MySQL server to store the data, get rid of the line where you create the old in-memory storage for the comments. E.g. the one like this:

![image](https://user-images.githubusercontent.com/56465665/66724148-21a84580-ee6e-11e9-8618-2613f62a6954.png)

And change it into this: 

![image](https://user-images.githubusercontent.com/56465665/66724167-6338f080-ee6e-11e9-8402-d0a1349b323e.png)

Keep in mind that the query attribute is something that SQLAlchemy added to your AddUser class, allowing you to make queries to the database, and its all method, just gets all users.

10. Next, add the following code after the code you have just added. 

![image](https://user-images.githubusercontent.com/56465665/66724180-8fed0800-ee6e-11e9-9147-f850432d8923.png)

Transactions batches up a bunch of changes into one, for efficiency and also so that if an error occurs you can easily abort and have none of them happen. 

11. Save your Python file, type and submit the details. Your details should now be displayed onto your webpage.

![image](https://user-images.githubusercontent.com/56465665/66724197-d0e51c80-ee6e-11e9-87d7-6d29a60959fa.png)

# Credits









