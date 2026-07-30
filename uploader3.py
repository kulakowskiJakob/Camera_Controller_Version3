import threading
import queue
import time
import os


class Uploader:

    def __init__(self):

        self.running = False
        self.thread = None
        self.upload_queue = queue.Queue()

    def start(self):

        if self.running:
            return

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

    def run(self):

        while self.running:

            try:

                file_path = self.upload_queue.get(
                    timeout=1
                )

                self.upload_file(file_path)

            except queue.Empty:

                continue

    def add_file(self, file_path):


        if os.path.exists(file_path):

            self.upload_queue.put(file_path)

    def upload_file(self, file_path):


        print("[Uploader] Uploading:", file_path
            )

        time.sleep(2)

        print(
            "[Uploader] Finished:", file_path
        )

    def stop(self):

        if not self.running:
            return

        self.running = False

        if self.thread:

            self.thread.join(
                timeout=2
            )

        print("GOTCHA")
        