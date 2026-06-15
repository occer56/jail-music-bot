import os
from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

# Map keypad digits to song URLs (replace these with your actual hosted audio files)
SONGS = {
    "1": "https://example.com/song1.mp3",
    "2": "https://example.com/song2.mp3",
    "3": "https://example.com/song3.mp3",
}


@app.route("/voice", methods=["POST", "GET"])
def voice():
    """Initial call handler: plays a menu and waits for a keypad selection."""
    response = VoiceResponse()

    gather = Gather(num_digits=1, action="/play", method="POST", timeout=10)
    gather.say("Welcome. Press 1 for song one, 2 for song two, or 3 for song three.")
    response.append(gather)

    # If no input is received, this runs
    response.say("We did not receive any input. Goodbye.")
    return Response(str(response), mimetype="text/xml")


@app.route("/play", methods=["POST", "GET"])
def play():
    """Handles the keypad selection and plays the chosen song."""
    digit = request.values.get("Digits", "")
    response = VoiceResponse()

    song_url = SONGS.get(digit)
    if song_url:
        response.play(song_url)
    else:
        response.say("Invalid selection. Goodbye.")

    return Response(str(response), mimetype="text/xml")


@app.route("/", methods=["GET"])
def index():
    """Simple health check route so Railway knows the app is alive."""
    return "Jail Music Bot is running."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
