from flask import Flask, request, render_template, url_for

app = Flask(__name__)

@app.route('/view/<program>')
def view(program=None):
    if program == '1':
       name = 'Straight line'
       description = 'The following code will drive the picaxe robot in a straight line'
       code="""main:
       forward A;
       go forwards
       forward B
       goto main"""

#    if program == '2':



    return render_template('index.html', name=name, description=description,
                           code=code)

if __name__ == "__main__":
    app.run(debug=True)



