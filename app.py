import os
import random
from flask import Flask, send_from_directory, jsonify, make_response
import json

app = Flask(__name__, static_folder='./build/static')


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

@app.route('/api/tarot-reading', methods=['GET'])
def generate_tarot_reading():

    

    with open('src/Tarot.json') as f:
        deck = json.load(f)

    # Number of cards to include in the reading (you can adjust this)
    num_cards = 3
    
    tarot_deck = deck
    
    chosen_deck = []
    for i in range(num_cards):
        chosen_deck.insert(i,deck[random.randrange(78)])
    print(chosen_deck)
    selected_cards = []
    interpretations = []
    descriptions = []
    for i in range(num_cards):
        selected_cards.insert(i,chosen_deck[i]['name'])
        interpretations.insert(i,chosen_deck[i]['interpretation'])
        descriptions.insert(i,chosen_deck[i]['description'])
    
    response = {
        "cards": selected_cards,
        "descriptions": descriptions,
        "interpretations": interpretations,
    }
    return jsonify(response)

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    debug=True
)
