import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Competition Dashboard</h1><iframe width="600" height="450" src="https://datastudio.google.com/embed/reporting/1dAOi-wtry-sZE2dWeKAj4RIvIeBxWKhj/page/KYKv" frameborder="0" style="border:0" allowfullscreen></iframe>"

app.run()