from flask import *
from hms import Customer
from database import DataBaseHelper

app = Flask("HotelManagementApp")
db_helper = DataBaseHelper()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

@app.route("/single")
def single():
    return render_template("single.html")


@app.route("/add-customer")
def add_customer():
    return render_template("add-customer.html")


@app.route("/view-customers")
def view_customers():
    cref = Customer()
    sql = cref.select_sql()
    rows = db_helper.read(sql)

    return render_template("view-customers.html", result=rows)


@app.route("/save-customers", methods=["POST"])
def save_customers():
    cref = Customer(name=request.form["name"], phone=request.form["phone"], email=request.form["email"],
                    room=request.form["room"],amount=request.form["amount"])
    print(vars(cref))
    sql = cref.insert_sql()
    db_helper.write(sql)
    # return cref.name + " Inserted Successfully"
    return render_template("success.html", message=cref.name + "Inserted successfully")


@app.route("/delete/<id>")
def delete_customer_from_db(id):
    cref = Customer(id=id)
    sql = cref.delete_sql()
    db_helper.write(sql)
    return render_template("success.html", message="Customer with ID "+id+" Deleted Successfully..")



def main():
    app.run()


if __name__ == "__main__":
    main()
