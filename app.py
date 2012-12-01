from flask import Flask, request, url_for, redirect, render_template, flash
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "Hola"

if __name__ == '__main__':
    app.run(debug=True)