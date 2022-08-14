### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

  PostgreSQL is an open source relational database management system. 

- What is the difference between SQL and PostgreSQL?

  SQL is a standard language used to manipulate data in a relational database. PostgreSQL is a software package, that based on the content of a given SQL statement, executes the hands on manipulation of the data.

- In `psql`, how do you connect to a database?

  By using the commance '\c [database mame]

- What is the difference between `HAVING` and `WHERE`?

  Both the WHERE cluase and the HAVING cluase are used to filter records in a SELECT statement. The WHERE clause is used to filter a set of records that have not been grouped in any way. The HAVING clause filters records that have been grouped by the use of the GROUP BY clause. Grouped sets of records are characterrized by the use of an aggregate function on the gourp members, such as COUNT, SUM, AVG, etc.

- What is the difference between an `INNER` and `OUTER` join?

  An INNER join will retrieve records from two participatin tables, if the two records are linked via a foriegn key. If a record from one table does not have a linked record in the other table, this record will not be retreived. 

  An OUTER join will retrieve a record from one table, even if it does not have a linked record in the other table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

  The LEFT and RIGHT keywords refer to where a table's name appear in relation to the '=' operator of the 'ON' clause. When the LEFT keyword is used, all the records from the table to the left of the '=' operator, who meet any filtering condition will be retrieved. Records from the table to the right, will only be retreived if they satisfy the foreign key constraint.

  When the RIGHT keyword is used, the rolls are reversed. All the records from the table on the right side of the '=' operator will be retreived, while records from the left side will only be retreived if they meet the foreign key constraint.

- What is an ORM? What do they do?

  ORM stands for Object-Relational Mapper. AN ORM is an ubstruction layer, that 'sits' between software that uses the object orinted programming methodology on one hand, and the SQL language on the other. It eliminated the need for the developer to code (sometimes) complex SQL statments, and the need to wrap these statments with database connection code. Using an ORM simplifys the coding procceses and allows for better code reuse.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

   Ajax is used on the client side, via JavaScript. A requests-like library is used from the server side.

   A server-initiated call can be reused by different apps. a client-initiated call is limited to the calling client/app.



- What is CSRF? What is the purpose of the CSRF token?

  CSRF stands for Cross-Site Request Forgery. This is a type of cyber attack that attempts to retreive/manipulate database data by presenting a simingly valid request to the server that holds the data, where in fact the attacker is not authorized to access/manipulate the data and is not using the authorized application/interface.

  CSRF attacks are prevented via the use of hashed tokens. The server is generating the token, and it expects the incoming request to present this token back to the server.

- What is the purpose of `form.hidden_tag()`?

  This method is used to avoid displaying WTForm elements that are meant to be hidden from the user, such as CSRF tokens.


