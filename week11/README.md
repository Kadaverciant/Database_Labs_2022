# Task 1

## 1.1
Let's create table:

```
create table accounts (
	id int primary key,
	name varchar(45),
	credit int,
	currency varchar(4)
);

insert into accounts (id, name, credit, currency)
values (1, 'account 1', 1000, 'RUB'),
	   (2, 'account 2', 1000, 'RUB'),
	   (3, 'account 3', 1000, 'RUB');
```

Now let's create transition, you can uncomment any savepoint, if you need to rollback:

```
set transaction isolation level read committed read write;
begin;
	savepoint my_savepoint1;
	
	update accounts
	set credit = credit - 500
	where id = 1;
	
	update accounts
	set credit = credit + 500
	where id = 3;
	
-- 	select * from accounts;
	
	savepoint my_savepoint2;
	
	update accounts
	set credit = credit - 700
	where id = 2;
	
	update accounts
	set credit = credit + 700
	where id = 1;
	
-- 	select * from accounts;
	
	savepoint my_savepoint3;
	update accounts
	set credit = credit - 100
	where id = 2;
	
	update accounts
	set credit = credit + 100
	where id = 3;
	
-- 	select * from accounts;
	
-- 	rollback to savepoint my_savepoint3;
-- 	rollback to savepoint my_savepoint2;
-- 	rollback to savepoint my_savepoint1;
end;
```

In case if you are working in pgAdmin, you might need this:

```
update accounts set credit = 1000;
```

## Task 1.2
Now let's add new column:

```
alter table accounts add column bankName varchar(45);
update accounts set bankname = 'Sberbank' where id = 1 or id = 3;
update accounts set bankname = 'Tinkoff' where id = 2;
```

Now let's add new row for collecting information about fee:
```
insert into accounts (id, name, credit, currency)
values (4, 'account 4', 0, 'RUB');
```

In case if you are working in pgAdmin, you might need this:

```
update accounts set credit = 1000;
update accounts set credit = 0 where id = 4;
```

Then according to task, our transition would be the following:
```
set transaction isolation level read committed read write;
begin;
savepoint my_savepoint1;

	update accounts
	set credit = credit - 500
	where id = 1;
	
	update accounts
	set credit = credit + 500
	where id = 3;
	
-- 	select * from accounts;
	
	savepoint my_savepoint2;
	
	update accounts
	set credit = credit - 700
	where id = 2;
	
	update accounts
	set credit = credit + 670
	where id = 1;
	
	update accounts set credit = credit + 30 where id = 4;
	
-- 	select * from accounts;
	
	savepoint my_savepoint3;
	update accounts
	set credit = credit - 100
	where id = 2;
	
	update accounts
	set credit = credit + 70
	where id = 3;
	
	update accounts set credit = credit + 30 where id = 4;
	
-- 	rollback to savepoint my_savepoint3;
-- 	rollback to savepoint my_savepoint2;
-- 	rollback to savepoint my_savepoint1;
end;
```

![image](https://user-images.githubusercontent.com/54617201/164748398-1748cf45-7020-495b-8849-6b6ad32baeae.png)
