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

Now let's create transition:

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
	
	rollback to savepoint my_savepoint1;
end;
```

In case if you are working in pgAdmin, you might need this:

```
update accounts set credit = 1000;
```

Now let's add new column:

```
alter table accounts add column bankName varchar(45);
update accounts set bankname = 'Sberbank' where id = 1 or id = 3;
update accounts set bankname = 'Tinkoff' where id = 2;
```
