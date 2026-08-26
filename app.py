from flask import Flask, render_template , jsonify

app = Flask(__name__)

JOBS=[
    {
        'id':1,
        'title':'Data Analyist',
        'location': 'Bengaluru',
        'salary': '10,00,000'
    },

    {
        'id':2,
        'title':'Data scientist',
        'location': 'New Delhi',
        'salary':'15,00,000'
    },

    {
        'id':3,
        'title':'Front-end engenier',
        'location': 'Remote',
        'salary':'20,00,000'
    },

    {
        'id':4,
        'title':'Back-end engenier',
        'location': 'San-Fansisco',
        'salary':'10,00,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs") #/api to know it is api
def list_jobs():
    return jsonify(JOBS)
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)