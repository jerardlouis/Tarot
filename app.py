import os
import random
from flask import Flask, send_from_directory, jsonify, make_response
import json
import AI

app = Flask(__name__, static_folder='./build/static')


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

@app.route('/api/tarot-reading', methods=['GET'])
def get_cards():

    

    with open('src/Tarot.json') as f:
        deck = json.load(f)

    # Number of cards to include in the reading (you can adjust this)
    num_cards = 3
    
    tarot_deck = deck
    
    chosen_deck = []
    for i in range(num_cards):
        chosen_deck.insert(i,deck[random.randrange(78)])
    #print(chosen_deck)
    selected_cards = []
    interpretations = []
    descriptions = []
    reversed = []
    for i in range(num_cards):
        likelihood_of_flip = random.randint(0,10)
        if likelihood_of_flip <= 2:
            is_flipped = 1
        else:
            is_flipped = 0
        selected_cards.insert(i,chosen_deck[i]['name'])
        interpretations.insert(i,chosen_deck[i]['interpretation'].split('Reversed:')[is_flipped])
        descriptions.insert(i,chosen_deck[i]['description'])
        if(is_flipped):
            card_status = 'Reversed'
        else:
            card_status = 'Not Reversed'
        reversed.insert(i,card_status)

    reading = AI.reading(chosen_deck)

    response = {
        "cards": selected_cards,
        "descriptions": descriptions,
        "interpretations": interpretations,
        "reversed": reversed,
        "reading": reading,
    }
    #print(response)
    #print(AI.test()) #Send the response here
    #print(AI.reading(chosen_deck))
    print(response)
    return jsonify(response)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    debug=True
)
