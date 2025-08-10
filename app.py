from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

FINE_RATE = 2  # ₹2 per day late

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        book_title = request.form["book_title"]
        borrow_date = request.form["borrow_date"]
        due_date = request.form["due_date"]
        return_date = request.form["return_date"]

        # Convert string dates to datetime objects
        due = datetime.strptime(due_date, "%Y-%m-%d")
        returned = datetime.strptime(return_date, "%Y-%m-%d")

        # Fine Calculation
        if returned <= due:
            fine = 0
            days_late = 0
        else:
            days_late = (returned - due).days
            fine = days_late * FINE_RATE

        return render_template("result.html",
                               book_title=book_title,
                               days_late=days_late,
                               fine=fine)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
