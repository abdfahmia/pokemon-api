from flask import Flask, render_template,jsonify,request
import requests

# Initialization
app = Flask(__name__)

# Handler in main controller
@app.route('/')
def main():
    return render_template('main.html')

# Handler action if /result is triggered
@app.route('/result', methods=['GET', 'POST'])
def pokemonData():
    if request.method == 'POST':
        pokemonName = request.form['poke']
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemonName}'
        data = requests.get(url)
        if data.status_code == 200:
            pokemon = data.json()
            id = pokemon['id']
            height = pokemon['height']
            weight = pokemon['weight']
            name = pokemon['name']
            image = pokemon['sprites']['front_default']
            poke = ({
                'id':id,'height':height,'weight':weight,
                'name':name,'image':image
            })
            return render_template('result.html', poke=poke)
        else:
            return render_template('errorPage.html')



# Run the Flask
if __name__ == '__main__':
    app.run(debug=True)