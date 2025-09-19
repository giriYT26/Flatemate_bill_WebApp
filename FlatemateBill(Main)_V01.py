from flask import Flask,render_template,request
from flask.views import MethodView
from wtforms import Form,StringField,SubmitField
from Bill_V01 import Bill,Flatemate

app = Flask(__name__)

class Homepage(MethodView):
    def get(self):
        return render_template("index.html")
    
class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template("bill_form_page.html",billform = bill_form)
    
class ResultPage(MethodView):
    def post(self):
        billform = BillForm(request.form)

        bill_amount = billform.bill_amt.data
        bill_period = billform.bill_period
        the_bill = Bill(bill_amount,bill_period)
        flatemate1 = Flatemate(billform.name1.data,billform.days_in_house1.data)
        flatemate2 = Flatemate(billform.name2.data,billform.days_in_house2.data)

        return f"{flatemate1.name} {flatemate1.pays}"
    
class BillForm(Form):
    bill_amt = StringField(label="Bill Amount:")
    bill_period = StringField(label="Bill Period:")
    #First FlateMate
    name1 = StringField(label="Name:")
    days_in_house1 = StringField(label="Days in house:")
    #Second FlateMate
    name2 = StringField(label="Name:")
    days_in_house2 = StringField(label="Days in house:")

    button = SubmitField("Calculate")


# Adding the url 
"""
This registers the / route to the "your respected class" as class-based view. 
The as_view("func_name_you_want") converts the class into a view function, and "func_name_you_want" is the endpoint name
"""

app.add_url_rule("/",view_func=Homepage.as_view("Home_page")) 
app.add_url_rule("/bill",view_func=BillFormPage.as_view("Bill_Form_Page"))
app.add_url_rule("/results",view_func=ResultPage.as_view("Results_page"))

app.run(debug=True)

