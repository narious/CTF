# SQL Injections

Most SQL Injections occur in the SELECT clause hoever we can also expand to other attacks such as the SQL [Union](https://www.w3schools.com/sql/sql_union.asp) attacks.
Union attacks are quite restrictive since they require
- The two queries return the same number of columns
- Data types between queries must be compatible

Since Union appends the results from the first query with the results of the second query (by column)

To find the number of columns we can utilizes the ORDER BY sent in a where clause i.e.,

```
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
etc.
```
[Using Unions and Null values](https://portswigger.net/web-security/learning-paths/sql-injection/sql-injection-determining-the-number-of-columns-required/sql-injection/union-attacks/determining-the-number-of-columns-required-6r5t)

Or using union select and a number of null values. Since NULL is compatible with every common data type, and we must have all values returns by the injected select to be compatible with. If successfull the result returns an additional row with all NULL values in the columns, however is succestuble to NULL POINTER EXCEPTION

```
UNION SELECT NULL [,NULL]--
```

![Lab discover columns](./labfindcols.png)

In this lab we discover the number of columns in a SQL query notice after trying three NULLs there is an extra row of NULLS at the bottom!

## [Database specific queries](https://portswigger.net/web-security/sql-injection/cheat-sheet)
Oracle requires the use of the FROM after a SELECT call. We may use DUAL which is a default table always available

On mySQL the comment commnad `--` should always be followed by a SPACE


## Looking for string data

String data usually is what we want to exfiltrate from the website, hence looking for a column that is compatible with string data comes in handy the typical way is to submit SQL UNION statements with a string character i.e.,`'a'` and check that the website response.

E.g. ' UNION SELECT 'a',NULL,NULL,NULL -- 

![StringData](./stringdata.png)

In this lab we send the SQL query when looking for accesories


> Database names and columns are difficult to find. Sometimes we need to guess however, all moderns Databases have a function to examine the tables and columns, if only we can access that functionality... 


## Lab Usefull data
In this lab we have discovered a SQL vulnerability in the filtering
