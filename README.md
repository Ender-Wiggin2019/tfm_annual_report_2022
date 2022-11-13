# Terraforming Mars Annual Report

## Developed using Django and VueJs

## Starting up project

    - git clone https://github.com/keiken-shin/agrex_assignment.git
    - cd backend
    - python manage.py migrate
    - python manage.py runserver
    - cd frontend
    - npm install
    - npm run serve

## Demo

- You can find the demo [here](http://report.ender.lol)
- Pages are modified from https://github.com/myth984/wechat-report 

### Login Page

![img.png](images/Nov-13-2022%2015-59-45.gif)


### Other Pages

![img_2.png](images/Nov-13-2022%2016-09-14.gif)


## Usage

- Implemented for multi-user website
- Has a hidden sign-up page
- Recommended usage is to insert data (user infos and displayed data) to this database from external source, here is a sample:

```python
from passlib.hash import django_pbkdf2_sha256
import pandas as pd
import json
import sqlite3
# original db
ori = sqlite3.connect('/YOUR_PATH/origin.db')

# target db
dev = sqlite3.connect('/YOUR_PATH/backend/db.sqlite3')

# df is the original data source
df = pd.read_sql_query("select * from data_source", ori).loc[:, ['name', 'password']];
# firstly transform all columns except pk to a json column
output = df[['pk']].assign(res=df.iloc[:,1:].agg(pd.Series.to_json,1))
output.to_sql('account_userdata', con = dev, if_exists = 'append', index = False)

user_df = pd.read_sql_query("select * from users", ori).loc[:, ['name', 'password']];
user_df['is_superuser'] = 0
user_df['is_active'] = 1
user_df['is_staff'] = 0

user_df['password'] = user_df['password'].apply(django_pbkdf2_sha256.encrypt)
user_df.to_sql('account_useraccount', con = dev, if_exists = 'append', index = False)
```
