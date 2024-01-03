import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from whitenoise import WhiteNoise

from forms import MunicipalitySelectForm

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


def get_plots(municipality):
    if municipality:
        return [
            f"{municipality}-countplot-rating-per-year.png",
            f"{municipality}-countplot-year-per-rating.png",
            f"{municipality}-wordcloud.png",
        ]
    return []


@app.route("/", methods=["get", "post"])
def index():
    form = MunicipalitySelectForm(request.form)
    plots = get_plots(form.municipality.data)

    return render_template("index.html", form=form, plots=plots)


if __name__ == "__main__":
    app.run(debug=True)
