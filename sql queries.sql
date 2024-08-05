mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| organization       |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)
-----------------------------------------------------------------------------------------
mysql> use organization;
Database changed
mysql> show tables;
+------------------------+
| Tables_in_organization |
+------------------------+
| departments            |
| employee_projects      |
| employees              |
| projects               |
+------------------------+
4 rows in set (0.00 sec)

mysql> select *from departments;
+---------------+-----------------+
| department_id | department_name |
+---------------+-----------------+
|             1 | Human Resources |
|             2 | Engineering     |
|             3 | Sales           |
|             4 | R&D             |
+---------------+-----------------+
4 rows in set (0.00 sec)

mysql> select *from employee_projects;
+-------------+------------+
| employee_id | project_id |
+-------------+------------+
|           2 |          1 |
|           4 |          1 |
|           1 |          2 |
|           3 |          3 |
|           5 |          4 |
+-------------+------------+
5 rows in set (0.00 sec)

mysql> select *from employees;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |
|           5 | roshan     | reddy     | roshan@gmail.com   | 8000899999   | 2024-07-04 | associate R&D            | 1200000.00 |             4 |       NULL |
|           6 | audrika    | borah     | audrika@gmail.com  | 8000099999   | 2024-07-04 | senior data scientist    | 1200000.00 |             2 |       NULL |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
6 rows in set (0.00 sec)

mysql> select *from projects;
+------------+--------------------+
| project_id | project_name       |
+------------+--------------------+
|          1 | fraud_detection    |
|          2 | text_summarization |
|          3 | automation         |
|          4 | generative_ai      |
+------------+--------------------+
4 rows in set (0.00 sec)

mysql> select *from employees where manager_id=6;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
4 rows in set (0.00 sec)
---------------------------------------------------------------------------------------------------------------






mysql> select count(employee_id) from employees group by manager_id;
+--------------------+
| count(employee_id) |
+--------------------+
|                  2 |
|                  4 |
+--------------------+
2 rows in set (0.00 sec)



mysql> select *from employees inner join departments where employees.department_id = departments.department_id;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+---------------+-----------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id | department_id | department_name |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+---------------+-----------------+
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |             2 | Engineering     |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |             2 | Engineering     |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |             2 | Engineering     |
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |             1 | Human Resources |
|           5 | roshan     | reddy     | roshan@gmail.com   | 8000899999   | 2024-07-04 | associate R&D            | 1200000.00 |             4 |       NULL |             4 | R&D             |
|           6 | audrika    | borah     | audrika@gmail.com  | 8000099999   | 2024-07-04 | senior data scientist    | 1200000.00 |             2 |       NULL |             2 | Engineering     |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+---------------+-----------------+
6 rows in set (0.00 sec)


ysql> select employees.employee_id,first_name, departments.department_id,departments.department_name from employees right join departments on emplo
yees.department_id=departments.department_id;
+-------------+------------+---------------+-----------------+
| employee_id | first_name | department_id | department_name |
+-------------+------------+---------------+-----------------+
|           4 | angel      |             1 | Human Resources |
|           6 | audrika    |             2 | Engineering     |
|           3 | ruby       |             2 | Engineering     |
|           2 | chandana   |             2 | Engineering     |
|           1 | swathi     |             2 | Engineering     |
|        NULL | NULL       |             3 | Sales           |
|           5 | roshan     |             4 | R&D             |
+-------------+------------+---------------+-----------------+
7 rows in set (0.00 sec)

mysql> select employees.employee_id,first_name, departments.department_id,departments.department_name from employees left join departments on employ
ees.department_id=departments.department_id ;
+-------------+------------+---------------+-----------------+
| employee_id | first_name | department_id | department_name |
+-------------+------------+---------------+-----------------+
|           1 | swathi     |             2 | Engineering     |
|           2 | chandana   |             2 | Engineering     |
|           3 | ruby       |             2 | Engineering     |
|           4 | angel      |             1 | Human Resources |
|           5 | roshan     |             4 | R&D             |
|           6 | audrika    |             2 | Engineering     |
+-------------+------------+---------------+-----------------+
6 rows in set (0.00 sec)

mysql> select employees.employee_id,first_name, departments.department_id,departments.department_name from employees right join departments on employees.department_id=departments.department_id;
+-------------+------------+---------------+-----------------+
| employee_id | first_name | department_id | department_name |
+-------------+------------+---------------+-----------------+
|           4 | angel      |             1 | Human Resources |
|           6 | audrika    |             2 | Engineering     |
|           3 | ruby       |             2 | Engineering     |
|           2 | chandana   |             2 | Engineering     |
|           1 | swathi     |             2 | Engineering     |
|        NULL | NULL       |             3 | Sales           |
|           5 | roshan     |             4 | R&D             |
+-------------+------------+---------------+-----------------+
7 rows in set (0.00 sec)


