from flask import Flask, send_from_directory

app = Flask(
    __name__,
    static_folder="frontend/build",
    static_url_path=""
)

@app.route("/")
def serve_frontend():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
