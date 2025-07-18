from flask import Flask,Response,stream_with_context,render_template
import time
import random
import string
import json
app=Flask(__name__)


def generate_random_string():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/text-content')
def text_content():
    @stream_with_context
    def generate():
        while True:
            yield 'data: {}\n\n'.format(time.time())
            time.sleep(1)
    return Response(generate(), mimetype='text/event-stream')



@app.route('/json-content')
def json_content():
    @stream_with_context
    def generate():
        while True:
            
            data={
                "string":generate_random_string(),
                "number":random.randint(1,100)
            }
            
            yield 'data: {}\n\n'.format(json.dumps(data))
            time.sleep(1)
    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True,threaded=True)
