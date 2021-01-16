"""Models for wine and cheese app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False,)
    password = db.Column(db.String, nullable=False)

    userpair_relationship = db.relationship('UserPair')
    communitypair_relationship = db.relationship('CommunityPair')
    rating_relationship = db.relationship('Rating')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Wine(db.Model):
    """A wine."""

    __tablename__ = "wines"

    wine_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    wine_name = db.Column(db.String, nullable=False)
    wine_color = db.Column(db.String, nullable=False)
    wine_region = db.Column(db.String, nullable=False)
    wine_bio = db.Column(db.Text, nullable=False)
    wine_img = db.Column(db.String)

    userpair_relationship = db.relationship('UserPair')
    communitypair_relationship = db.relationship('CommunityPair')

    def __repr__(self):
        return f'<Wine Information wine_id={self.wine_id} wine_name={self.wine_name}>'


class Cheese(db.Model):
    """A cheese."""

    __tablename__ = "cheeses"

    cheese_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True,)
    cheese_name = db.Column(db.String, nullable=False)
    cheese_img = db.Column(db.String)
    cheese_region = db.Column(db.String, nullable=False)
    cheese_description = db.Column(db.Text, nullable=False)
    cheese_bio = db.Column(db.Text, nullable=False)
    cheese_animal = db.Column(db.String)
    cheese_density = db.Column(db.String, nullable=False)

    userpair_relationship = db.relationship('UserPair')
    communitypair_relationship = db.relationship('CommunityPair')

    def __repr__(self):
        return f'<Cheese Information cheese_id={self.cheese_id} cheese_name={self.cheese_name}>'


class UserPair(db.Model):
    """A user's created paired wine and cheese."""

    __tablename__ = "user_pairs"

    userpair_id = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    wine_id = db.Column(db.Integer, db.ForeignKey('wines.wine_id'))
    cheese_id = db.Column(db.Integer, db.ForeignKey('cheeses.cheese_id'))

    user_relationship = db.relationship('User')
    wine_relationship = db.relationship('Wine')
    cheese_relationship = db.relationship('Cheese')

    def __repr__(self):
        return f'UserPair userpair_id={self.userpair_id} user_id={self.user_id}'


class CommunityPair(db.Model):
    """An already established cheese and wine pairing that can be seen viewed/accessed by users."""

    __tablename__ = "community_pairs"

    communitypair_id = db.Column(db.Integer,
                                 primary_key=True,
                                 autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    wine_id = db.Column(db.Integer, db.ForeignKey(wines.wine_id))
    cheese_id = db.Column(db.Integer, db.ForeignKey(cheeses.cheese_id))

    user_relationship = db.relationship('User')
    wine_relationship = db.relationship('Wine')
    cheese_relationship = db.relationship('Cheese')

    def __repr__(self):
        return f'Community Pair communitypair_id={self.communitypair_id} user_id={self.user_id}'



class Rating(db.Model):
    """A rating that a user can create and publish on their profile"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True)
    pairtype_id = db.Column(db.String, db.ForeignKey(pair_types.pairtype_id))
    user_id = db.Column(db.Integer, db.ForeignKey(users.user_id))
    pair_rating = db.Column(db.Integer)
    user_made_pair = db.Column(db.Boolean, nullable=False)

    user_relationship = db.relationship('User')

    def __repr__(self):
        return f'Rating rating_id={self.rating_id} pair_rating={self.pair_rating}'


def connect_to_db(flask_app, db_uri='postgresql:///gameapp', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    # db.create_all()
