from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, SelectMultipleField, SelectField, TextAreaField, FieldList, FormField, validators
from wtforms.validators import InputRequired, DataRequired

class CourseForm(FlaskForm):
    course = SelectField('your course with professor?', choices=[], validators=[DataRequired()], render_kw={"class": "form-control select2-js", "col": "col-sm-4 col-sm-push-8"})
    year = SelectField('year?', choices=[(year, str(year - 1) + '/' + str(year)) for year in range(2025, 2000, -1)], validators=[DataRequired()], render_kw={"class": "form-control select2-js", "col": "col-sm-2 col-sm-push-2"})
    semester = SelectField('semester?', choices=[(1, '1'), (2, '2')], validators=[DataRequired()], render_kw={"class": "form-control select2-js", "col": "col-sm-2 col-sm-pull-2"})
    grade_choices = [(mark, str(mark)) for mark in range(30, 17, -1)]
    grade_choices.insert(0, (31, '30L'))
    grade_choices.append((17, 'Failed'))
    grade = SelectField('final mark?', choices=grade_choices, validators=[DataRequired()], render_kw={"class": "form-control select2-js", "col": "col-sm-3 col-sm-pull-7"})
    
class RatingForm(FlaskForm):
    rating1 = RadioField('Teaching Quality', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int, validators=[InputRequired()], description={'lowest_label': 'Bad', 'highest_label': 'Good'})
    
    rating2 = RadioField('Grading', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int, validators=[InputRequired()], description={'lowest_label': 'Bad', 'highest_label': 'Good'})
    
    rating3 = RadioField('Ethic', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int, validators=[InputRequired()], description={'lowest_label': 'Bad', 'highest_label': 'Good'})
    
    rating4 = RadioField('Teaching Load', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], coerce=int, validators=[InputRequired()], description={'lowest_label': 'Low', 'highest_label': 'High'})
    
    personality1 = RadioField('How much did you learn from this professor?', choices=[(1, 'not so much'), (2, 'acceptable'), (3, 'a lot')], coerce=int, validators=[InputRequired()], description={'data-page': '1'})
    
    personality2 = RadioField('How is professor grading policy?', choices=[(1, 'unclear'), (2, 'normal'), (3, 'quite clear')], coerce=int, validators=[InputRequired()], description={'data-page': '2'})
    
    personality3 = RadioField("How is professor's teaching exciting?", choices=[(1, 'boring'), (2, 'normal'), (3, 'exciting')], coerce=int, validators=[InputRequired()], description={'data-page': '3'})
    
    personality4 = RadioField('How much professor care about studens?', choices=[(1, "doesn't care"), (2, 'normal'), (3, 'care a lot')], coerce=int, validators=[InputRequired()], description={'data-page': '4'})
    
    personality5 = RadioField('How punctual is professor?', choices=[(1, 'not punctual'), (2, 'normal'), (3, 'punctual')], coerce=int, validators=[InputRequired()], description={'data-page': '5'})
    
    personality6 = RadioField("How is professor's classes order?", choices=[(1, 'disorderly'), (2, 'normal'), (3, 'in good order')], coerce=int, validators=[InputRequired()], description={'data-page': '6'})
    
    personality7 = RadioField("How is professor's power of conveying content?", choices=[(1, 'weak'), (2, 'normal'), (3, 'strong')], coerce=int, validators=[InputRequired()], description={'data-page': '7'})
    
    personality8 = RadioField('How much professor is master at the subject of the lessons?', choices=[(1, 'not at all'), (2, 'acceptable'), (3, 'master')], coerce=int, validators=[InputRequired()], description={'data-page': '8'})
    
    personality9 = RadioField('funny or serious', choices=[(1, 'serious'), (2, 'normal'), (3, 'funny')], coerce=int, validators=[InputRequired()], description={'data-page': '9'})
    
    personality10 = RadioField('how much does professor answer to questions?', choices=[(1, 'not much'), (2, 'normal'), (3, 'very much')], coerce=int, validators=[InputRequired()], description={'data-page': '10'})
    
    personality11 = SelectMultipleField('study materials?', choices=[(1, 'notes'), (2, 'books'), (3, 'slides')], coerce=int, validators=[InputRequired()], description={'data-page': '11'})
    
    personality12 = RadioField('presence and absence', choices=[(1, 'mandatory'), (2, 'optional')], coerce=int, validators=[InputRequired()], description={'data-page': '12'})
    
    personality13 = RadioField('Behavior or grading between different students?', choices=[(1, 'with discrimination'), (2, 'normal'), (3, 'with justice')], coerce=int, validators=[InputRequired()], description={'data-page': '13'})
    
    personality14 = RadioField('accesable out of class?', choices=[(1, 'no'), (2, 'yes')], coerce=int, validators=[InputRequired()], description={'data-page': '14'})
    
    personality15 = RadioField('exams difficaulty', choices=[(1, 'very hard'), (2, 'normal'), (3, 'easy')], coerce=int, validators=[InputRequired()], description={'data-page': '15'})
    
    personality16 = RadioField('teaching methods', choices=[(1, 'old and bad'), (2, 'normal'), (3, 'new and good')], coerce=int, validators=[InputRequired()], description={'data-page': '16'})
    
    personality17 = RadioField('professor is up to date?', choices=[(1, 'no'), (2, 'yes')], coerce=int, validators=[InputRequired()], description={'data-page': '17'})
    
    personality18 = RadioField('possibility to fail the course?', choices=[(1, 'yes'), (2, 'no')], coerce=int, validators=[InputRequired()], description={'data-page': '18'})
    
    Courses = FieldList(FormField(CourseForm), min_entries=1)
    
    review_textarea = TextAreaField('your review', [validators.optional(), validators.length(max=2000)], render_kw={"placeholder": "If you have any good or bad experoence with professor %s please share with others...", "id": "review-textarea"}, name= "review-textarea")


    submit = SubmitField('Submit', render_kw={"id": "send-review"})


