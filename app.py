from flask import Flask, render_template, jsonify, request
from database import load_professors_from_db

app = Flask(__name__)

@app.route('/')
def HomePage():
    return render_template('home.html', title="RateYourProfessor")

# Search endpoint that returns dynamic search suggestions
@app.route('/search')
def search():
    professors = load_professors_from_db()  # Load the list of professors from the database
    query = request.args.get('q', '').lower()  # Get search query
    if query:
        # Filter professors based on the query (searching by Name)
        results = [
            {
                'name': item['Name'], 
                'url': f"/professor/{item['PID']}"  # Using PID for unique URL
            }
            for item in professors if query in item['Name'].lower()
        ]
    else:
        results = []  # Ensure that an empty list is returned for empty queries
    return jsonify(results)


# Results page route (when user presses Enter)
@app.route('/results')
def results():
    query = request.args.get('q', '')
    return f"Results for {query}"

# Direct page route for selected professor using the PID
@app.route('/professor/<pid>')
def professor_page(pid):
    professors = load_professors_from_db()
    # Find the professor by PID
    professor = next((prof for prof in professors if prof['PID'] == pid), None)
    
    if professor:
        return f"Welcome to {professor['Name']}'s page!"
    else:
        return "Professor not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
