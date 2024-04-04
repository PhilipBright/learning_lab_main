from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure the MongoDB URI
# For a local MongoDB instance
app.config["MONGO_URI"] = "mongodb+srv://Philip:Myanmar2023@cluster0.cze7alr.mongodb.net/learningLab?retryWrites=true&w=majority"

# If using MongoDB Atlas, replace the line above with your connection string
# app.config["MONGO_URI"] = "<Your Atlas Connection String>"

mongo = PyMongo(app)

@app.route('/insert')
def insert_data():
    a = "some_value"  # Define the variable "a"
    mongo.db.user.insert_one({a: 1})  # 'test_collection' is created if it doesn't exist
    return jsonify({"message": "Data inserted successfully."})


@app.route('/data')
def get_data():
    # Retrieving the first document from the 'test_data' collection
    data = mongo.db.test_data.find_one({}, {'_id': 0})  # Exclude the '_id' field
    return jsonify(data if data else {"message": "No data found."})

@app.route('/test_db')
def test_db():
    try:
        mongo.db.list_collection_names()  # This should not raise if the connection is successful
        return jsonify({"message": "Database connection is successful."})
    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/check_connection')
def check_connection():
    try:
        # This line should work if mongo has been properly initialized
        mongo.db.list_collection_names()  # Forces a connection and fetches collection names
        return jsonify({"message": "Successfully connected to MongoDB."})
    except Exception as e:
        # General exception catch for troubleshooting; refine as needed
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True, port=5001)
