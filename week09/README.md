# Task 1
function:
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

Python code 
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
![image](https://user-images.githubusercontent.com/54617201/163573605-f5c2e673-a63f-42f9-8482-bc21ff90e6e1.png)

