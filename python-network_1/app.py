from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for root (Index) page
@app.route('/')
def index():
    return "Index"  # Display "Index" when the root URL is accessed

# Route for POST email
@app.route('/post_email', methods=['POST'])
def post_email():
    email = request.form.get('email')  # Get the email from the POST request
    return jsonify({"message": f"Your email is: {email}"})

# Route for 401 Unauthorized
@app.route('/status_401', methods=['GET'])
def status_401():
    return jsonify({"error": "Unauthorized"}), 401  # Explicitly returning 401 status code

# Route for 500 Internal Server Error
@app.route('/status_500', methods=['GET'])
def status_500():
    # Simulating an internal server error by raising an exception
    raise Exception("Internal Server Error")

# Handle 500 errors globally
@app.errorhandler(500)
def handle_500_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# Handle 401 errors globally
@app.errorhandler(401)
def handle_401_error(error):
    return jsonify({"error": "Unauthorized"}), 401

# Run the Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensure it's running on the correct address and port
