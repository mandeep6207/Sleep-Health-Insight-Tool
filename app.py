from flask import Flask, render_template, request

from utils.analyzer import analyze_sleep

app = Flask(__name__)

DEFAULT_FORM = {
    "sleep_duration": 7.5,
    "screen_time": 2.0,
    "caffeine_intake": 1.0,
    "stress_level": 4.0,
}


@app.route("/", methods=["GET", "POST"])
def index():
    form_values = DEFAULT_FORM.copy()
    analysis = None

    if request.method == "POST":
        form_values = {
            "sleep_duration": float(request.form.get("sleep_duration", DEFAULT_FORM["sleep_duration"])),
            "screen_time": float(request.form.get("screen_time", DEFAULT_FORM["screen_time"])),
            "caffeine_intake": float(request.form.get("caffeine_intake", DEFAULT_FORM["caffeine_intake"])),
            "stress_level": float(request.form.get("stress_level", DEFAULT_FORM["stress_level"])),
        }
        analysis = analyze_sleep(form_values)

    if analysis is None:
        analysis = analyze_sleep(DEFAULT_FORM)

    return render_template("index.html", form_values=form_values, analysis=analysis)


if __name__ == "__main__":
    app.run(debug=True)
