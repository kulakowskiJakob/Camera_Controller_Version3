import os
import threading
import subprocess
import time

from flask import Flask, send_from_directory, send_file

class Streamer:

    def __init__(self,
                 host="0.0.0.0",
                 port=5000,
                 stream_directory="hls"):

        self.host = host
        self.port = port

        self.stream_directory = stream_directory

        self.app = Flask(__name__)

        self.server_thread = None
        self.ffmpeg_process = None

        self.running = False

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/")
        def index():

            return send_file(
                "index.html"
             )

        @self.app.route("/stream.m3u8")
        def playlist():

            return send_from_directory(
                self.stream_directory,
                "stream.m3u8"
            )

        @self.app.route("/<path:file>")
        def files(file):

            return send_from_directory(
                self.stream_directory,
                file
            )

    def start(self):

        if self.running:
            return

        if not os.path.exists(self.stream_directory):
            os.makedirs(self.stream_directory)

        self.start_ffmpeg()

        self.running = True

        self.server_thread = threading.Thread(
            target=self.run_server,
            daemon=True
        )

        self.server_thread.start()

        print("[Streamer] Running on port",
               self.port)

    def start_ffmpeg(self):

        command = [
            "ffmpeg",
            "-y",

            "-f",
            "h264",

            "-i",
            "video.h264",

            "-c:v",
            "copy",

            "-f",
            "hls",

            "-hls_time",
            "2",

            "-hls_list_size",
            "5",

            "-hls_flags",
            "delete_segments",

            f"{self.stream_directory}/stream.m3u8"
        ]

        self.ffmpeg_process = subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def run_server(self):

        self.app.run(
            host=self.host,
            port=self.port,
            threaded=True,
            use_reloader=False
        )

    def stop(self):

        if not self.running:
            return

        self.running = False

        if self.ffmpeg_process:

            self.ffmpeg_process.terminate()


        print("GOTCHA")

        
