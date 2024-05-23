from flask import Flask, render_template, request, redirect, url_for
from main import otp_verify, gmail_verify
import re

class OTPGenerator:
    otp = ''

    @classmethod
    def generate_otp(cls):
        cls.otp = otp_verify()
        return cls.otp

to_email = ''
verify_otp = int()

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET' ])
def index():
    print(request.method)
    if request.method == 'GET':
        return render_template('index.html')
    else:
        to_email = request.form['emailID']
        pattern = '@gmail.com'
        res = re.findall(pattern, to_email)
        print(res)
        if res:
            print('Valid')
        else:
            print('Invalid')
            return render_template('index.html', res = 'invalid')
        print(to_email)
        otp = OTPGenerator.generate_otp()

        # print(otp)
        gmail_verify(to_email, otp)
        return render_template('verify.html')
    
@app.route('/verify', methods = ['POST', 'GET'])
def verify():
    print(request.method)
    if request.method == 'POST':
        verify_otp = request.form['verify']
        otp = OTPGenerator.otp
        print(otp)
        print("otp: ", otp, '\n' 'verify_otp: ',verify_otp)
        if verify_otp == otp:
            return render_template('email_verify.html')
        else:
            return render_template('invalid.html')

if __name__ == '__main__':
    app.run(debug=True)