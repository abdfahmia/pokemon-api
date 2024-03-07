from flask import Flask, jsonify, render_template, request

# Initialization
app = Flask(__name__)

# Handler in main controller
@app.route('/')
def main():
    return render_template('main.html')


# Run the Flask
if __name__ == '__main__':
    app.run(debug=True)