from flask import Flask

app=Flask(__name__)

@app.route('/')
def homepage():
    return('hello gpcet-ai chaithu ai how are you.')

if (__name__=="__main__"):
    app.run()