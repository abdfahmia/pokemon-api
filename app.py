from flask import Flask, render_template, request
import requests, pymysql

# Initialization
app = Flask(__name__)

# Function to establish connection and fetch data
def fetch_data():
    host = 'localhost'
    user = 'root'
    password = 'C8a86wzJ3zsXtTHRGcvFJwT7h'
    database = 'pokemon'
    
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon_data")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return results

# Handler in main controller
@app.route('/', methods=['GET'])
def main():
    data = fetch_data()
    pokemons = [{'id': row[0], 'name': row[1], 'img_url': row[2], 'type': row[3], 'review': row[4]} for row in data]
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