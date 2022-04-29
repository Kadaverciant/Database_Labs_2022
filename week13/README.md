# Task 1
## Data creation
```
create (kn:Fighter {name:"Khabib Nurmagomedov",weight:"155"}),
(rda:Fighter {name:"Rafael Dos Anjos",weight:"155"}),
(nm:Fighter {name:"Neil Magny",weight:"170"}),
(jj:Fighter {name:"Jon Jones",weight:"205"}),
(dc:Fighter {name:"Daniel Cormier",weight:"205"}),
(mb:Fighter {name:"Michael Bisping",weight:"185"}),
(mh:Fighter {name:"Matt Hamill",weight:"185"}),
(fm:Fighter {name:"Frank Mir",weight:"230"}),
(bv:Fighter {name:"Brandon Vera",weight:"205"}),
(bl:Fighter {name:"Brock Lesnar",weight:"230"}),
(kg:Fighter {name:"Kelvin Gastelum",weight:"185"}),
(kn)-[:beats]->(rda),
(rda)-[:beats]->(nm),
(jj)-[:beats]->(dc),
(mb)-[:beats]->(mh),
(jj)-[:beats]->(bv),
(bv)-[:beats]->(fm),
(fm)-[:beats]->(bl),
(nm)-[:beats]->(kg),
(kg)-[:beats]->(mb),
(mb)-[:beats]->(mh),
(mb)-[:beats]->(kg),
(mh)-[:beats]->(jj)
```
![image](https://user-images.githubusercontent.com/54617201/165946036-fc06f3a9-2fcd-403d-8d96-d7206e35741a.png)

## 1.1 Return all middle/Walter/light weight fighters (155,170,185) who at least have one win. 
```
match (p:Fighter)-[:beats]-(pp:Fighter) where p.weight="155" or p.weight="170" or p.weight="185" return distinct p
```
![image](https://user-images.githubusercontent.com/54617201/165946982-48483e83-e33c-491a-98bd-d92e76661370.png)

## 1.2 Return fighters who had 1-1 record with each other. Use Count from the aggregation functions. 
```
match (p1:Fighter)-[:beats]->(p2:Fighter)-[:beats]->(p1) return p1, p2
```
![image](https://user-images.githubusercontent.com/54617201/165948689-85b2da14-967b-411a-935e-7eeb059d9ec8.png)

## 1.3 Return all fighter that can “Khabib Nurmagomedov” beat them and he didn’t have a fight with them yet.
```
match (kn:Fighter)-[:beats]->(p)-[:beats*1..]->(p1) where kn.name="Khabib Nurmagomedov" return distinct p1
```
![image](https://user-images.githubusercontent.com/54617201/165950215-730e7d6a-089e-4c7c-b857-0593c85f83ea.png)

## 1.4 Return undefeated Fighters(0 loss), defeated fighter (0 wins). 
```
match (p) where not ()-[:beats]->(p) or not (p)-[:beats]->() return p
```
![image](https://user-images.githubusercontent.com/54617201/165954581-ef50aef3-143f-457f-b0ad-56f8f9ac31ac.png)

## 1.5 Return all fighters MMA records and create query to enter the record as a property for a fighter {name, weight, record}. 
```
match (p) return p.name as name, p.weight as weight, size((p)-[:beats]->()) as wins, size(S()-[:beats]->(p)) as losses
```
![image](https://user-images.githubusercontent.com/54617201/165956613-0492a333-c2a9-49bb-a9fd-c7cfcafb7f34.png)
