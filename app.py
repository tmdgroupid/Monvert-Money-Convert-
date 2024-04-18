from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_currency():
    if request.method == 'POST':
        amount = request.form['amount']
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}?apikey=578affc430421d4ff12f8bd4&symbols={to_currency}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if to_currency in data['rates']:
                rate = data['rates'][to_currency]
                converted_amount = float(amount) * rate
                return str(converted_amount)
            else:
                return "Error: Currency conversion not supported"
        else:
            return "Error: Unable to fetch data from API"

    currencies = ['IDR', 'USD', 'EUR', 'GBP', 'CHF', 'AED', 'KWD']
    return render_template('index.html', currencies=currencies)

if __name__ == '__main__':
    app.run(debug=True)
