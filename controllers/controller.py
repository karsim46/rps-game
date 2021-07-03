from app import app
from flask import Flask, render_template, request
from models.game import *
from models.player import *
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/<player_1_choice>/<player_2_choice>")
def result(player_1_choice, player_2_choice):
    player_1 = Player("Player 1", player_1_choice)
    player_2 = Player("Player 2", player_2_choice)
    result = decision(player_1, player_2)
    return render_template("scissors.html", result=result)