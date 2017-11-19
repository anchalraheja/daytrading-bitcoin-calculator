from __future__ import division
from flask import flash

from flask import Flask, request, render_template
app = Flask(__name__)



@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		btc = float(request.form['btc'])
		profit = float(request.form['profit'])

		print(btc)
		print(profit)

		a = float(profit) / 100
		print(a)

		b = 1.005012531 * float(btc)
		print(float(b))

		s = float(1 + a) * float(b)
		print "%.16f" % s

		flash('BTC. ' + "%.16f" % s,'success')





	return render_template('home.html')




if __name__ == '__main__':
	app.secret_key='anchal'
	app.run(debug=True)