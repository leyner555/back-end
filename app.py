from flask import Flask, render_template, request
import pyrebase
app = Flask(__name__)

config = {
  'apiKey': "AIzaSyCpmhkLCAYygYIF2zrteVo2UvPQCTPKvSg",
  'authDomain': "back-end-379220.firebaseapp.com",
  'projectId': "back-end-379220",
  'storageBucket': "back-end-379220.appspot.com",
  'messagingSenderId': "518519562623",
  'appId': "1:518519562623:web:e7e530b11fc6e772563a4a",
  'databaseURL':""
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def basic():
	unsuccessful = 'error'
	successful = 'register'
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['pass']
		try:
           
			auth.create_user_with_email_and_password(email, password)
			return render_template('new.html',s=successful )
		except:
			return render_template('new.html', us=unsuccessful)

	return render_template('new.html')




if __name__ == '__main__':
	app.run()


#email ="leyner@savimbo.com"
#password ="1224343"
#user = auth.create_user_with_email_and_password(email, password)
#user = auth.sign_in_with_email_and_password(email, password)
#auth.send_email_verification(user['idToken'])
#auth.send_password_reset_email(email)
#auth.get_account_info(user['idToken'])

