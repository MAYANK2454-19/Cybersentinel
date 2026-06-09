from flask import Flask, render_template, request
from scanner.scanner import run_scan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        hostname = request.form["hostname"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])

        report = run_scan(hostname,start_port,end_port )

        return render_template(
            "results.html",
            report=report
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )