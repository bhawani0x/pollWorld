from flask import Blueprint, request, render_template
from flask.views import View
# from api.Forms.signupForm import RegistrationForm
from api.Models.User import User
import datetime
from api.Helper.helper import response

signup_bp = Blueprint("signup", __name__)


class Signup(View):
    def dispatch_request(self):
        if request.method == "POST":
            return self.SignupPage()

    def SignupPage(self):
        data = request.get_json()
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        mob = data.get('mob_num')
        dob = datetime.datetime.strptime(data.get('dob'), '%d-%m-%Y').date()
        gender = data.get('gender')
        password = data.get('paswd')

        user = User().create_user(name, username, email, password, mob, dob, gender)
        if user:
            return response(msg="user created successful", code=201)
        return response(msg="unable to user create", code=400)

    # def SignupPage(self):
    #     form = RegistrationForm()
    #     if form.validate_on_submit():
    #         user = User().create_user(
    #             form.name,
    #             form.username,
    #             form.email,
    #             form.password,
    #             form.mobile_number,
    #             form.dob,
    #             form.gender,
    #         )
    #         if user:
    #             return "user Created"
    #     return render_template("SignupPage.html", form=form)
