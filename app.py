from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory "database"
ideas = []

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		idea = request.form.get('idea')
		if idea:
			ideas.insert(0, idea)
		return redirect('/')
	return render_template('index.html', ideas=ideas)

if __name__ == '__main__':
	app.run(debug=True)
