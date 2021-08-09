from threading import Thread
import cv2 as cv

class WebCamVideoWriter(object):
    def __init__(self, src='jahy.mp4'):
        self.capture = cv.VideoCapture(src)

        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        self.codec = cv.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv.VideoWriter('output.avi', self.codec, 30.0, (self.frame_width, self.frame_height))

        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        if self.status:
            self.frame = cv.flip(self.frame, 90)
            #self.frame = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
            cv.imshow('frame', self.frame)

        if cv.waitKey(1) == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv.destroyAllWindows()
            exit()

    def save_frame(self):
        self.output_video.write(self.frame)

if __name__ == '__main__':
    webcam = WebCamVideoWriter()
    while True:
        try:
            webcam.show_frame()
            webcam.save_frame()
        except AttributeError:
            pass