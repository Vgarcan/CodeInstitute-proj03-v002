import functools

"""
Using `functools.wraps` in Python Decorators

`functools.wraps` is used to preserve the metadata of the original function when creating decorators. It maintains the original function’s name, docstring, and other attributes.

Example:
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before func()")
        result = func(*args, **kwargs)
        print("After func()")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World")


Without `functools.wraps`, the metadata of the original function is lost, which can cause issues with debugging and documentation.

Resources:
- functools.wraps: https://docs.python.org/3/library/functools.html#functools.wraps
"""

from flask import redirect, url_for, flash
from flask_login import current_user


def role_checker(role):
    """
    A decorator function that checks the user's role before allowing access to a route.

    Parameters:
    role (str): The required role for accessing the route.

    Returns:
    function: The decorated function that checks the user's role.
    """

    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            """
            The decorated function that checks the user's role.

            Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

            Returns:
            function or redirect: The original function if the user has the required role,
                                  otherwise, a redirect to the error page.
            """
            if current_user.role != role:
                flash("You do not have permission to view this page!", "danger")
                if role == "user":
                    return redirect(url_for("main.error403"))
                elif role == "company":
                    return redirect(url_for("main.error403"))

            return f(*args, **kwargs)

        return decorated_function

    return decorator
