#  Task 1
1 - Find the names of suppliers who supply some red part. 
```
SELECT distinct(S.sname)
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and P.color='Red';
```
![image](https://user-images.githubusercontent.com/54617201/161287686-ffb434c9-772c-4098-9311-f08b02919451.png)

2 - Find the sids of suppliers who supply some red or green part. 
```
SELECT distinct(S.sid)
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and (P.color='Red' or P.color='Green');
```
![image](https://user-images.githubusercontent.com/54617201/161287605-d5139dd7-6a09-47ff-9df4-24d55ada0155.png)

3 - Find the sids of suppliers who supply some red part or are at 221 Packer Street. 
```
SELECT distinct(S.sid)
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and (P.color='Red' or S.address='221 Packer Street');
```
![image](https://user-images.githubusercontent.com/54617201/161287515-20fa37a6-e729-4b26-ac44-1cf743b6cba7.png)

4 - Find the sids of suppliers who supply every red or green part. 
```
SELECT sid FROM Suppliers  
WHERE sid not in ( SELECT sid FROM (
(SELECT sid , pid FROM (select pid from Parts WHERE color = 'Red') as p cross join 
(select distinct sid from Suppliers) as sp)
EXCEPT
(SELECT sid , pid FROM Catalog) ) AS r )
or sid in ( select sid from Catalog where pid in 
		   (select pid from Parts where Color='Green'));
```
![image](https://user-images.githubusercontent.com/54617201/161287998-c2d86682-1e70-4dec-ac8d-c7d230c26c30.png)

5 - Find the sids of suppliers who supply every red part or supply every green part. 
```
SELECT sid FROM Suppliers  
WHERE sid not in ( SELECT sid FROM (
(SELECT sid , pid FROM (select pid from Parts WHERE color = 'Red') as p cross join 
(select distinct sid from Suppliers) as sp)
EXCEPT
(SELECT sid , pid FROM Catalog) ) AS r )
or sid not in ( SELECT sid FROM (
(SELECT sid , pid FROM (select pid from Parts WHERE color = 'Green') as p cross join 
(select distinct sid from Suppliers) as sp)
EXCEPT
(SELECT sid , pid FROM Catalog) ) AS r )
```
![image](https://user-images.githubusercontent.com/54617201/161289016-007d8f93-34ee-40da-92b1-f9ed00c69fff.png)

6 - Find pairs of sids such that the supplier with the first sid charges more for some part than the supplier with the second sid. 
```
select distinct(c1.sid, c2.sid )
from Catalog as c1, Catalog as c2
where c1.cost>c2.cost and c1.pid=c2.pid
```
![image](https://user-images.githubusercontent.com/54617201/161290703-4aff0252-62c4-4ab5-ba25-80007b901184.png)

7 - Find the pids of parts supplied by at least two different suppliers.
```
select distinct(c1.pid)
from Catalog as c1, Catalog as c2
where c1.sid!=c2.sid and c1.pid=c2.pid
```
![image](https://user-images.githubusercontent.com/54617201/161291352-cff349f2-e4a1-4345-b88f-8462d85f7ae8.png)

8 - find the average cost of the red parts and green parts for each of the suppliers
```
select c.sid, count(sid), avg(cost), p.color
from Catalog as c, Parts as p
where c.pid=p.pid and p.color='Red'
group by c.sid, p.color
union
select c.sid, count(sid), avg(cost), p.color
from Catalog as c, Parts as p
where c.pid=p.pid and p.color='Green'
group by c.sid, p.color
```
![image](https://user-images.githubusercontent.com/54617201/161296113-cb3bb805-b112-4e35-9f69-73893a5c2017.png)

9 - find the sids of suppliers whose most expensive part costs $50 or more
```
select c.sid, max(cost)
from Catalog as c
where c.cost>=50
group by c.sid
```
![image](https://user-images.githubusercontent.com/54617201/161296867-fb8e203f-4190-45aa-aad1-d7424f801c18.png)

# Task 2
1 - Author ⋈ (author_id=editor) Book
```
select *
from author, book
where author_id=editor
```
![image](https://user-images.githubusercontent.com/54617201/161316261-74c50e16-cb31-412c-bf69-3a2f5205afae.png)

2 - Пauthor_id(Author) − Πeditor(Book)
```
select author_id
from author
where author_id not in (select author_id from author,book where author_id=editor)
```
![image](https://user-images.githubusercontent.com/54617201/161316045-c28c4123-4ea0-4636-8da1-bf41f070b8cd.png)

3 - Пfirst_name,last_name( (Пauthor_id(Author) − Πeditor(Book)) ⋈ Author)
```
select first_name, last_name 
from (select author_id from author where author_id not in (select author_id from author,book where author_id=editor)) as r
natural join author
```
![image](https://user-images.githubusercontent.com/54617201/161315680-5b6beba0-6f7c-45f4-80f3-7d020db4aa09.png)