mysql> select *from employees right join departments on employees.department_id=departments.department_id;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+---------------+-----------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id | department_id | department_name |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+---------------+-----------------+
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |             1 | Human Resources |
|           6 | audrika    | borah     | audrika@gmail.com  | 8000099999   | 2024-07-04 | senior data scientist    | 1200000.00 |             2 |       NULL |             2 | Engineering     |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |             2 | Engineering     |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |             2 | Engineering     |
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |             2 | Engineering     |
|        NULL | NULL       | NULL      | NULL               | NULL         | NULL       | NULL                     |       NULL |          NULL |       NULL |             3 | Sales           |
|           5 | roshan     | reddy     | roshan@gmail.com   | 8000899999   | 2024-07-04 | associate R&D            | 1200000.00 |             4 |       NULL |             4 | R&D             |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+---------------+-----------------+
7 rows in set (0.00 sec)

mysql> select *from employees where employee_id=1;
+-------------+------------+-----------+------------------+--------------+------------+--------------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email            | phone_number | hire_date  | job_title                | salary     | department_id | manager_id |
+-------------+------------+-----------+------------------+--------------+------------+--------------------------+------------+---------------+------------+
|           1 | swathi     | srinivas  | swathi@gmail.com | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
+-------------+------------+-----------+------------------+--------------+------------+--------------------------+------------+---------------+------------+
1 row in set (0.00 sec)

mysql> select avg(salary) from employees;
+----------------+
| avg(salary)    |
+----------------+
| 1200000.000000 |
+----------------+
1 row in set (0.00 sec)

mysql> update employees set salary=2000000 where employee_id=6;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select *from employees order by salary asc;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |
|           5 | roshan     | reddy     | roshan@gmail.com   | 8000899999   | 2024-07-04 | associate R&D            | 1200000.00 |             4 |       NULL |
|           6 | audrika    | borah     | audrika@gmail.com  | 8000099999   | 2024-07-04 | senior data scientist    | 2000000.00 |             2 |       NULL |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
6 rows in set (0.00 sec)

mysql> select *from employees order by salary desc;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
|           6 | audrika    | borah     | audrika@gmail.com  | 8000099999   | 2024-07-04 | senior data scientist    | 2000000.00 |             2 |       NULL |
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |
|           5 | roshan     | reddy     | roshan@gmail.com   | 8000899999   | 2024-07-04 | associate R&D            | 1200000.00 |             4 |       NULL |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
6 rows in set (0.00 sec)
mysql> select count(manager_id) from employees group by manager_id;
+-------------------+
| count(manager_id) |
+-------------------+
|                 0 |
|                 4 |
+-------------------+
2 rows in set (0.00 sec)

mysql> select max(salary) from employees group by salary;
+-------------+
| max(salary) |
+-------------+
|  1200000.00 |
|  2000000.00 |
+-------------+
2 rows in set (0.00 sec)

mysql> select max(salary) from employees group by salary order by salary desc;
+-------------+
| max(salary) |
+-------------+
|  2000000.00 |
|  1200000.00 |
+-------------+
2 rows in set (0.00 sec)

mysql> select salary from employees group by salary order by salary desc;
+------------+
| salary     |
+------------+
| 2000000.00 |
| 1200000.00 |
+------------+
2 rows in set (0.00 sec)

mysql> select *from employees where salary>1000000;
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email              | phone_number | hire_date  | job_title                | salary     | department_id | manager_id |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
|           1 | swathi     | srinivas  | swathi@gmail.com   | 8000009999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           2 | chandana   | narthu    | chandana@gmail.com | 8888899999   | 2024-07-04 | Associate data scientist | 1200000.00 |             2 |          6 |
|           3 | ruby       | elik      | ruby@gmail.com     | 8088899999   | 2024-07-04 | Associate data engineer  | 1200000.00 |             2 |          6 |
|           4 | angel      | sajhu     | angel@gmail.com    | 8008899999   | 2024-07-04 | HR                       | 1200000.00 |             1 |          6 |
|           5 | roshan     | reddy     | roshan@gmail.com   | 8000899999   | 2024-07-04 | associate R&D            | 1200000.00 |             4 |       NULL |
|           6 | audrika    | borah     | audrika@gmail.com  | 8000099999   | 2024-07-04 | senior data scientist    | 2000000.00 |             2 |       NULL |
+-------------+------------+-----------+--------------------+--------------+------------+--------------------------+------------+---------------+------------+
6 rows in set (0.00 sec)

