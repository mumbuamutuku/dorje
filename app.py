from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

JOBS = [
  {
  'id': 1,
  'title':'Data Analyst',
  'location': 'Nairobi',
  'Salary': 'Kshs 290000'
},
{
  'id': 2,
  'title':'Data Scientist',
  'location': 'Nakuru',
  'Salary': 'Kshs 200000'
},
{
  'id': 3,
  'title':'Frontend Engineer',
  'location': 'Remote',
  'Salary': 'USD 10000'
},
  {
    'id': 4,
  'title':'backend Engineer',
  'location': 'Remote',
  }
]
@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Dorje')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)