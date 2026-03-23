from flask import Flask, render_template


# Lab 12 - Aidan Thoma
# Flask needs to know the name of this file to find templates and static files
app = Flask(__name__)

# ============================================================
#  ROUTE 1 — Home page
#  Visit: http://YOUR_IP:8080/
# ============================================================
@app.route('/')
def home():
    # render_template loads templates/home.html and sends it to the browser
    return render_template('home.html', page_title="Aidan Thoma's Flask Site")


# ============================================================
#  ROUTE 2 — Hello page with a URL variable
#  Visit: http://YOUR_IP:8080/hello/YourName/
#  Anything you put after /hello/ becomes the `name` variable
# ============================================================
@app.route('/hello/<name>/')
def hello(name):
    return render_template('hello.html', name=name)


# ============================================================
#  YOUR ROUTES GO BELOW THIS LINE
#  Each exercise asks you to add a new @app.route here
# ============================================================
@app.route('/analyze/<word>/')
def analyze(word):
    vowels = {'a','e','i','o','u'}
    number = len(word)
    
    vowel_count = 0
    for char in word:
        if char.lower() in vowels:
            vowel_count += 1
    
    reversed_word = word[::-1]

    return render_template('analyze.html', word=word, number=number, vowel_count=vowel_count, reversed_word=reversed_word)



# ============================================================
#  These two lines always stay at the bottom of the file.
#  host='0.0.0.0' means "listen on all network interfaces"
#  so the server is reachable from outside EC2, not just locally
# ============================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
