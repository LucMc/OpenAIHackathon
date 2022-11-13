from flask import Flask
from flask import render_template, url_for, redirect, request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/",methods=["POST","GET"])
def homepage():
    if request.method == "POST":
        todo = request.form.get("todo")
        print(todo)
    return render_template('homepage.html')

# @app.route("/login")
# def contact(name=None):
#     return render_template('contact.html', name=name)

# @app.route("/events/")
# def events(name=None):
#     return render_template('events.html', name=name)


# @app.route('/optimized/<name>')
# def optimized(name):
#    return 'welcome %s' % name

# @app.route('/submit',methods = ['POST'])
# def submit():
#       user = request.form['nm']
#       return redirect(url_for('optimized',name = user))


if __name__ == '__main__':
   app.run(debug = True)