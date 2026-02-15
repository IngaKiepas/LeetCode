/* 
Table: Customer
+---------------------------
| Column name | Type       |
+--------------------------+
| id          | int        |
| name        | varchar    |
| referee_id  | int        |
+--------------------------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Find the name of the customer that are either:
- referred by any customer with id != 2
- not referred by any customer
Return the result table in any order.
*/

SELECT name from Customer where referee_id != 2 or referee_id is null