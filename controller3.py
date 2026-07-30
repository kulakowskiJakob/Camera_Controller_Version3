import threading
import time

class Controller:

    def __init__(self, camera, encoder, streamer, uploader):
        self.camera = camera
        self.encoder = encoder
        self.streamer = streamer
        self.uploader = uploader

        self.running = False
        self.thread = None

    def start(self):

        if self.running:
            return

        self.running = True

        self.camera.start()
        self.encoder.start()
        self.uploader.start()
        self.streamer.start()

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

    def run(self):

        while self.running:
            time.sleep(1)

    def stop(self):

        if not self.running:
            return

        self.running = False

        self.streamer.stop()
        self.uploader.stop()
        self.encoder.stop()
        self.camera.stop()

        if self.thread is not None:
            self.thread.join(timeout=2)

        print("done")
        