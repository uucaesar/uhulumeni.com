from flask import Flask, render_template

app = Flask(__name__)
application = app  # For compatibility with some deployment setups

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/learners-test-bookings')
def learners():
    return render_template("learners.html")

@app.route('/traffic-fine-reductions')
def reductions():
    return render_template("reductions.html")

if __name__ == '__main__':
    app.run(debug=True)