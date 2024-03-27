from flask import Flask, request
from flask_mfa import MFA

app = Flask(__name__)
mfa = MFA(app)

@app.route('/login', methods=['POST'])
@mfa.required
def login():
    # Authenticate user and grant access
    return 'Login successful'

if __name__ == '__main__':
    app.run()
