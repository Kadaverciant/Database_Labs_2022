# Task 1
## 1st query
```
explain analyze select name from customer where name = 'Amy Cox'
```
before:
![image](https://user-images.githubusercontent.com/54617201/162440389-4671ce19-f233-4580-a169-a2d8fbd0301f.png)

after creating btree index for name:
![image](https://user-images.githubusercontent.com/54617201/162441022-6a3fe2ba-b085-413c-9cb7-7cafe402df39.png)

Conclusion: As we can see, after creating an index cost decreased and time increased.

## 2nd query
```
explain analyze select review from customer where length(review) < 25
```
before:

![image](https://user-images.githubusercontent.com/54617201/162434392-d52eac6a-71b5-43c3-ae3b-60139621d7e9.png)

after creating btree index for review:
![image](https://user-images.githubusercontent.com/54617201/162436993-7bf20d51-7034-483d-ac33-f7f1c8ace7bd.png)

Conclusion: As we can see, after creating an index nothing changed. That's ok, since btree can't influence on length function.

## 3rd query 
```
explain analyze select id from customer where id = 13 or id = 5675 or id = 177013
```
before:

![image](https://user-images.githubusercontent.com/54617201/162434550-05f19c52-edd0-459c-8968-09de73ca24fd.png)

after creating hash index for id:

![image](https://user-images.githubusercontent.com/54617201/162435326-28eb1cd0-981b-48cf-be64-acd51d218ebb.png)

Conclusion: As we can see, after creating an index cost decreased and time decreased.
