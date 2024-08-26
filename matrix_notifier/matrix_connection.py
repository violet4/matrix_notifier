import queue
import time
import threading
import asyncio

from nio import AsyncClient


class MatrixNotifier:
    def __init__(self, homeserver:str, username:str, password:str, room_id:str, device_name:str):
        self.room_id = room_id
        self.client = AsyncClient(homeserver, username)
        self.password = password
        self.device_name = device_name
        self.message_queue = queue.Queue()

        self.thread = threading.Thread(target=self.start)
        self.thread.daemon = True
        self.thread.start()

    def send_message(self, message: str):
        self.message_queue.put(message)

    def start(self):
        asyncio.run(self.process_queue())

    async def process_queue(self):
        login_response = await self.client.login(self.password, self.device_name)
        print('login response:', login_response)

        while True:
            try:
                message = self.message_queue.get()
                await self._send_message(message)
            except Exception as e:
                print(f"Error sending message: {e}")
            time.sleep(1)

    async def _send_message(self, message: str):
        await self.client.room_send(
            room_id=self.room_id,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": message
            }
        )
