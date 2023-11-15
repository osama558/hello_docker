from markupsafe import escape

def hello_world():
    return "<p>Hello, World!</p>"

def name(name):
    return f"<p>Hello, {escape(name)} </p>"