mysql> select *from employees where salary>1200000;
+-------------+------------+-----------+-------------------+--------------+------------+-----------------------+------------+---------------+------------+
| employee_id | first_name | last_name | email             | phone_number | hire_date  | job_title             | salary     | department_id | manager_id |
+-------------+------------+-----------+-------------------+--------------+------------+-----------------------+------------+---------------+------------+
|           6 | audrika    | borah     | audrika@gmail.com | 8000099999   | 2024-07-04 | senior data scientist | 2000000.00 |             2 |       NULL |
+-------------+------------+-----------+-------------------+--------------+------------+-----------------------+------------+---------------+------------+
1 row in set (0.00 sec)

mysql> select count(job_title) from employees where job_title= "Associate data scientist";
+------------------+
| count(job_title) |
+------------------+
|                2 |
+------------------+
1 row in set (0.00 sec)mysql> select *from projects;
+------------+--------------------+
| project_id | project_name       |
+------------+--------------------+
|          1 | fraud_detection    |
|          2 | text_summarization |
|          3 | automation         |
|          4 | generative_ai      |
+------------+--------------------+
4 rows in set (0.00 sec)

mysql> select *from employee_projects;
+-------------+------------+
| employee_id | project_id |
+-------------+------------+
|           2 |          1 |
|           4 |          1 |
|           1 |          2 |
|           3 |          3 |
|           5 |          4 |
+-------------+------------+
5 rows in set (0.00 sec)
mysql> select employees.employee_id, employees.first_name,employees.manager_id, employee_projects.project_id from employees left join employee_projects on employee_projects.employee_id=employees.employee_id;
+-------------+------------+------------+------------+
| employee_id | first_name | manager_id | project_id |
+-------------+------------+------------+------------+
|           1 | swathi     |          6 |          2 |
|           2 | chandana   |          6 |          1 |
|           3 | ruby       |          6 |          3 |
|           4 | angel      |          6 |          1 |
|           5 | roshan     |       NULL |          4 |
|           6 | audrika    |       NULL |       NULL |
+-------------+------------+------------+------------+
6 rows in set (0.00 sec)

mysql> select count(project_id) from projects group by project_id;
+-------------------+
| count(project_id) |
+-------------------+
|                 1 |
|                 1 |
|                 1 |
|                 1 |
+-------------------+
4 rows in set (0.00 sec)

mysql> select count(project_id), project_id from projects group by project_id;
+-------------------+------------+
| count(project_id) | project_id |
+-------------------+------------+
|                 1 |          1 |
|                 1 |          2 |
|                 1 |          3 |
|                 1 |          4 |
+-------------------+------------+
4 rows in set (0.00 sec)
mysql> select employees.employee_id, employees.first_name,employees.manager_id, employee_projects.project_id, projects.project_name from employees left join employee_projects on employee_projects.employee_id=employees.employee_id inner join projects on employee_projects.project_id=projects.project_id;
+-------------+------------+------------+------------+--------------------+
| employee_id | first_name | manager_id | project_id | project_name       |
+-------------+------------+------------+------------+--------------------+
|           2 | chandana   |          6 |          1 | fraud_detection    |
|           4 | angel      |          6 |          1 | fraud_detection    |
|           1 | swathi     |          6 |          2 | text_summarization |
|           3 | ruby       |          6 |          3 | automation         |
|           5 | roshan     |       NULL |          4 | generative_ai      |
+-------------+------------+------------+------------+--------------------+
5 rows in set (0.00 sec)

mysql> create view EmployeeProjectDetails as select employees.employee_id, employees.first_name,employees.manager_id, employee_projects.project_id, projects.project_name from employees left join employee_projects on employee_projects.employee_id=employees.employee_id inner join projects on employee_projects.project_id=projects.project_id;
Query OK, 0 rows affected (0.01 sec)

mysql> select *from EmployeeProjectDetails;
+-------------+------------+------------+------------+--------------------+
| employee_id | first_name | manager_id | project_id | project_name       |
+-------------+------------+------------+------------+--------------------+
|           2 | chandana   |          6 |          1 | fraud_detection    |
|           4 | angel      |          6 |          1 | fraud_detection    |
|           1 | swathi     |          6 |          2 | text_summarization |
|           3 | ruby       |          6 |          3 | automation         |
|           5 | roshan     |       NULL |          4 | generative_ai      |
+-------------+------------+------------+------------+--------------------+
5 rows in set (0.00 sec)
