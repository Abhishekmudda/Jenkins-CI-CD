from flask import Flask, request, render_template

app = Flask(__name__)

def even_or_odd(num):
    if num < 1:
        return "Invalid Input"
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            result = even_or_odd(num)
        except:
            result = "Invalid Input"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
