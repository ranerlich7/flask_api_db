from flask import Flask, jsonify
from data import cars, users
# Create a Flask web server
app = Flask(__name__)

# Define a route for the root URL of the web server


@app.route('/cars')
def cars_list():
    return cars


@ app.route('/users')
def users_list():
    return jsonify(users)


# Run the web server on localhost at port 5000
if __name__ == '__main__':
    app.run(debug=True)
