from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SECRET_KEY"] = "secret_key"
db = SQLAlchemy(app)
login_manager = LoginManager(app)


## Models

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    comments = db.relationship("Comment", backref="post", lazy=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship("User", backref="comments", lazy=True)


## Forms

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=64)])
    email = StringField("Email", validators=[InputRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=128)])

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=64)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=128)])

class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(min=4, max=100)])
    content = TextAreaField("Content", validators=[InputRequired()])
    category = StringField("Category", validators=[InputRequired(), Length(min=4, max=50)])

class CommentForm(FlaskForm):
    content = TextAreaField("Comment", validators=[InputRequired()])


## Routes

@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
    return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template("post.html", post=post, comments=comments)

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, category=form.category.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("create.html", form=form)

@app.route("/update/<int:post_id>", methods=["GET", "POST"])
@login_required
def update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        db.session.commit()
        return redirect(url_for("index"))
    form.title.data = post.title
    form.content.data = post.content
    form.category.data = post.category
    return render_template("update.html", form=form)

@app.route("/delete/<int:post_id>")
@login_required
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/comment/<int:post_id>", methods=["GET", "POST"])
@login_required
def comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post=post, author=current_user)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("post", post_id=post_id))
    return render_template("comment.html", form=form, post=post)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form["query"]
    posts = Post.query.whoosh_search(query).all()
    return render_template("search.html", posts=posts)


## Error Handlers

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403


## Login Manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)