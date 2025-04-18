from flask import Flask, request, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyCDMou0uNoCDkVbFeZEfUsiD9rJnalrcro")

@app.route('/', methods=['GET', 'POST'])
def index():
    story = None
    if request.method == 'POST':
        prompt = request.form['prompt']
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Generate a short story based on the following prompt: {prompt}")
        story = response.text
    return render_template('index.html', story=story)

if __name__ == '__main__':
    app.run(debug=True)