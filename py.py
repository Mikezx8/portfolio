from flask import Flask, send_from_directory
import os

app = Flask(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Catch-all route
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(ROOT_DIR, path)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
