# Intro-to-Relational-Database

This course by Udacity introduces the basics of relational databases and SQL. There are four lessons in this course:
1. Relational Concepts: how to organize data in relational databases. 
2. SQL Queries: how to fetch data out of a database and to insert new data into it. 
3. Python Database API: connect Python code up to a database server. 
4. Advanced SQL: learn to perform more advanced SQL queries. 

[Link to Udacity Source Code](https://github.com/udacity/fullstack-nanodegree-vm)
[Link to Udacity Intro to Relational Database Course](https://classroom.udacity.com/courses/ud197)

## Troubleshooting: ##
### The web forum doesn't show the time of when the message is posted.  ###

There is a problem in the forumdb_solved.py from Udacity source code. If you test it, the web forum won't show the time of when the message was posted, even though the tutorial did show time, because they only insert the message content into the table. To solve this problem, we need to import datetime from the datetime library.

Change this line 

`c.execute("insert into posts values (%s)", (bleach.clean(content),))`

to 

`c.execute("insert into posts values (%s, %s)", (bleach.clean(content), datetime.now(), ))`. 

_New forumdb_solved.py can be downloaded above._
 
