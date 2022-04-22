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

Now let's create transition, you can uncomment any save point if you need to rollback:

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

Accounts table would be:

![image](https://user-images.githubusercontent.com/54617201/164748398-1748cf45-7020-495b-8849-6b6ad32baeae.png)

## 1.3

Let's create new table Ledger:

```
create table ledger (
	id int primary key,
	fromID int,
	toID int,
	fee int,
	amount int,
	TransactionDateTime timestamp,
	constraint fk_from foreign key(fromID) references accounts(id),
	constraint fk_to foreign key(toID) references accounts(id)
);
```
Then let's modify our transition:
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
	
	insert into ledger (id, fromID, toID, fee, amount, TransactionDateTime) 
	values (1,1,3,0,500, '2022-11-14');
	
	savepoint my_savepoint2;
	
	update accounts
	set credit = credit - 700
	where id = 2;
	
	update accounts
	set credit = credit + 670
	where id = 1;
	
	update accounts set credit = credit + 30 where id = 4;
	insert into ledger (id, fromID, toID, fee, amount, TransactionDateTime) 
	values (2,2,1,30,670, '2022-11-13');
	
	savepoint my_savepoint3;
	
	update accounts
	set credit = credit - 100
	where id = 2;
	
	update accounts
	set credit = credit + 70
	where id = 3;
	
	update accounts set credit = credit + 30 where id = 4;
	insert into ledger (id, fromID, toID, fee, amount, TransactionDateTime) 
	values (3,2,3,30,70, '2022-11-12');
-- 	rollback to savepoint my_savepoint3;
-- 	rollback to savepoint my_savepoint2;
-- 	rollback to savepoint my_savepoint1;
end;
```

Ledger table would be:

![image](https://user-images.githubusercontent.com/54617201/164751980-c6cc2dec-6f53-4ccc-a239-d7abdd850a0c.png)

# Task 2
## 2.1
### For read commited
1) Do both terminals show the same information? Explain the reason

Answer: They would show different information since we use read commited isolation level, in which only commited difference will be applied to data base. So, T1 would see only 'jones', not 'ajones'.

Terminal 1
```
set transaction isolation level read committed read write;
begin;
    select * from account;
commit;
select * from account;
```

Terminal 2
```
begin isolation level read committed;
    update account set username = 'ajones' where username = 'jones';

    select * from account;
rollback;
select * from account;
```

2) Explain the output form the second terminal:

Answer: After step 2 Terminal 2 would wait until Terminal 1 would commit changes and Terminal 2 would consider information about balance after changes.

Terminal 1
```
set transaction isolation level read committed read write;
begin;
    select * from account;
commit;
select * from account;

update account set balance = balance + 10 where username='ajones';
commit;
```

Terminal 2
```
begin isolation level read committed;
    update account set username = 'ajones' where username = 'jones';
    select * from account;
commit;

begin isolation level read committed;
    update account set balance = balance + 20 where username='ajones';
rollback;
```
