from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': "Data Analyst",
  'location': 'Almaty, Kazakhstan',
  'salary': 'KZT, 500,000'
}, {
  'id': 2,
  'title': "Data Scientist",
  'location': 'Almaty, Kazakhstan',
}, {
  'id': 3,
  'title': "Frontend Engineer",
  'location': 'Remote',
  'salary': 'KZT, 550,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Craft')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
