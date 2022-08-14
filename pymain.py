import json
from flask import request
from flask import Flask, render_template
# Step1: -  In Python Create a Flask Application -> this is now starting the process of creating a web development site.


class AskQuestion:
    def __init__(self, idd, name , age, question,extraNotes):
        #If you print here anything it print automaticlly.
        self.idd = idd
        self.name = name
        self.age = age
        self.question = question
        self.extraNotes = extraNotes
        
    def saveData(self):
        # save these data in database/files
        with open("askQuestionData.txt" , "a") as f:
            f.write(f"{self.idd},{self.name},{self.age},{self.question},{self.extraNotes}\n");
        

app = Flask(__name__ , template_folder ='templates')

# Step2:-  Create the WEB route for telling the programme what the HTML template is called.
@app.route('/')
def index():
    return render_template('index.html')

# Create the logic that will receive the data from the JSON on the website.
@app.route('/test' , methods = ['POST'])
def test():
    output = request.get_json()
    print("This is the output that was stored in the JSON within te browser" , output , type(output))
    
    result = json.loads(output) # this converts  the json output to a python dictionary
    print(result, type(result))
    data = AskQuestion(result["idd"], result["name"], result["age"], result["question"], result["extranotes"] )
    data.saveData()
    
    return "Done"
    
if __name__ =="__main__":
    app.run(debug = False )
    #port= 8000 