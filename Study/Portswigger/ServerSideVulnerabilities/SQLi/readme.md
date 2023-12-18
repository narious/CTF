# SQL Injection
SQL injections happen when a input field or the server processes a user editable field as SQL. Indicators of SQL vulnerability are:
- Processing of `'` single quote and odd response
- Processing of ` OR 1=1` i.e., booleans
- Look for semantic differences by the response of the application

Or utilize Burp Scanner to find SQL vulnerabilities

An [example](https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/sql-injection-apprentice/sql-injection/retrieving-hidden-data): A shopping cart searches for a category of items using catergory?burritoes; In the backend this returns a SQL query `SELECT * WHERE category = 'burritoes'` etc

> Crucially, note that -- is a comment indicator in SQL.

This command `products?category=Gifts'+OR+1=1--`
- The first `'` terminates the first quote mark in the SQL and the -- causes the rest to be a comment!

Login SQL queries are particularly dangerous i.e., 

`SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'`

As we know if we utilize the username admin'-- then we maybe able to log