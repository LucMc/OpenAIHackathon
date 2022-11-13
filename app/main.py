from flask import Flask
from flask import render_template, url_for, redirect, request
import openai
# For the API to work set your OpenAI API Key like follows
# export OPENAI_API_KEY="<OPENAI_API_KEY>"

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

MODEL_ID = 'curie:ft-oai-hackathon-2022-team-20-2022-11-13-10-10-42'

@app.route("/",methods=["POST","GET"])
def homepage():
   return render_template('homepage.html')


@app.route("/optim",methods=["POST"])
def optim():

   prompt = request.form.get("prompt")
   print("Starting request to API...")
   result = openai.Completion.create(
      model=MODEL_ID,
      prompt=prompt,
      max_tokens=200)
   suggested_code = result['choices'][0]['text']
   print("finished")
   return suggested_code

if __name__ == '__main__':
   app.run(debug = True)