import multiprocessing
import cv2

def show_video(video_path):
    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        cv2.imshow('video', frame)
        cv2.waitKey(1)

if __name__ == '__main__':
    process1 = multiprocessing.Process(target=show_video, args=["input/Despicable Me 2 (2013).mp4"])
    process2 = multiprocessing.Process(target=show_video, args=["input/Scrat's Continental Crack-Up Part 2.mp4"])
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print('Done!')
