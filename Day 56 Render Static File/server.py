from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(port=5050,debug=True)

# Edit on Google Developer Tools
# console --> document.body.contentEditable = true
