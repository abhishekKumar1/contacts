from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask import abort
import handlers
import data
import errorhandlers

app = Flask(__name__)
auth = HTTPBasicAuth()

# For verifing password
@auth.get_password
def get_pw(username):
    if username in data.users:
        return data.users.get(username)
    abort(401)

#custom error handler for 400
@app.errorhandler(400)
def invalid_req(e):
    return jsonify(errorhandlers.error400()), 400

#custom error handler for 401
@app.errorhandler(401)
def unauthorized(e):
    return jsonify(errorhandlers.error401()), 401

#custom error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(errorhandlers.error404()), 404

#custom error handler for 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify(errorhandlers.error500()), 500

#Are you alive endpoint
@app.route("/", methods=["GET"])
@auth.login_required
def abc():
    return jsonify({'I am alive': true})

#Search by email endpoint
@app.route("/get/email/<email>", methods=["GET"])
@auth.login_required
def get_email(email):
    user = handlers.get_by_email(email)
    if user == False :
        abort(404)
    return jsonify(user)

#Search by first name endpoint
@app.route("/get/name/<name>", methods=["GET"])
@auth.login_required
def get_by_name(name):
    number_of_request = 10
    offset = request.args.get('offset')
    if offset is None :
        users = handlers.get_by_first_name(name, number_of_request, 0)
    else:
        users = handlers.get_by_first_name(name, number_of_request, int(offset))
    if users == False :
        abort(404)
    return jsonify(users)

#Adding a new user endpoint
@app.route("/add", methods=["POST"])
@auth.login_required
def add_user():
    try:
        checkin_resp = request.form
        first_name = checkin_resp.get('first_name')
        last_name  = checkin_resp.get('last_name')
        email = checkin_resp.get('email')
        phone_number = checkin_resp.get('phone_number')
        if first_name and email and phone_number is not None:
            flag = handlers.add_user_in_db(first_name, last_name, email ,phone_number)
            if flag == True:
                status = "Success"
            else:
                status = "Failed"
            return jsonify({'Response status': status})
        else:
            abort(400)
    except Exception as e:
        abort(500)

#Deleting a use endpoint
@app.route("/delete/<email>", methods=["DELETE"])
@auth.login_required
def delete_user(email):
    try:
        if email is not None:
            flag = handlers.delete_user_in_db(email)
            if flag == True :
                return jsonify({'Response status': "Success"})
            else:
                abort(404)
        else:
            abort(400)
    except Exception as e:
        abort(500)
if __name__ == '__main__':
    app.run(debug=True)
