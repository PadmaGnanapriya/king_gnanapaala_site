from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('home.html')


@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/article')
def article_page():
    return render_template('article.html')


@app.route('/project')
def project_page():
    return render_template('project.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


# @app.errorhandler(404)
# def page_not_found(e):
#     return "Not found in Padme site: " + request.path


if __name__ == '__main__':
    app.run()
