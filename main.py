from flask import Flask,request,jsonify
from threading import Thread
from youtube_transcript_api import YouTubeTranscriptApi as ys
from flask_cors import CORS

app = Flask("app")
CORS(app)


@app.route("/")
def landing():
    return "This page is not acessible"


@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        arr = []
        wordsarr = [[]]
        warr = [[]]
        full = ""
        words = []
        js = request.json
        print(js)
        for word in js["coins"]:
            words.append(word)
        print(words)
        for id in js["ids"]:
            ts = ys.get_transcript(id)
            for t in ts:
                for word in t["text"].split():
                    full += f"{word} "
                    arr.append(word)
            for idx in arr:
                for word in words:
                    if idx.lower() != word:
                        pass
                    else:
                        wordsarr.append(word)
                        if not word in warr:
                            warr.append(word)
        carr = [[]]
        for word in words:
          if(word not in warr):
            warr.append(word)
        for i, word in enumerate(warr):
            if not word in carr[i]:
                carr.append([word, wordsarr.count(word)])
            

        carr.remove([[], 1])
        carr.remove([])
        print(carr)
        print(words)
        print(warr)
        if(carr == []):
          for word in words:
            carr.append([word,0])
        return jsonify(carr)


Thread(target=app.run, args=("0.0.0.0", 8080)).start()


# print(arr)
# print(wordsarr)
# print(f"\n{full}")
