from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

import os


class Encoder:

    def __init__(self,
                 camera,
                 output_directory="hls",
                 bitrate=4000000):

        self.camera = camera

        self.output_directory = output_directory
        self.bitrate = bitrate

        self.encoder = None
        self.output = None

        self.running = False


    def start(self):

        if self.running:
            return


        print("[Encoder] Starting H.264/HLS encoder...")


        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)


        picam2 = self.camera.get_camera()


        self.encoder = H264Encoder(
            bitrate=self.bitrate
        )


        hls_file = os.path.join(
            self.output_directory,
            "stream.m3u8"
        )


        ffmpeg_options = (
            "-f hls "
            "-hls_time 2 "
            "-hls_list_size 5 "
            "-hls_flags delete_segments "
        )


        self.output = FfmpegOutput(
            ffmpeg_options + hls_file
        )


        picam2.start_recording(
            self.encoder,
            self.output
        )


        self.running = True


        print("[Encoder] HLS stream created.")



    def stop(self):

        if not self.running:
            return


        print("[Encoder] Stopping encoder...")


        picam2 = self.camera.get_camera()


        picam2.stop_recording()


        self.running = False


        print("[Encoder] Encoder stopped.")



    def is_running(self):

        return self.running    
