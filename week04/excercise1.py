#!/bin/env python

import numpy as np
import pandas as pd

df=pd.DataFrame({
    "id":np.random.randint(100,2000,50) ,
    "salary":np.random.randint(5,50,50),
    "age":np.random.randint(15,50,50)
    })

# 1. SELECT * FROM data;
print(df[:])

# 2. SELECT * FROM data LIMIT 10;
print(df.head(10))

# 3.  SELECT id FROM data;  //id 是 data 表的特定一列
print(df['id'])

# 4. SELECT COUNT(id) FROM data;
print(df['id'].count())

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
print(df[(df['id']<1000) & (df['age']>30)])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
ids = [1001, 975, 1039, 875]
df1 = pd.DataFrame({
    "id": [ ids[x] for x in np.random.randint(0,len(ids),50) ],
    "ages": np.random.randint(20,50,50)
})
print(df1.groupby('id').count())

raw_data_1 = {
        'id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

df1 = pd.DataFrame(raw_data_1, columns=["id","first_name","last_name"])
df2 = pd.DataFrame(raw_data_2, columns=["id","first_name","last_name"])

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
df = pd.merge(df1, df2, on="id", how="inner")
print(df)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
df = pd.concat([df1,df2])
print(df)

# 9. DELETE FROM table1 WHERE id=10;
raw_data = {
        'id': ['1', '2', '3', '4', '5', '10'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung', 'GeeK'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches', 'Times']}

df3 = pd.DataFrame(raw_data, columns=['id','first_name','last_name'])
df3 = df3[df3['id']!='10']
print(df3)

# 10. ALTER TABLE table1 DROP COLUMN column_name;
df4=pd.DataFrame({
    "id":np.random.randint(100,2000,50) ,
    "column_name":np.random.randint(15,50,50)
    })
df4 = df4.drop(columns='column_name')
print(df4)


