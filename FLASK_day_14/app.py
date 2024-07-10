from flask import Flask, render_template, request, redirect, url_for

# create an instance of the flask class
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
@app.route('/')  # the symbol / takes you to index
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

if __name__ == "__main__":
    app.run(debug=True)
