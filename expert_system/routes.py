from flask import Flask, flash, redirect,render_template, session, url_for

from expert_system import app
from expert_system.form import SlectForm

from expert_system.functions import laptops_filtration
from expert_system.models import Cart, laptop

from expert_system.aima_logic import get_sysExpert_result

@app.route("/",  methods=['GET' , 'POST'])
@app.route("/home" , methods=['GET', 'POST'])
def home_page():
    form = SlectForm()
    if form.validate_on_submit():
        cart = Cart(form.selectProcessor.data, form.selectRam.data, form.selectStorage.data , form.selectBattryLife.data, form.selectBudget.data)
        # print(f"{cart.Processor , cart.Ram , cart.Storage , cart.BattryLife, cart.Budget}")
        result = get_sysExpert_result(cart)
        if result == "" :
            flash("Your inputs are not compatible with each other. Please check your inputs and try again !!!!", category='danger')
        else:
            session["result"] = str(result)
            return redirect(url_for('Laptops_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f' {err_msg}', category='danger')

    return render_template('home.html', form=form)

@app.route("/laptops")
def Laptops_page():
    result = session.get("result" , "") # Retrieve laptops from session, default to empty list if not found
    # Now you can use laptops in your template or further processing
    if result != "":
        laptopsDb = laptops_filtration(result)
        return render_template('laptops.html' , laptops = laptopsDb , result = result)
    else:
        with app.app_context():
            laptops = laptop.query.all()
        return render_template('laptops.html' , laptops = list(laptops) , result = "")
@app.route('/laptop/<int:lap_id>')
def Laptop_details_page(lap_id):
    laptopdb = laptop.query.get_or_404(lap_id)
    return render_template('laptop_details.html' , laptop = laptopdb )