from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests, pymysql
import os

# Initialization
app = Flask(__name__)

# Function to establish connection and fetch data, insert_review, get_review
def fetch_data():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pokemon_data")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return results

def insert_review(review_text, pokemon_name, ip_address, user_agent):
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

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

def get_reviews():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pokemon_data")
        reviews = cursor.fetchall()
        cursor.close()
        connection.close()
        return reviews
    except pymysql.Error as e:
        print(f"Error inserting review: {e}")

def insert_pokemon_data(id, name, image, poke_type):
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    
    # Insert Pokémon data into the database
    insert_query = "INSERT INTO pokemon_data (id, name, img_url, type) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (id, name, image, poke_type))
    
    # Commit changes and close connection
    connection.commit()
    cursor.close()
    connection.close()



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
            types = [poke_type['type']['name'] for poke_type in pokemon['types']]

            if len(types) == 1:
                poke_type = types[0]
            else:
                poke_type = "flying"  # Handle case when there are multiple types
            
            poke = {
                'id': id, 'height': height, 'weight': weight,
                'name': name, 'image': image, 'type': poke_type
            }

            existing_reviews = get_reviews()

            # Check if the Pokémon name is already available in the database
            if name not in [review[1] for review in existing_reviews]:
                # If not available, insert the Pokémon data into the database
                insert_pokemon_data(id, name, image, poke_type) 
                print("successfully added new pokemon info")

            return render_template('result.html', poke=poke, review=existing_reviews)
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