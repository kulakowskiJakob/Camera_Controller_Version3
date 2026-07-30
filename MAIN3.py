import signal
import sys
import time

from camera import Camera
from encoder import Encoder
from streamer import Streamer
from controller import Controller
from uploader import Uploader

def main():

    camera = Camera(
        width=1280,
        height = 720,
        framerate=30,
    )

    encoder = Encoder(
        camera=camera,
        output_directory="hls",
        bitrate=4000000
    )

    controller = Controller(
        camera=camera,
        encoder=encoder,
        streamer=streamer,
        uploader=uploader
    )

    def shutdown(signum, frame):
        controller.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    controller.start()

    print("")
    print("Server Running")
    print("--------------------")
    print("Open your browser to:")
    print("http://localAddress>:5000/video")
    print("")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        shutdown(None, None)

if __name__ == "__main__":
    main()



