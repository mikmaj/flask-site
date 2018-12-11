from flask import Blueprint, render_template

# A Blueprint is a way to organize a group of related views and other code.
# Rather than registering views and other code directly with an application, they are registered with a blueprint.
# Then the blueprint is registered with the application when it is available in the factory function.

errors = Blueprint('errors', __name__)

# If a page is not found, return a custom 404 error page inside the layout
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

# If a page is forbidden, return a custom 403 error page inside the layout
@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

# If there's an internal server error, return a custom 500 error page inside the layout
@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
