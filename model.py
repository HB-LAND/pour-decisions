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


class Pair(db.Model):
    """A user's created paired wine and cheese."""

    __tablename__ = "pairs"

    pair_id = db.Column(db.Integer,
                            primary_key=True,
                            autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    wine_id = db.Column(db.Integer, db.ForeignKey('wines.wine_id'))
    cheese_id = db.Column(db.Integer, db.ForeignKey('cheeses.cheese_id'))
    user_made = db.Column(db.Boolean, nullable=False)

    user_relationship = db.relationship('User')
    wine_relationship = db.relationship('Wine')
    cheese_relationship = db.relationship('Cheese')

    def __repr__(self):
        return f'Pair userpair_id={self.pair_id} user_id={self.user_id}'


class Rating(db.Model):
    """A rating that a user can create and publish on their profile"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True)
    pair_id = db.Column(db.String, db.ForeignKey('pairs.pair_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    pair_rating = db.Column(db.Integer)

    user_relationship = db.relationship('User')

    def __repr__(self):
        return f'Rating rating_id={self.rating_id} pair_rating={self.pair_rating}'


def connect_to_db(app):
    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pour-decisions'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
