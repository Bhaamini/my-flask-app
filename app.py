from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "<h1>My DevOps Portfolio App</h1><p>Flask is running.</p>"


@app.get("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=True)