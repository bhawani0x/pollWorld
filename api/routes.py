from api.app import app
from api.Controllers.Auth.Signup import signup_bp, Signup
from api.Controllers.Auth.Login import login_bp, Login
from api.Controllers.Categories.categories import category_bp, Category
from api.Controllers.User.ProfileUpdate import profileUpdate_bp, ProfileUpdate
from api.Controllers.Posts.Posts import posts_bp, Post


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# app.register_blueprint(signup_bp)
# app.register_blueprint(login_bp)


app.add_url_rule("/signup", view_func=Signup.as_view('signup'), methods=['GET', 'POST'])
app.add_url_rule("/login", view_func=Login.as_view('login'), methods=['POST'])
app.add_url_rule("/category", view_func=Category.as_view("categories"), methods=['GET', 'POST'])
app.add_url_rule("/profile/", view_func=ProfileUpdate.as_view("profile"), methods=['GET'])
app.add_url_rule("/profile/update/", view_func=ProfileUpdate.as_view("profileUpdate"), methods=['PUT'])

app.add_url_rule("/posts", view_func=Post.as_view("allposts"), methods=['GET'])
app.add_url_rule("/posts/create", view_func=Post.as_view("createpost"), methods=['POST'])
app.add_url_rule("/posts/<id>", view_func=Post.as_view("updatepost"), methods=['PUT'])
