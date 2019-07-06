# app.py for Takumi CHCH

from flask import Flask, render_template, request, redirect, session

#configure db
##mydb = mysql.connector.connect(
##    host="localhost",
##    user="root",
##    passwd="password",
##)

app = Flask(__name__)

#############################
#########Home page###########
#############################
@app.route('/')
def home():
        return render_template('takumihome.html')

# Debugger
if __name__=="__main__":
	app.run(debug=True)
