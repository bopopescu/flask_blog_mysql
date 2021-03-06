from functools import wraps
from flask import session, request, redirect, url_for, abort

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('username'):
            return redirect(url_for('login', next=request.url))
            # returns you to same page as the page you logged in from
        return f(*args, **kwargs)
    return decorated_function

def author_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('is_author'):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function