import os

CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

CAMERA_FRAMERATE = 30


VIDEO_BITRATE = 4000000

H264_OUTPUT = "video.h264"

STREAM_HOST = "0.0.0.0"
STREAM_PORT = 5000

HLS_DIRECTORY = "hls"

HLS_SEGMENT_TIME = 2
HLS_LIST_SIZE = 5

UPLOAD_ENABLED = False
UPLOAD_DIRECTORY = "uploads"


RECORDINGS_DIRECTORY = "recordings"

LOG_FILE = "camera.log"

PROJECT_DIRECTORY = os.path.dirname(
    os.path.abspath(__file__)
)

HLS_PATH = os.path.join(
    PROJECT_DIRECTORY,
    HLS_DIRECTORY
)

RECORDINGS_PATH = os.path.join(
    PROJECT_DIRECTORY,
    RECORDINGS_DIRECTORY
)

UPLOAD_PATH = os.path.join(
    PROJECT_DIRECTORY,
    UPLOAD_DIRECTORY
)

for directory in [
    HLS_PATH,
    RECORDINGS_PATH,
    UPLOAD_PATH
]:

    if not os.path.exists(directory):

        os.makedirs(directory)

        