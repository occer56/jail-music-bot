from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather
import os

app = Flask(__name__)

@app.route("/incoming", methods=["POST"])
def incoming():
    response = VoiceResponse()
    response.play(digits="5")
    gather = Gather(num_digits=1, action="/menu", timeout=10)
    gather.say("Welcome. Press 1 for deep house. Press 2 for tech house. Press 3 for classic house.")
    response.append(gather)
    return Response(str(response), mimetype="text/xml")

@app.route("/menu", methods=["POST"])
def menu():
    digit = request.form.get("Digits", "1")
    response = VoiceResponse()
    response.say("You pressed " + digit + ". Music coming soon. Thank you.")
    return Response(str(response), mimetype="text/xml")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
