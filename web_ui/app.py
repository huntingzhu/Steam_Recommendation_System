from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
DB_URI = 'mysql://huntingzhu:ad2137096068ad@steam-recommendation.chcqngehr8cs.us-west-2.rds.amazonaws.com/steam_recommendation'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class recommendation_global(db.Model):
    __tablename__ = 'global_recommend'
    rank = db.Column('rank', db.Integer, primary_key = True)
    name = db.Column('name', db.Text)
    header_image = db.Column('header_image', db.Text)
    steam_appid = db.Column('steam_appid', db.Integer)

    def __init__(self, rank, name, header_image, steam_appid):
        self.rank = rank
        self.name = name
        self.header_image = header_image
        self.steam_appid = steam_appid

class recommendation(db.Model):
    __tablename__ = 'final_recommend'
    user_id = db.Column('user_id', db.Text, primary_key = True)
    rank = db.Column('rank', db.Integer, primary_key = True)
    name = db.Column('name', db.Text)
    header_image = db.Column('header_image', db.Text)
    steam_appid = db.Column('steam_appid', db.Integer)

    def __init__(self, user_id, rank, name, header_image, steam_appid):
        self.user_id = user_id
        self.rank = rank
        self.name = name
        self.header_image = header_image
        self.steam_appid = steam_appid

@app.route('/')
def global_recommendation():
    global_recom = recommendation_global.query.order_by(recommendation_global.rank).all()
    return render_template("index.html", global_recom=global_recom)

@app.route('/<user_id>')
def user_recommendation(user_id):
    user_recom = recommendation.query.filter_by(user_id=user_id).order_by(recommendation.rank).all()
    return render_template("user.html", user_recom = user_recom)

if __name__ == '__main__':
    app.run()
