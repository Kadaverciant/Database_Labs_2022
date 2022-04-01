#  Task 1
- Find the names of suppliers who supply some red part. 
```
SELECT S.sname
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and P.color='Red';
```
![image](https://user-images.githubusercontent.com/54617201/161285672-a99b4fcc-1171-4728-96aa-a74f5793e158.png)

- Find the sids of suppliers who supply some red or green part. 
```
SELECT S.sid
FROM Suppliers AS S, Parts AS P, Catalog AS C
WHERE C.sid=S.sid and P.pid=C.pid and (P.color='Red' or P.color='Green');
```
![image](https://user-images.githubusercontent.com/54617201/161285956-1dfbabdf-28f7-49d7-a8da-e0e21d00b028.png)
