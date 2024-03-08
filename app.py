from flask import Flask, render_template,jsonify,request
import requests

# Initialization
app = Flask(__name__)

# Define Model
class Pokemon:
    def __init__(self, img_url, name, number):
        self.img_url = img_url
        self.name = name
        self.number = number

# Handler in main controller
@app.route('/')
def main():
    pokemons = [
        Pokemon(number=1, name="hariyama", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/297.png" ),
        Pokemon(number=2, name="porygon", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png" ),
        Pokemon(number=3, name="golduck", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/55.png" ),
        Pokemon(number=4, name="magby", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/240.png" ),
        Pokemon(number=5, name="pinsir", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/127.png" ),
        Pokemon(number=6, name="ledian", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/166.png" ),
        Pokemon(number=7, name="sceptile", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/254.png" ),
        Pokemon(number=8, name="porygon", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/137.png" ),
        Pokemon(number=9, name="pineco", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/204.png" ),
        Pokemon(number=10, name="lickitung", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/108.png" ),
        Pokemon(number=11, name="jynx", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png" ),
        Pokemon(number=12, name="hitmontop", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/237.png" ),
        Pokemon(number=13, name="raichu", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/26.png" ),
        Pokemon(number=14, name="houndour", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/228.png" ),
        Pokemon(number=15, name="unown", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/201.png" ),
        Pokemon(number=16, name="houndoom", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/229.png" ),
        Pokemon(number=17, name="azurill", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/298.png" ),
        Pokemon(number=18, name="sentret", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/161.png" ),
        Pokemon(number=19, name="jynx", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png" ),
        Pokemon(number=20, name="loudred", img_url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/294.png" ),
    ] 
    return render_template("main.html", pokemons=pokemons, number=len(pokemons))


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