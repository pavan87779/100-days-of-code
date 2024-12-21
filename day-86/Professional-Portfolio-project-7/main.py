import flask
from flask import render_template, app
import requests
@app.route('/café')
def cafe():
    cafe_response = requests.get("https://mirko867.pythonanywhere.com/random")
    if cafe_response.status_code == 200:
        cafe_data = cafe_response.json()[ 'cafe' ]
    else:
        cafe_data = {}

    all_cafe_response = requests.get("https://mirko867.pythonanywhere.com/all")
    if all_cafe_response.status_code == 200:
        all_cafe_data = all_cafe_response.json()['cafes']
    else:
        all_cafe_data = {}

    return render_template("cafe_index.html", cafe=cafe_data, all_cafe=all_cafe_data)

@app.route('/search')
def search_cafe():
    search_query = request.args.get('loc')  # Get 'loc' parameter from the search form
    api_url = f"https://mirko867.pythonanywhere.com/search?loc={search_query}"
    cafe_response = requests.get(api_url)
    print(cafe_response)
    if cafe_response.status_code == 200:
        cafes_data = cafe_response.json().get('cafes' , [ ])
    else:
        cafes_data = [ ]

    return render_template("Search.html" , cafes=cafes_data , query=search_query)

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    url = "https://mirko867.pythonanywhere.com/add"
    add_form = AddForm()
    if request.method == "POST":
        if add_form.validate_on_submit():
            print("Form is valid, proceeding to send data.")
            form_data = {
                "name": add_form.name.data ,
                "loc": add_form.location.data ,
                "has_sockets": add_form.has_sockets.data ,
                "has_toilet": add_form.has_toilet.data ,
                "has_wifi": add_form.has_wifi.data ,
                "can_take_calls": add_form.can_take_calls.data ,
                "coffee_price": add_form.coffee_price.data,
                "review": add_form.review.data or "No review provided" ,
                "user": add_form.user.data or "Anonymous" ,
                "ig": add_form.ig.data or "Not provided"
            }

            # Send the data to the API
            response = requests.post(url, data=form_data)
            print(response)
            return render_template("thanks.html")

    return render_template("add_cafes.html", form=add_form)