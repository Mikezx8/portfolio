from flask import Flask, send_from_directory
import os

app = Flask(__name__)
# Set the folder containing your HTML files
HTML_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "html")

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_file(path):
    # Serve any file in the HTML_DIR
    return send_from_directory(HTML_DIR, path)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
