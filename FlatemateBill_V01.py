from flask import Flask,render_template
from flask.views import MethodView
from wtforms import Form,StringField

app = Flask(__name__)

class Homepage(MethodView):
    def get(self):
        return render_template("index.html")
class BillFormPage(MethodView):
    def get(self):
        return render_template("bill_form_page.html")
class ResultPage(MethodView):
    pass    
class BillForm(Form):
    pass

# Adding the url 
"""
This registers the / route to the "your respected class" as class-based view. 
The as_view("func_name_you_want") converts the class into a view function, and "func_name_you_want" is the endpoint name
"""

app.add_url_rule("/",view_func=Homepage.as_view("Home_page")) 
app.add_url_rule("/bill",view_func=BillFormPage.as_view("Bill_Form_Page"))

app.run(debug=True)

