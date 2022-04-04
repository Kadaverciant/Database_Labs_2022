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
