from matrix_notifier.app import app, add_send_message_endpoint
from config import notifier


if __name__ == '__main__':
    add_send_message_endpoint(notifier)
    app.run(debug=True, host='127.0.0.1', port=31471)
