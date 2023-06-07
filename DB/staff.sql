
create table if not exists Departments (
	id SERIAL primary key,
	name VARCHAR(40)
);

create table if not exists Managers (
	id SERIAL primary key,
	name VARCHAR(80),
	employee_id INTEGER references Employees(id)
);

create table if not exists Employees (
	id SERIAL primary key,
	name VARCHAR(80),
	department_id INTEGER references Departments(id),
	manager_id INTEGER references Managers(id),
	manager BOOLEAN
);

alter table Managers
add employee_id Integer references Employees(id);