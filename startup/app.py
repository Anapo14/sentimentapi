from flask import Flask
from textblob import TextBlob

# create Flask app
app = Flask(__name__)

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Python loves VS Toolbox!'

# create sentiment api
@app.route('/<message>')
def index(message):
    sentiment = "positive"
    # if (TextBlob(message).sentiment.polarity < 0.0):
    #     sentiment = "negative"
    return app.make_response(sentiment)