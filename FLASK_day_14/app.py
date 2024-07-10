from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# list of wild conservation species
species_list = [
    {
        'name': 'Brown Bear',
        'habitat': 'Mountainous regions'
    },
    {
        'name': 'Giraffe',
        'habitat': 'Savannahs and deserts'
    },
    {
        'name': 'Lion',
        'habitat': 'Grasslands and savannahs'
    },
]

# create the route
@app.route('/')
def index():
    return render_template("index.html", species=species_list)

@app.route('/add_species', methods=['GET', 'POST'])
def add_species():
    if request.method == 'POST':
        species_name = request.form['species_name']
        habitat = request.form['habitat']
        species_list.append({
            'name': species_name,
            'habitat': habitat
        })
        return redirect(url_for('index'))
    return render_template('add_species.html')

@app.route('/species_list')
def species_list_page():
    return render_template("species_list.html", species=species_list)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/donate')
def donate():
    return render_template("donate.html")

if __name__ == "__main__":
    app.run(debug=True)
