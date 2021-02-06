# seed script to populated pour decisions db

import os
import crud
import server

# import all model classes and functions to talk to db
from model import db, connect_to_db, User, Wine, Cheese, Pair, Rating
import psycopg2
import pandas as pd

from sqlalchemy import create_engine
engine = create_engine('postgresql://Loranne@localhost:5432/pourdecisions')


# drop then recreate to start db from scratch
os.system("dropdb pourdecisions")
os.system("createdb pourdecisions")

# once that's done, we connect
connect_to_db(server.app)
# and create our model classes inside the db
db.create_all()

# populate cheeses table from csv
cheese_file = open("cheese.csv", "r")
next(cheese_file)

for row in cheese_file:
    fields = row.split("|") 
    for field in fields:
        if field == "":
            field = None

    cheese_name, cheese_pronunciation, cheese_region, cheese_density, cheese_description, cheese_bio, cheese_animal, cheese_img, cheese_sub = fields

    crud.create_cheese(cheese_name, cheese_pronunciation, cheese_region, cheese_density, 
                        cheese_description, cheese_bio, cheese_animal, cheese_img, 
                        cheese_sub)
    
cheese_file.close()

# populate wines table
wine_file = open("wine.csv", "r")
next(wine_file)

for row in wine_file:
    fields = row.split("|") 
    # converting sparkling values to true booleans
    # have to enumerate because field in fields is just a local variable and doesn't
    # persist beyond the loop (and we have to crud.create outside the loop)
    for i, field in enumerate(fields):
        if fields[i] == "":
            fields[i] = None
        elif fields[i] == "T":
            fields[i] = True
        elif fields[i] == "F":
            fields[i] = False

    wine_name, wine_pronunciation, wine_color, wine_sparkling, wine_region, wine_country, wine_bio, wine_img, wine_sub = fields

    crud.create_wine(wine_name, wine_pronunciation, wine_color, wine_sparkling,
                        wine_region, wine_country, wine_bio, wine_img, wine_sub)
    
wine_file.close()

# create a fake user record
crud.create_user("Your", "Mom", "fetaoffdead@no.com", "1234007")

# populate pairs table
pairs_file = open("pairs.csv", "r")
next(pairs_file)

for row in pairs_file:
    fields = row.split(",") 

    cheese_id, wine_id, user_id = fields

    crud.create_pair(cheese_id=cheese_id, wine_id=wine_id, user_id=user_id )
    
pairs_file.close()


#################### Other solutions I didn't use ###################

# # reads csv file and saves as pandas dataframe
# cheese_data = pd.read_csv("cheese.csv")

# # sets column names to first row of data
# cheese_data.columns = cheese_data.iloc[0]

# # takes slice of all data after first row
# cheese_data = cheese_data[1:]

# # dumps data into table
# cheese_data.to_sql('cheeses', engine)

# conn = psycopg2.connect("host=localhost dbname=pourdecisions user=postgres")
# cur = conn.cursor()

# with open("cheese.csv", "r") as cheeses:
    # next(cheeses)
    # cur.copy_from(cheeses, "cheeses", sep=",")

# # populate wines table from csv
# with open("wine.csv", "r") as wines:
#     next(wines)
#     cur.copy_from(wines, "wines", sep=",")

# # commit those
# conn.commit()