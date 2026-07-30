from picamera2 import Picamera2
import time

class Camera:

    def __init__ (self,
                  width=1280,
                  height=720,
                  framerate=30):
        self.width = width
        self.height = height
        self.framerate = framerate

        self.picam2 = None
        self.running = False

    def start(self):

        if self.running:
            return

        self.picam2 = Picamera2()
        config = self.picam2.create_video_configuration(

            main={
                "size": (self.width, self.height),
                "format": "YUV420"
            },
            controls={
                "FrameRate": self.framerate
            }
        )

        self.picam2.configure(config)
        self.picam2.start()

        time.sleep(2)
        self.running = True

    def stop(self):
        if not self.running:
            return

        self.picam2.stop()
        self.running = False

    def get_camera(self):
        return self.picam2

    def is_running(self):
        return self.running

    def get_resolution(self):

        return(
            self.width,
            self.height
        )

    def get_framerate(self):
        return self.framerate
    
