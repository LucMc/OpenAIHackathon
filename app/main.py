from flask import Flask
import os
from flask import render_template, url_for, redirect, request
import openai
# For the API to work set your OpenAI API Key like follows
# export OPENAI_API_KEY="<OPENAI_API_KEY>"

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

MODEL_ID = 'davinci:ft-oai-hackathon-2022-team-20-2022-11-13-17-33-32'

@app.route("/",methods=["POST","GET"])
def homepage():
   return render_template('homepage.html')


@app.route("/optim",methods=["POST"])
def optim():
   prompt = request.form.get("prompt")
   print("Starting request to API...")
   # result = openai.Completion.create(
   #    model=MODEL_ID,
   #    prompt=prompt,
   #    max_tokens=200)
   # suggested_code = result['choices'][0]['text']
   # print("finished")
   suggested_code = prompt
   return suggested_code

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

if __name__ == '__main__':
   app.run(debug = True)