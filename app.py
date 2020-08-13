from flask import Flask, request, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("catform.html")
    
@app.route('/category',methods = ['POST', 'GET'])
def category():
   if request.method == 'POST':
      category = request.form
      return render_template("post.html",category = category)
    

if __name__ == "__main__":
    app.run(debug=True)