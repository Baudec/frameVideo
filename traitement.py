def break_into_frame(path):
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        success,image = vidcap.read()
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
        count += 1