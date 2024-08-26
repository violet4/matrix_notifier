from flask import Flask, request, jsonify
from threading import Lock

from matrix_notifier.matrix_connection import MatrixNotifier

app = Flask(__name__)
lock = Lock()


def add_send_message_endpoint(matrix_notifier:MatrixNotifier):
    @app.route('/send', methods=['POST'])
    def send_message():
        message_content = request.json.get('message')
        if message_content is None:
            return jsonify({"error": "No message provided"}), 400

        try:
            with lock:
                matrix_notifier.send_message(message_content)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify({"success": True}), 200
