from flask import Flask, render_template_x000D_
app = Flask(__name__)_x000D_
_x000D_
@app.route('/')_x000D_
def index():_x000D_
  return render_template('index.html')_x000D_
_x000D_
@app.route('/my-link/')_x000D_
def my_link():_x000D_
  print ('I got clicked!')_x000D_
_x000D_
  return 'Click.'_x000D_
_x000D_
if __name__ == '__main__':_x000D_
  app.run(debug=True)