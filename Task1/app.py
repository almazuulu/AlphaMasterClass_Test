from flask import Flask, request, render_template
from .data_referall import load_referral_tree, get_referrals

app = Flask(__name__)
csv_path = 'client.csv'

# Loading the referral tree
referral_tree = load_referral_tree(csv_path)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        client_email = request.form['client_email']
        referrals = get_referrals(client_email, referral_tree)
        return render_template('index.html', referrals=referrals, client_email=client_email)
    return render_template('index.html')