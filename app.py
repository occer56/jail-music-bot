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
    streams = {
        "1": "https://ice2.somafm.com/deepspaceone-128-mp3",
        "2": "https://ice2.somafm.com/techno-128-mp3",
        "3": "https://ice2.somafm.com/groovesalad-128-mp3",
    }
    url = streams.get(digit, streams["1"])
    response.play(url)
    return Response(str(response), mimetype="text/xml")

if __name__
