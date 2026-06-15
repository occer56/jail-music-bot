app = Flask(__name__)

HOUSE_STREAMS = [
"https://www.youtube.com/watch?v=vHIob3bT0pk", # placeholder
]

@app.route("/incoming", methods=["POST"])
def incoming():
response = VoiceResponse()
# Auto-press 5 to accept jail call
response.play(digits="5")
gather = Gather(num_digits=1, action="/menu", timeout=10)
gather.say("Welcome. Press 1 for deep house. Press 2 for tech house. Press 3 for classic house.")
response.append(gather)
return Response(str(response), mimetype="text/xml")

@app.route("/menu", methods=["POST"])
def menu():
digit = request.form.get("Digits", "1")
response = VoiceResponse()
streams = {
"1": "https://stream.radioparadise.com/mellow-flac",
"2": "https://stream.radioparadise.com/rock-flac",
"3": "https://stream.radioparadise.com/flac",
}
url = streams.get(digit, streams["1"])
response.play(url)
return Response(str(response), mimetype="text/xml")

if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
Tq
