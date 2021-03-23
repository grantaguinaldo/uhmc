from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def data():
    return render_template('uhmc-data.html')

if __name__ == "__main__":
    app.run(debug=True)