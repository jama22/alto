from flask import escape, render_template
import functions_framework
@functions_framework.http
def alto_function_http(request): 
    return render_template("index.html")