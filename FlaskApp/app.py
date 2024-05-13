from flask import Flask, render_template, flash,request

# Create a Flask application instance
app = Flask(__name__)
app.secret_key = "nourpristinibachelor"

# Define a route for the root URL
@app.route('/')
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/welcome", methods=['POST', 'GET'])
def greet():
	flash(f"Hello {request.form['name']}, great to see you!")
	return render_template("index.html")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
