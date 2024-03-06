from flask import Flask, jsonify

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Handler untuk route /hello
@app.route('/hello')
def hello():
    # Membuat pesan JSON
    message = {"message": "Hello, World!"}
    # Mengembalikan pesan JSON
    return jsonify(message)

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run(debug=True)