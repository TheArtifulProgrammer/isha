from flask import Flask, request, render_template
from flask_cors import CORS
from isha import Isha
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'Ri6p4zytT3BlbkFJ8jhsr7q8ma'
CORS(app)


@app.route("/")
def hello():
    return 'Hello World'

@app.route('/hi/isha', methods=['POST'])
async def isha():
    question = request.json['question']
    res, status = await Isha().patient_entry(question)
    return res, status


if __name__ == "__main__":
    app.run(debug=True)
