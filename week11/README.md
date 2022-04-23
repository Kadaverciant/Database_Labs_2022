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
Lets's create everythin what we need:
```
create table account (
    username varchar(45) primary key ,
    fullname varchar(45),
    balance int,
    group_id int
);

insert into account (username, fullname, balance, group_id)
values ('jones', 'Alice Jones', 82, 1),
('bitdiddl', 'Ben Bitdiddle', 65, 1),
('mike', 'Michael Dole', 73, 2),
('alyssa', 'Alyssa P. Hacker', 79, 3),
('bbrown', 'Bob Brown', 100, 3 );
```
### For read commited
Terminal 1
```
begin isolation level read committed; -- step 1
    select * from account; -- step 1
    select * from account; -- step 3
    select * from account; -- step 5.2
    update account set balance = balance + 10 where fullname = 'Alice Jones'; -- step 7
commit; -- step 9
```

Terminal 2
```
begin isolation level read committed; -- step 2
    update account set username = 'ajones' where fullname = 'Alice Jones'; -- step 2
    select * from account; -- step 4
commit; -- step 5.1
select * from account; -- step 5.2
begin isolation level read committed; -- step 6
    update account set balance = balance + 20 where fullname = 'Alice Jones'; -- step 8
rollback; -- step 10
```

1) Do both terminals show the same information? Explain the reason

Answer: They would show different information since we use read commited isolation level, in which only commited difference will be applied to data base. So, T1 would see only 'jones', not 'ajones'.

2) Explain the output form the second terminal:

Answer: After step 2 Terminal 2 would wait until Terminal 1 would commit changes and Terminal 2 would consider information about balance after changes.

### For repeatable read:
Terminal 1
```
begin isolation level repeatable read; -- step 1
    select * from account; -- step 1
    select * from account; -- step 3
    select * from account; -- step 5.2
    update account set balance = balance + 10 where fullname = 'Alice Jones'; -- step 7
commit; -- step 9
```

Terminal 2
```
begin isolation level repeatable read; -- step 2
    update account set username = 'ajones' where fullname = 'Alice Jones'; -- step 2
    select * from account; -- step 4
commit; -- step 5.1
select * from account; -- step 5.2
begin isolation level repeatable read; -- step 6
    update account set balance = balance + 20 where fullname = 'Alice Jones'; -- step 8
rollback; -- step 10
```
1) Do both terminals show the same information? Explain the reason

Answer: They would show different information since we use repeatable read isolation level, in which transactions only sees data committed before the transaction began. So in Terminal 1 we won't see any changes.

2) Explain the output form the second terminal:

Answer: ERROR:  could not serialize access due to concurrent update - which indicates that the UPDATE statement was queued behind another UPDATE statement on the same row.

## 2.2
### For read commited

After commiting T1 and T2, Mike balance would be increased by 15, and Bob group would be changed to 2.
Since all updates happened befor commits, Bob balance won't be increased. In other words, if update in Terminal 2 would be commited befor update in Terminal 1, then Bob's balance would be changed.

 username |     fullname     | balance | group_id 
----------+------------------+---------+----------
 bitdiddl | Ben Bitdiddle    |      65 |        1
 alyssa   | Alyssa P. Hacker |      79 |        3
 ajones   | Alice Jones      |      82 |        1
 bbrown   | Bob Brown        |     100 |        2
 mike     | Michael Dole     |      88 |        2

Terminal 1:
```
begin isolation level read committed; -- step 1
    select * from account where group_id = 2; -- step 2
    select * from account where group_id = 2; -- step 4
    update account set balance = balance +15 where group_id = 2; -- step 5
commit; -- step 6
```

Terminal 2:
```
begin isolation level read committed; -- step 1
    update account set group_id = 2 where fullname = 'Bob Brown' -- step 3
commit; -- step 6
```
### For repeatable read:

Situation would be the same as for read commited. 

After commiting T1 and T2, Mike balance would be increased by 15, and Bob group would be changed to 2.
However, even if T2 would be commited before update in T1, Bob balance won't be increased.
