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

def insert_review(review_text, pokemon_name, ip_address, user_agent):
    host = 'localhost'
    user = 'root'
    password = 'C8a86wzJ3zsXtTHRGcvFJwT7h'
    database = 'pokemon'

    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()

        # Assuming id is auto-incremented
        update_query = "UPDATE pokemon_data SET review = %s, ip_address = %s, user_agent = %s WHERE name = %s"
        cursor.execute(update_query, (review_text, ip_address, user_agent, pokemon_name))

        
        connection.commit()
        cursor.close()
        connection.close()
        print("Review inserted successfully.")
    except pymysql.Error as e:
        print(f"Error inserting review: {e}")

# Call this function when submitting the review
# insert_review("This is a sample review.")

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

# Handler action if /review is triggered
@app.route('/review', methods=['POST'])
def pokemonReview():
    review_text = request.form['review']
    pokemon_name = request.form['pokemon_name']
    ip_address = request.remote_addr
    user_agent = request.user_agent.string
    insert_review(review_text, pokemon_name, ip_address, user_agent)
    return render_template("review.html")


# Run the Flask
if __name__ == '__main__':
    app.run(debug=True)