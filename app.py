import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

FORM_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Send Names to EC2</title>
</head>
<body>
    <h2>Enter Names (comma-separated)</h2>
    <form method="POST" action="/send_names">
        <input type="text" name="names" />
        <input type="submit" value="Send" />
    </form>
</body>
</html>
"""


@app.route("/send_names", methods=["GET", "POST"])
def send_names():
    if request.method == "POST":
        names = request.form["names"]
        try:
            response = requests.post(
                "http://52.14.156.99:5000/receive_data", json={"names": names}
            )
            print(response.text)
            return f"Response from EC2: {response.text}"
        except requests.exceptions.RequestException as e:
            print(e)
            return str(e)

    return render_template_string(FORM_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True)
