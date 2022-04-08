# Task 1
1st query 
```
explain analyze select name from customer where name like 'Amy%'
```
before:

![image](https://user-images.githubusercontent.com/54617201/162434062-a3f717b4-f596-4844-8d47-33c1471db077.png)

after creating btree index for name:

![image](https://user-images.githubusercontent.com/54617201/162436083-6a07e0aa-382c-4c6b-89a2-031ad076d434.png)

2nd query
```
explain analyze select review from customer where length(review) < 25
```
before:
![image](https://user-images.githubusercontent.com/54617201/162434392-d52eac6a-71b5-43c3-ae3b-60139621d7e9.png)

3rd query 
```
explain analyze select id from customer where id = 13 or id = 5675 or id = 177013
```
before:

![image](https://user-images.githubusercontent.com/54617201/162434550-05f19c52-edd0-459c-8968-09de73ca24fd.png)

after creating hash index for id:

![image](https://user-images.githubusercontent.com/54617201/162435326-28eb1cd0-981b-48cf-be64-acd51d218ebb.png)

