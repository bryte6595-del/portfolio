from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send():
    name    = request.form.get('name')
    email   = request.form.get('email')
    service = request.form.get('service')
    message = request.form.get('message')
    print(f"Message from {name} ({email}) [{service}]: {message}")
    return render_template('thanks.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
