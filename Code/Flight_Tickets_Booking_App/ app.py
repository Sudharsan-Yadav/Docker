from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flight Ticket Booking</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f5f7fa; }
        h1 { color: #1f4fd8; }
        form { background: white; padding: 20px; width: 350px; border-radius: 8px; }
        input, button { width: 100%; padding: 8px; margin-top: 10px; }
        .result { margin-top: 20px; background: #eaffea; padding: 15px; }
    </style>
</head>
<body>

<h1>✈ Flight Ticket Booking</h1>

<form method="POST">
    <input name="source" placeholder="From" required>
    <input name="destination" placeholder="To" required>
    <input type="number" name="passengers" min="1" value="1" required>
    <button type="submit">Search Flights</button>
</form>

{% if result %}
<div class="result">
    <h3>✅ Booking Details</h3>
    <p><b>Route:</b> {{source}} → {{destination}}</p>
    <p><b>Passengers:</b> {{passengers}}</p>
    <p><b>Total Price:</b> ₹{{price}}</p>
</div>
{% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]
        passengers = int(request.form["passengers"])
        price = passengers * 6500

        return render_template_string(
            HTML_PAGE,
            result=True,
            source=source,
            destination=destination,
            passengers=passengers,
            price=price
        )

    return render_template_string(HTML_PAGE, result=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
