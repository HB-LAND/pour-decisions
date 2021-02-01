"""CRUD operations."""


from model import db, connect_to_db, User, Wine, Cheese, Pair, Rating


def create_user(fname, lname, email, password):
    """Create and return a new user"""

    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_wine(wine_name, wine_color, wine_region, wine_bio, wine_img):
    """Create and return a wine."""

    wine = Wine(wine_name=wine_name,
                wine_color=wine_color,
                wine_region=wine_region,
                wine_bio=wine_bio,
                wine_img=wine_img)

    db.session.add(wine)
    db.session.commit()

    return wine


def create_cheese(cheese_name, cheese_pronunciation, cheese_region, cheese_density, 
                    cheese_description, cheese_bio, cheese_animal, cheese_img, 
                    cheese_sub):
    """Create and return a cheese."""

    cheese = Cheese(cheese_name=cheese_name, cheese_pronunciation=cheese_pronunciation, 
                    cheese_region=cheese_region, cheese_density=cheese_density, 
                    cheese_description=cheese_description, cheese_bio=cheese_bio,
                    cheese_animal=cheese_animal, cheese_img=cheese_img, 
                    cheese_sub=cheese_sub)

    db.session.add(cheese)
    db.session.commit()

    return cheese


def create_pair(user_id, wine_id, cheese_id, user_made):
    """Creates a paired wine and cheese based on a user's selection"""

    pair = Pair(user_id=user_id,
                wine_id=wine_id,
                cheese_id=cheese_id,
                user_made=user_made)

    db.session.add(pair)
    db.session.commit()

    return pair


def create_rating(pair_id, user_id, pair_rating):
    """Creates a rating based on a user's like or dislike of a wine and cheese pairing"""

    rating = Rating(pair_id=pair_id,
                    user_id=user_id,
                    pair_rating=pair_rating)


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
