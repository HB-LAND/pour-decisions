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

# populate cheeses table from csv
cheese_file = open("cheese.csv", "r")
# next(cheese_file)

for row in cheese_file:
    fields = row.split("|") 
    # for field in fields:
    #     if field == None:
    #         field = " "

    cheese_name, cheese_pronunciation, cheese_region, cheese_density, cheese_description, cheese_bio, cheese_animal, cheese_img, cheese_sub = fields

    crud.create_cheese(cheese_name, cheese_pronunciation, cheese_region, cheese_density, 
                        cheese_description, cheese_bio, cheese_animal, cheese_img, 
                        cheese_sub)
    
cheese_file.close()


# # reads csv file and saves as pandas dataframe
# cheese_data = pd.read_csv("cheese.csv")

# # sets column names to first row of data
# cheese_data.columns = cheese_data.iloc[0]

# # takes slice of all data after first row
# cheese_data = cheese_data[1:]

# # dumps data into table
# cheese_data.to_sql('cheeses', engine)
