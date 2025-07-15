from flask import Flask, request, render_template_string

app = Flask(__name__)
messages = []

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.json
    messages.append(data.get('msg', ''))
    return {'status': 'received'}, 200

@app.route('/')
def show_messages():
    return render_template_string("""
        <h1>Messages Received</h1>
        <ul>{% for msg in messages %}<li>{{ msg }}</li>{% endfor %}</ul>
    """, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
