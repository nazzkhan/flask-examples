from flask import Flask, redirect, url_for 
app=Flask(__name__) 

@app.route("/") 
def greet():
    return ("https://blinkit.com/")

@app.route("/blinkit")
def blinkit():
    return redirect("https://blinkit.com/")


if __name__=="__main__":
    app.run(debug=True, port=5002)
