import cv2
import numpy as np


def load_video_frames(video_path):
    video = cv2.VideoCapture(video_path)
    frames = []
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)
    video.release()
    return frames

def load_frame_timestamps(timestamp_file):
    with open(timestamp_file, 'r') as file:
        timestamps = [float(line.strip()) for line in file]
    return timestamps

def synchronize_video(frames, timestamps, target_fps):
    num_frames = len(frames)
    num_timestamps = len(timestamps)
    frame_duration = 1 / target_fps

    synchronized_frames = []
    frame_index = 0

    for timestamp in timestamps:
        while frame_index < num_frames and frame_index * frame_duration < timestamp:
            synchronized_frames.append(frames[frame_index])
            frame_index += 1

    return synchronized_frames


video_path = 'data/1.avi'
timestamp_file = 'data/1.txt'
target_fps = 5

frames = load_video_frames(video_path)
timestamps = load_frame_timestamps(timestamp_file)

synchronized_frames = synchronize_video(frames, timestamps, target_fps)

