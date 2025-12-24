from flask import Flask, render_template, request
import io

app = Flask(__name__)

# Секретний ключ краще тримати в .env файлі
app.config['SECRET_KEY'] = "90ce45547a4f5b5019fb726383c96689bdea90fd25a45ad3ef0a88000b6de32a"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    user_file = request.files.get('user_file')

    if user_file.mimetype != 'text/plain':
        return render_template('index.html', content="SERVER: Not a txt file")

    file_data = user_file.read()

    if len(file_data) > 10 * 1024 * 1024:
        return "SERVER: Size limit is 10mb"

    content = file_data.decode('utf-8')

    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8000)