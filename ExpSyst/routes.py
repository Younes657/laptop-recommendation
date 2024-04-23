from flask import Flask, flash, redirect,render_template, session, url_for

from ExpSyst import app
from ExpSyst.form import SlectForm
from ExpSyst.models import Cart, laptop

from ExpSyst.aima_logic import get_sysExpert_result

@app.route("/",  methods=['GET' , 'POST'])
@app.route("/home" , methods=['GET', 'POST'])
def home_page():
    form = SlectForm()
    if form.validate_on_submit():
        cart = Cart(form.selectProcessor.data, form.selectRam.data, form.selectStorage.data , form.selectBattryLife.data, form.selectBudget.data)
        print(f"{cart.Processor , cart.Ram , cart.Storage , cart.BattryLife, cart.Budget}")
        #get_sysExpert_result(cart)

        with app.app_context():
            laptopsDb = laptop.query.limit(10).all()
        laptops = []
        for laptopdb in laptopsDb:
            laptops.append(laptopdb.to_dict())

        session["laptops"] = laptops
        return redirect(url_for('Laptops_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f' {err_msg}', category='danger')

    return render_template('home.html', form=form)

@app.route("/laptops")
def Laptops_page():
    
    laptops = session.get('laptops', []) # Retrieve laptops from session, default to empty list if not found
    # Now you can use laptops in your template or further processing

    return render_template('laptops.html', laptops=laptops)

@app.route('/laptop/<int:lap_id>')
def Laptop_details_page(lap_id):
    laptopdb = laptop.query.get_or_404(lap_id)
    return render_template('laptop_details.html' , laptop = laptopdb)