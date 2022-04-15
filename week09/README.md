# Task 1
Function code:

```
CREATE OR REPLACE FUNCTION public.ex1_retrieve_addresses_under_condition()
    RETURNS table (id integer, address text)
    LANGUAGE 'sql'
    COST 100
    IMMUTABLE PARALLEL UNSAFE
AS $$
SELECT a.address_id, a.address
from address as a
where (a.city_id <= 600) and (a.city_id >=400) and (a.address like '%11%')
$$;
```

Python code:

```
import psycopg2
import geopy
from geopy.geocoders import Nominatim
con = psycopg2.connect(database="Dvdrental", user="postgres",
                       password="2791", host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()
cur.execute("select * from ex1_retrieve_addresses_under_condition()")
a = cur.fetchall()
# print (a)
b = []
geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36")


for i in range (len(a)):
    try:
        location = geolocator.geocode(a[i][1])
        b.append([a[i][0], a[i][1], location.latitude, location.longitude])
    except:
        b.append( [a[i][0], a[i][1], 0,0] )

# print (len(b))
# print (b)

for i in range (len(a)):
    cur.execute(f"update address set latitude = {b[i][2]}, longitude = {b[i][3]} where address_id = {b[i][0]}")

con.commit()
```

Picture:

![image](https://user-images.githubusercontent.com/54617201/163574325-847f6b0c-0dc8-4c63-bc3b-1b9c36add48b.png)

# Task 2
Function code:
```
-- DROP FUNCTION ex2_paging(integer,integer)

CREATE OR REPLACE FUNCTION public.ex2_paging( num_from int, num_to int )
    RETURNS table (id integer, first_name character varying(45), last_name character varying(45), address_id smallint)    
AS $$
begin
if num_from > num_to 
then
	raise exception 'illegal order';
elseif num_from<0 or num_to<0 then
	raise exception 'some arguments are negative';
elseif num_from>600 or num_to>600 then
	raise exception 'some arguments are more than 600';
else
	return query SELECT c.customer_id, c.first_name, c.last_name, c.address_id
	from customer as c
	order by c.address_id
	limit num_to-num_from
	offset num_from;
end if;
end;
$$
LANGUAGE 'plpgsql';
```

Example code:
```
select * from ex2_paging(20, 30)
```

Picture:

![image](https://user-images.githubusercontent.com/54617201/163580227-b8fc7585-77e5-4a01-9691-cb22722fa8b4.png)
