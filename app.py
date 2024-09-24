from flask import Flask, render_template, jsonify, request
from database import load_professors_from_db, store_rating_into_db, load_professor_course_from_db, load_all_course_from_db
from flask_breadcrumbs import Breadcrumbs, register_breadcrumb
from form import RatingForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234'

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
@app.route('/professor/<pid>', methods = ['GET', 'POST'])
def professor_page(pid):
    form = RatingForm()
    if request.method == 'POST':
        teaching_quality = request.form.get('rating1')
        grading = request.form.get('rating2')
        ethic = request.form.get('rating3')
        teaching_load = request.form.get('rating4')

        # Process or store the ratings
        if teaching_quality and grading and ethic and teaching_load:
            # Example: Storing the ratings in a dictionary or sending it to a database
            ratings = {
                'teaching_quality': int(teaching_quality),
                'grading': int(grading),
                'ethic': int(ethic),
                'teaching_load': int(teaching_load)
            }
            
            store_rating_into_db(pid, ratings)
            return "thanks for submitting"
    professors = load_professors_from_db()
    course_names = load_professor_course_from_db(pid)
    course_choices = [(index + 1, course) for index, course in enumerate(course_names)]
    course_choices.append((0, 'Other'))  # Add the "Other" option

    for subform in form.Courses:
        subform.course.choices = course_choices
    # Find the professor by PID
    professor = next((prof for prof in professors if prof['PID'] == pid), None)
    if professor:
        return render_template("profile.html", professor = professor, form = form)
    else:
        return "Professor not found", 404
    
# @app.route('/department')
# def 

# survay = dict()
# @app.route('/survey')
# def survey():
#     labels = [row[0] for row in professor_rate]
#     values = [row[1] for row in professor_rate]
    
#     return render_template('survey.html', labels = labels, values = values)


@app.route("/form", methods = ['GET', 'POST'])
def test_form():
    form = RatingForm()
    course_names = load_professor_course_from_db('003584')
    course_choices = [(index + 1, course) for index, course in enumerate(course_names)]
    course_choices.append((0, 'Other'))  # Add the "Other" option

    for subform in form.Courses:
        subform.course.choices = course_choices

    return render_template("wtform.html", form = form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
