import flask

app= flask.Flask(__name__, static_url_path='/', static_folder='build/html/')

@app.route('/')
@app.route('/<path:path>')
def serve_sphinx_docs(path='index.html'):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

