# seed script to populated pour decisions db

import os
import crud

# import all model classes and functions to talk to db
from model import db, connect_to_db, User, Wine, Cheese, Pair, Rating

# drop then recreate to start db from scratch
os.system("dropdb pour-decisions")
os.system("createdb pour-decisions")

# once that's done, we connect
connect_to_db(server.app)
# and create our model classes inside the db
db.create_all()


