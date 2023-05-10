# Import necessary modules
from flask import Flask, request, jsonify
from mashine_learning import get_recommendations, get_customer_segments

# Create a Flask web server from the Flask module
app = Flask(__name__)

# Define the recommendation endpoint
@app.route('/recommendations', methods=['GET'])
def recommendations():
    """
    Endpoint to provide product recommendations.
    It expects 'user_id' as a query parameter in the request and returns a list of recommended product ids.
    """
    user_id = request.args.get('user_id') # get user_id from the request
    recommendations = get_recommendations(user_id) # get recommendations for this user
    return jsonify(recommendations) # return recommendations as JSON

# Define the customer segments endpoint
@app.route('/customer_segments', methods=['GET'])
def customer_segments():
    """
    Endpoint to provide customer segments.
    It returns a mapping of user_ids to segments.
    """
    segments = get_customer_segments() # get customer segments
    return jsonify(segments) # return segments as JSON

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
