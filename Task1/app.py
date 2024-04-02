from __future__ import annotations

from flask import Flask
from flask import render_template
from flask import request

from .data_referall import get_referrals
from .data_referall import load_referral_tree

app = Flask(__name__)
csv_path = "client.csv"

# Loading the referral tree
referral_tree = load_referral_tree(csv_path)


@app.route("/", methods=["GET", "POST"])
def home():
    client_email = ""
    referrals_list = []
    if request.method == "POST":
        client_email = request.form["client_email"]
        referrals_list = get_referrals(client_email, referral_tree)
    return render_template(
        "index.html",
        referrals=referrals_list,
        client_email=client_email,
    )


if __name__ == "__main__":
    app.run(debug=True)
