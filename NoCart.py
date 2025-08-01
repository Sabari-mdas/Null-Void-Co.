from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forget', methods=['POST'])
def forget():
    memory = request.form['memory']
    # Simulate forgetting by not saving or storing the memory
    return redirect(url_for('index'))

if _name_ == '_main_':
    app.run(debug=True)
