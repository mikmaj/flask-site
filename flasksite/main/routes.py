from flask import render_template, request, Blueprint
from flasksite.models import Post

# A Blueprint is a way to organize a group of related views and other code.
# Rather than registering views and other code directly with an application, they are registered with a blueprint.
# Then the blueprint is registered with the application when it is available in the factory function.

main = Blueprint('main', __name__)

# The home page route, can be accessed with root url or with /home. 
@main.route("/")
@main.route("/home")
def home():
    # Make sure we start on the first page on load
    page = request.args.get('page', 1, type=int)
    # Query the posts from the db, order them by date (desc) and allow 5 posts per page.
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    # Return the template and pass posts to it
    return render_template('home.html', posts=posts)

# The about page route
@main.route("/about")
def about():
    return render_template('about.html', title='About')
