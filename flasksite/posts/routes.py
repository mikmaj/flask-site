from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flasksite import db
from flasksite.models import Post
from flasksite.posts.forms import PostForm

# A Blueprint is a way to organize a group of related views and other code.
# Rather than registering views and other code directly with an application, they are registered with a blueprint.
# Then the blueprint is registered with the application when it is available in the factory function.

posts = Blueprint('posts', __name__)

# The route for posting a new post. Both GET and POST requests are allowed.
@posts.route("/post/new", methods=['GET', 'POST'])
# Have to be logged in to view this route.
@login_required
def new_post():
    form = PostForm()
    # If the post is valid, save it into the db and
    # flash a message with the bootstrap class 'success' and redirect to home page.
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')

# The route for viewing a single post.
@posts.route("/post/<int:post_id>")
def post(post_id):
    # Query the post with the given id and return the template or the custom 404 error page if it's not found.
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

# The route for updating a post, Both GET and POST requests are allowed.
@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
# Have to be logged in to view this route.
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    # Make sure the editor is the poster, if not, return the custom 403 error page
    if post.author != current_user:
        abort(403)
    form = PostForm()
    # If the post is valid, save it into the db and
    # flash a message with the bootstrap class 'success' and redirect to home page.
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')

# The route for deleting a post. Only POST requests are allowed
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
# Have to be logged in to view this route.
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    # If the user is not the poster, return the custom 403 error page.
    # Else delete the post from the db and flash a message with 
    # the bootstrap class 'success' and redirect to home page.
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
