#  Task 1
- Find the names of suppliers who supply some red part. 
```
SELECT distinct(S.sname)
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and P.color='Red';
```
![image](https://user-images.githubusercontent.com/54617201/161287686-ffb434c9-772c-4098-9311-f08b02919451.png)

- Find the sids of suppliers who supply some red or green part. 
```
SELECT distinct(S.sid)
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and (P.color='Red' or P.color='Green');
```
![image](https://user-images.githubusercontent.com/54617201/161287605-d5139dd7-6a09-47ff-9df4-24d55ada0155.png)

- Find the sids of suppliers who supply some red part or are at 221 Packer Street. 
```
SELECT distinct(S.sid)
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and (P.color='Red' or S.address='221 Packer Street');
```
![image](https://user-images.githubusercontent.com/54617201/161287515-20fa37a6-e729-4b26-ac44-1cf743b6cba7.png)

- Find the sids of suppliers who supply every red or green part. 
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
