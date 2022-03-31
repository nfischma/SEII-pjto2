from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# if request.form['submit'] == 'Refresh':
#         estado_l1 = request.form.get("onoff1")
#         estado_l2 = request.form.get("onoff2")
#         print(estado_l1, estado_l2)

if __name__ == "__main__":
    app.run(debug=True, port = 5000)