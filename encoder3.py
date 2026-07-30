from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

import os
import threading
import time


class Encoder:

    def __init__(self,
                 camera,
                 output_directory="hls",
                 bitrate=4000000):

        self.camera = camera

        self.output_directory = output_directory
        self.bitrate = bitrate

        self.encoder = None
        self.output = FfmpegOutput(
            "-"
        )

        self.running = False
        self.thread = None
        self.h264_file = "video.h264"

    def start(self):

        if self.running:
            return

        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

            picam2 = self.camera.get_camera()

            self.encoder = H264Encoder(
                bitrate=self.bitrate
            )

            picam2.start_encoder(
                self.encoder,
                self.output
            )

            self.running = True

    def stop(self):

        if not self.running:
            return

        picam2 = self.camera.get_camera()
        picam2.stop_encoder()
        self.running = False

    def get_file(self):
        return self.h264_file

    def is_running(self):
        return self.running

    
