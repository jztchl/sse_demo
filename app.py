from flask import Flask,Response,stream_with_context,render_template
import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True 
)

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text-content')
def text_content():
    @stream_with_context
    def generate():
        pubsub = redis_client.pubsub()
        pubsub.subscribe('main_channel')
        for message in pubsub.listen():
            if message['type'] == 'message':
                yield f"data: {message['data']}\n\n"
    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True,threaded=True)
