from flask import Flask, render_template, request
# from flask.wrappers import Request
from flasgger import Swagger

# WSGI
app = Flask(__name__)
Swagger(app)

@app.route('/')
def welcome():
    return "Learning Swagger Building"

@app.route('/anothername/<your_name>')
def names(your_name):
    return f"Welcome to Praxis {your_name}" 


@app.route('/checking_req',methods =['GET','POST'], )
def get_req_parameters():

    """ Practicing Swagger
    ---
    parameters:
      - name: Student_name
        in: query
        type: string
        required: true
      - name: roll_no
        in: query
        type: number
        required: true
    responses:
        200:
            description: Result is 
    
    """
    name = request.args.get("Student_name")
    roll_no = request.args.get("roll_no")
    return f"Student name is {name} and roll number is {roll_no}"

if __name__ == '__main__':
    app.run(debug= True,port=3400)