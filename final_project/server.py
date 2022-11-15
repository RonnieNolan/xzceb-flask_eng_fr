from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    #The translation code
    french_text= translator.english_2_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    #The translation code
    english_text= translator.french_2_english(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    #Rendering the template
    return render_template("index.html")   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
