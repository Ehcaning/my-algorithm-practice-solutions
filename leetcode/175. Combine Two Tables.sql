select
    Person.firstName as 'firstName',
    Person.lastName as 'lastName',
    Address.city as 'city',
    Address.state as 'state'
from Person
left join Address on Address.personId = Person.personId
