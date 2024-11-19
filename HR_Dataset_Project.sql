-- 1. List all employees' names and their job titles.

SELECT e.first_name, e.last_name, j.job_title
FROM employees e 
JOIN jobs j ON e.job_id = j.job_id

-- 2. Display the employee names and their department name.

SELECT e.first_name, e.last_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id

-- 3. List the names of all departments and the average salary of the employees in each department

SELECT d.department_name, ROUND(AVG(e.salary)) AS average_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name

-- 4. Create a query that returns  employee id, first, last name salary and a new column named ''salary_category'' that calculates salary category as
--following:
----''Associate'' for salary =<3000
----''Senior'' for 3000 <salary =<5000
----''Manager'' for 5000<salary <10000
----''Executive' for salary>=10000
----ordered by descending salary.

select
   employee_id,
   first_name,
   last_name,
   salary,
   case
           when salary <= 3000 then 'associate'
           when salary <= 5000 then 'senior'
           when salary < 10000 then 'manager'
           when salary >= 10000 then 'executive'
   end  as salary_category
from
   employees
order by
   salary desc ;

-- 5. Use above query as nested in a new one to group ''salary_category'' and count employees per category

select salary_category, count(employee_id) from (
select
   employee_id,
   first_name,
   last_name,
   salary,
   case
           when salary <= 3000 then 'associate'
           when salary <= 5000 then 'senior'
           when salary < 10000 then 'manager'
           when salary >= 10000 then 'executive'
   end  as salary_category
from
   employees) as foo
group by salary_category

-- 6. Create a query that returns employee id, first name, last name from ''employees'' table and
--its dependants first name, last name and relationship from "dependents'' table

select employees.employee_id, employees.first_name ,employees.last_name, dependents.first_name, dependents.last_name, dependents.relationship
from employees inner join dependents
on employees.employee_id = dependents.employee_id
order by employees.employee_id

-- 7. Create  a query that returns department_name, department_id and how many employees each department occupies

select
   min(employees.department_id) as dpt_id,
   count(employees.employee_id) as No_of_employees ,
   departments.department_name
from
   employees
left join departments on
   employees.department_id = departments.department_id
group by
   departments.department_id
order by
   department_name

-- 8. Create a query that returns employee id,first_name,last_name,salary.
----Also calculate for each one the percentage of his salary to the max_salary he could enjoy for his job type.
----Sort results from the greatest percentage to the lower.
----Bonus: Can you demonstrate the calculated percentage with 2 decimals only?

select
   employees.employee_id ,
   employees.first_name,
   employees.last_name ,
   employees.salary ,
   Round(employees.salary / jobs.max_salary, 2) as percentage
from
   employees
left join jobs on
   employees.job_id = jobs.job_id
order by
   percentage desc

-- 9. Find the names of all employees, along with the names of their departments and the names of their jobs.

SELECT e.first_name, e.last_name, d.department_name, j.job_title
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN jobs j ON e.job_id = j.job_id;

-- 10. List the first name and last name of employees, their managers' names, and the department names.

SELECT e.first_name, e.last_name, m.first_name AS manager_first_name, m.last_name AS manager_last_name, d.department_name
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
JOIN departments d ON e.department_id = d.department_id;


-- 11. Find pairs of employees where one reports to the other, and they work in the same department.

SELECT E1.last_name AS Manager, E2.last_name AS Subordinate, D.department_name
FROM employees E1
JOIN employees E2 ON E1.employee_id = E2.manager_id
JOIN departments D ON E1.department_id = D.department_id AND E2.department_id = D.department_id;