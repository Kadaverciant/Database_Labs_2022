# Task 1
Part 1:

![image](https://user-images.githubusercontent.com/54617201/161531564-cb579384-3038-421a-a549-796aac68fa70.png)


Part 2:

![image](https://user-images.githubusercontent.com/54617201/161539061-6d718a4e-3757-43ca-bc79-1129fc227435.png)
```
create table Customers (
	customerId int primary key,
	customerName varchar(45),
	city varchar(20)
);

create table Orders (
	orderId int primary key,
	date varchar(10),
	customerId int,
	constraint fk_orderInfo foreign key(customerId) references Customers(customerId)
);

create table Items (
	itemId int primary key,
	itemName varchar(45),
	price float
);

create table Nomenclature (
	orderId int,
	itemId int,
	quant int,
	constraint fk_ordersO foreign key(orderId) references Orders(orderId),
	constraint fk_ordersI foreign key(itemId) references Items(itemId)
);

insert into Customers (customerId, customerName, city)
values (101, 'Martin', 'Prague'),
	   (107, 'Herman', 'Madrid'),
	   (110, 'Pedro', 'Moscow');
	   

insert into Items (itemId, itemName, price)
values (3786, 'Net', 35.00),
       (4011, 'Racket', 65.00),
	   (9132, 'Pack-3', 4.75),
	   (5794, 'Pack-6', 5.00 ),
	   (3141, 'Cover', 10.00);

insert into Orders (orderId, date, customerId)
values (2301, '23/02/2011', 101),
       (2302, '25/02/2011', 107),
	   (2303, '27/02/2011', 110);

insert into Nomenclature (orderId, itemId, quant)
values (2301, 3786, 3),
       (2301, 4011, 6),
	   (2301, 9132, 8),
	   (2302, 5794, 4),
	   (2303, 4011, 2),
	   (2303, 3141, 2);

select orderId, sum(quant), sum(price*quant) 
from Nomenclature as N, Items as I
where N.itemId=I.itemId
group by orderId;

select C.customerId, C.customerName, C.city
from (select orderId, sum(price*quant) 
from Nomenclature as N, Items as I
where N.itemId=I.itemId
group by orderId
order by sum(price*quant) DESC LIMIT 1) as p, Customers as C,  Orders as O
where O.orderId=p.orderId and O.customerId = C. CustomerId;
```

# Task 2
Part 1:

![image](https://user-images.githubusercontent.com/54617201/161566615-7143d1d8-9ca9-4441-a9f5-a96de1f311d8.png)


Part 2:

![image](https://user-images.githubusercontent.com/54617201/161566677-285affef-f93d-458f-a120-a68180b259b5.png)
```
create table Books (
	book varchar(100) primary key,
	publisher varchar(100)
);

create table Schools (
	school varchar(100),
	teacher varchar(100) primary key
);

create table Classes (
	teacher varchar(100),
	course varchar(100),
	room varchar(10),
	grade varchar(10),
	book varchar(100),
	loanDate Date,
	primary key(teacher, course, loanDate),
	constraint fk_ClassesB foreign key(book) references Books(book), 
	constraint fk_ClassesS foreign key(teacher) references Schools(teacher)
);



insert into Books (book, publisher)
values ('Learning and teaching in early childhood', 'BOA Editions' ),
       ('Preschool,N56', 'Taylor & Francis Publishing'),
	   ('Early Childhood Education N9', 'Prentice Hall'),
	   ('Know how to educate: guide for Parents and ', 'McGraw Hill');
	   
insert into Schools (school, teacher)
values ('Horizon Education Institute','Chad Russell'),
       ('Horizon Education Institute','E.F.Codd'),
	   ('Horizon Education Institute','Jones Smith'),
	   ('Bright Institution','Adam Baker');	   
	   
insert into Classes (teacher, course, room, grade, book, loanDate)
values ('Chad Russell','Logical thinking','1.A01','1st grade',
	   'Learning and teaching in early childhood', '2010-09-09'),
	   ('Chad Russell','Wrtting','1.A01','1st grade',
	   'Preschool,N56', '2010-05-05'),
	   ('Chad Russell','Numerical Thinking','1.A01','1st grade',
	   'Learning and teaching in early childhood', '2010-05-05'),
	   ('E.F.Codd','Spatial, Temporal and Causal Thinking','1.B01','1st grade',
	   'Early Childhood Education N9', '2010-05-06'),
	   ('E.F.Codd','Numerical Thinking','1.B01','1st grade',
	   'Learning and teaching in early childhood', '2010-05-06'),
	   ('Jones Smith','Wrtting','1.A01','2nd grade',
	   'Learning and teaching in early childhood', '2010-09-09'),
	   ('Jones Smith','English','1.A01','2nd grade',
	   'Know how to educate: guide for Parents and ', '2010-05-05'),
	   ('Adam Baker','Logical thinking','2.B01','1st grade',
	   'Know how to educate: guide for Parents and ', '2010-12-18'),
	   ('Adam Baker','Numerical Thinking','2.B01','1st grade',
   	   'Learning and teaching in early childhood', '2010-05-06');

select school, b.publisher, count(b.publisher)
from Classes as c, Books as b, Schools as s
where s.teacher = c.teacher and b.book=c.book
group by school, b.publisher
order by school;

select school, max(loandate), c.teacher 
from Classes as c, Schools as s
where s.teacher = c.teacher
group by school, c.teacher
order by school, max(loandate) Desc limit 2;









```
