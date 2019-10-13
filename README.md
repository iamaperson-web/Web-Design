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





