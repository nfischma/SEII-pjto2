from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")
    

@app.route("/ligarled1", methods = ["POST"])
def ligarled1():
    print("L1 ligada")
    modificar_estado(1,"ON")
    return render_template("index.html")

@app.route("/desligarled1", methods = ["POST"])
def desligarled1():
    print("L1 desligada")
    modificar_estado(1,"OFF")
    return render_template("index.html")

@app.route("/ligarled2", methods = ["POST"])
def ligarled2():
    print("L2 ligada")
    modificar_estado(2,"ON")
    return render_template("index.html")

@app.route("/desligarled2", methods = ["POST"])
def desligarled2():
    print("L2 desligada")
    modificar_estado(2,"OFF")
    return render_template("index.html")


def modificar_estado(led,estado):
    f = open('estados.txt','r')
    print(f)
    for estados in f:
        print(estados)
        estados = estados.split(";")
        print(estados)
        if estado=="ON":
            estados[led-1]="1"
        else:
            estados[led-1]="0"
        novos_estados = estados[0] + ";" + estados[1]
    f.close()
    f1 = open('estados.txt', 'w')
    f1.write(novos_estados)
    f1.close()

    

if __name__ == "__main__":
    app.run(debug=True, port = 5000)