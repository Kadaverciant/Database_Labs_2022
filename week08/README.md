# Task 1
## 1st query
```
explain analyze select name from customer where name = 'Amy Cox'
```
before:

![image](https://user-images.githubusercontent.com/54617201/162440389-4671ce19-f233-4580-a169-a2d8fbd0301f.png)

after creating btree index for name:

![image](https://user-images.githubusercontent.com/54617201/162441022-6a3fe2ba-b085-413c-9cb7-7cafe402df39.png)

Conclusion: As we can see, after creating an index, cost and time decreased.

## 2nd query
```
explain analyze select review from customer where length(review) < 25
```
before:

![image](https://user-images.githubusercontent.com/54617201/162434392-d52eac6a-71b5-43c3-ae3b-60139621d7e9.png)

after creating btree index for review:
![image](https://user-images.githubusercontent.com/54617201/162436993-7bf20d51-7034-483d-ac33-f7f1c8ace7bd.png)

Conclusion: As we can see, after creating an index, nothing changed. That's ok, since btree can't influence on length function.

## 3rd query 
```
explain analyze select id from customer where id = 13 or id = 5675 or id = 177013
```
before:

![image](https://user-images.githubusercontent.com/54617201/162434550-05f19c52-edd0-459c-8968-09de73ca24fd.png)

after creating hash index for id:

![image](https://user-images.githubusercontent.com/54617201/162435326-28eb1cd0-981b-48cf-be64-acd51d218ebb.png)

Conclusion: As we can see, after creating an index, cost and time decreased.

# Task 2
## 1st query
```
select f.film_id, f.title, f.rating 
from film as f, category as c, film_category as fc, 
(select distinct f.film_id
from film as f 
except (
select distinct f.film_id 
from film as f, inventory as i, rental as r
where f.film_id = i.film_id and i.inventory_id = r.inventory_id)) as unrented 
where f.film_id=unrented.film_id and (rating = 'R' or rating = 'PG-13') and 
f.film_id=fc.film_id and fc.category_id = c.category_id and (c.name='Horror' or 
c.name='Sci-Fi')
```
![image](https://user-images.githubusercontent.com/54617201/162475507-2e77f568-b783-4ac8-bf34-d6f93ce07daf.png)


## 2nd query
```
select a.city, st.store_id, st.money, st.address_id  from 
(
select distinct a.address_id, c.city
from address as a, city as c
where a.city_id=c.city_id
) as a join ( 
	select s.store_id, s.money, st.address_id 
	from
	(
		select s.store_id, sum(money) as money
		from (
		select staff_id, sum(amount) as money
		from payment --, staff as s
		where payment_date >=  
			(select max(payment_date) from payment)- interval '1 month'
		 group by staff_id
		) as bill, staff as sf, store as s
		where bill.staff_id = sf.staff_id and s.store_id = sf.store_id
		group by s.store_id
	) as s join store as st on s.store_id = st.store_id
) as st on a.address_id = st.address_id
```
![image](https://user-images.githubusercontent.com/54617201/162475424-abb5e933-7195-47be-9abe-82c4405a93b0.png)
