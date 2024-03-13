import os
import random
from flask import Flask, send_from_directory, jsonify, make_response
import json

app = Flask(__name__, static_folder='./build/static')


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

@app.route('/test', methods=['GET'])
def test():
    response = make_response('test response')
    return response

@app.route('/api/tarot-reading', methods=['GET'])
def generate_tarot_reading():

    

    """tarots = open(os.path.join('src',"Tarot.json"),"r")
    json.loads(str(tarots))
    print(str(tarots))"""

    with open('src/Tarot.json') as f:
        deck = json.load(f)
        #print(deck)
        #print(type(deck))

    # Number of cards to include in the reading (you can adjust this)
    num_cards = 3
    
    tarot_deck = {
        "Card1": "Interpretation 1 for Card 1",
        "Card2": "Interpretation 2 for Card 2",
        "Card3": "Interpretation 3 for Card 3",
        # Add more cards and interpretations as needed
    }
    print(type(deck[0])) #deck is a list of dictionaries
    #tarot_deck = random.sample(set(deck.keys()), num_cards)
    tarot_deck = deck
    """# Shuffle the Tarot deck
    shuffled_deck = list(tarot_deck)
    random.shuffle(shuffled_deck)
    
    # Select a random set of cards for the reading
    selected_cards = shuffled_deck[:num_cards]"""
    print(deck[0]['name'])
    print(deck[0]['interpretation'])
    selected_cards = []
    interpretations = []
    descriptions = []
    for i in range(num_cards):
        selected_cards.insert(i,deck[i]['name'])
        interpretations.insert(i,deck[i]['interpretation'])
        descriptions.insert(i,deck[i]['description'])
    # Retrieve interpretations for the selected cards
    #interpretations = [tarot_deck[card] for card in selected_cards]
    # Return the Tarot reading as JSON data
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
