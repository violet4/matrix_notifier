
# Matrix Notifier

Matrix Notifier presents a simple python program that opens a long-lived connection to a Matrix server instance and listens for HTTP requests on localhost to send messages on your behalf.

This makes it easy to enable any program that is capable of sending a localhost HTTP request to send messages within Matrix.

Uses Python, python-nio, and flask.

Installation:
* Ensure you meet the installation requirements for python matrix-nio, particularly the libolm dependency for your operating system / distribution: https://matrix-nio.readthedocs.io/en/latest/#installation
* `poetry install --with=client`
* `cp config.py.sample config.py`
* Fill out the values in `config.py`
* `./start.sh` in one terminal
* From another terminal: `poetry run python send_message.py 'hello!'`

Initial version can only send a single text-based message at a time to a single room. The only configuration options are:
* Homeserver
* username (we recommend making a dedicated account for your sender)
* password
* target room ID (the room where messages will be sent)
* device name (e.g. `python_matrix_notifier` to correspond to this program)
