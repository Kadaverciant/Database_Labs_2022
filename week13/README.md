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

## 1.1
```
match (p:Fighter)-[:beats]-(pp) where p.weight="155" or p.weight="170" or p.weight="185" return distinct p
```
![image](https://user-images.githubusercontent.com/54617201/165946982-48483e83-e33c-491a-98bd-d92e76661370.png)
