from api.app import app
from api.Controllers.Auth.Signup import signup_bp, Signup
from api.Controllers.Auth.Login import login_bp, Login
from api.Controllers.Categories.categories import category_bp, Category


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)

app.add_url_rule("/signup", view_func=Signup.as_view('signup'), methods=['GET', 'POST'])
app.add_url_rule("/login", view_func=Login.as_view('login'), methods=['POST'])
app.add_url_rule("/topics", view_func=Category.as_view("categories"), methods=['GET', 'POST'])
