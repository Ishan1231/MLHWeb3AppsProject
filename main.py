from flask import Flask, request

app = Flask(__name__)


@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    required_money = request.form.get('required-money')
    description = request.form.get('description')

    print(f'Name: {name}, Email: {email}, Required Money: {
          required_money}, Description: {description}')

    return 'Form submitted'


if __name__ == '__main__':
    app.run(debug=True)
