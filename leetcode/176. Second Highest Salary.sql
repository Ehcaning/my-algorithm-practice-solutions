select
    max(salary) as SecondHighestSalary
from Employee
where salary != (select salary from Employee order by salary desc limit 1)
