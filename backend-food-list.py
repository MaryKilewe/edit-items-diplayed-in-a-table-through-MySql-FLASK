
from flask import Flask, render_template, request, session, redirect, url_for, flash
import pymysql
import pandas
import matplotlib.pyplot as plt
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/>?@$'

# create the popup form with some adjustments to the code - https://www.formget.com/how-to-create-pop-up-contact-form-using-javascript/
@app.route('/food-list', methods=['POST', 'GET'])
def food_list():
    con = pymysql.connect("localhost", "root", "", "sampledb")

    cursor = con.cursor()
    sql_allfood = "SELECT * FROM `allfood_tbl` ORDER BY `id`"
    cursor.execute(sql_allfood)
    rows_allfood = cursor.fetchall()

    # this will join the data from all three tables in a variable named foodata.
    # This is abetter way to display all food items in the database.
    # Sql Full joins won't work here because there is no common column among the table
    return render_template('food-list.html', fooddata=rows_allfood)


@app.route('/edit-food/<item_id>', methods=['POST', 'GET'])
def edit_food(item_id):
    if request.method == 'POST':  # check if user posted something
        item = request.form['item']
        # notice the difference in brackets used on description line. () is used instead of []
        description = request.form['description']
        cost = request.form['cost']
        image = request.form['image']

        # update the row with the specific id passed in the url above
        # --------------------------------------------------------------
        con = pymysql.connect("localhost", "root", "", "sampledb")
        # update main database
        cursor = con.cursor()
        sql = "UPDATE `allfood_tbl` " \
              "SET `item`=%s, `description`=%s, `cost`=%s, `image`=%s " \
              "WHERE `id`=%s"

        cursor.execute(sql, (item, description, cost, image, item_id))
        con.commit()

        # redirect to food list url
        return redirect(url_for('food_list'))

    else:
        con = pymysql.connect("localhost", "root", "", "sampledb")
        cursor_1 = con.cursor()
        sql_allfood = "SELECT * FROM `allfood_tbl` ORDER BY `id`"
        cursor_1.execute(sql_allfood)
        rows_allfood = cursor_1.fetchall()

        # pass the item's name, description, cost and image to the input field of the html form
        cursor_item_name = con.cursor()
        sql_item_name = "SELECT * FROM `allfood_tbl` WHERE `id`=%s"
        cursor_item_name.execute(sql_item_name, item_id)
        item_name = cursor_item_name.fetchall()

        #name_of_item = con.cursor().execute("SELECT `item` FROM `meals_tbl` WHERE `id`=%s", item_id)
        return render_template('edit-food-list.html',
                               fooddata=rows_allfood,
                               item_edited=item_id,
                               description_data=[{'description':'meal'}, {'description':'drink'}, {'description':'dessert'}],
                               selected_item=item_name
                               )


if __name__ == "__main__":
    app.run(debug=True)
