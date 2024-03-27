'''
This is a multiline
comment in Python
'''

import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    target = request.args["target"]

    # BAD: user has full control of URL
    resp = requests.get("https://" + target + ".example.com/data/")

    # GOOD: `subdomain` is controlled by the server.
    subdomain = "europe" if target == "EU" else "world"
    resp = requests.get("https://" + subdomain + ".example.com/data/")

'''
This is a multiline
comment in Python
'''

@app.route("/partial_ssrf")
def partial_ssrf():
    user_id = request.args["user_id"]

    # BAD: user can fully control the path component of the URL
    resp = requests.get(f"https://api.example.com/user_info/{user_id}",
                       params={"userId": user_id}
                       )

    if user_id.isalnum():
        # GOOD: user_id is restricted to be alpha-numeric, and cannot alter path component of URL
        resp = requests.get("https://api.example.com/user_info/" + user_id)


'''
This is a multiline
comment in Python
'''
