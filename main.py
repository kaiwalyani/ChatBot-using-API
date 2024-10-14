from flask import Flask, render_template, request
import google.generativeai as genai

app =  Flask(__name__)

GOOGLE_API_KEY='Paste_Your_API_key'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])

def get_response():
    user_input = request.form['user_input']
    response = model.generate_content(user_input)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
