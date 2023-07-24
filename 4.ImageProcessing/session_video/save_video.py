import cv2

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter("sajjad.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    _, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY)

    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

writer.release()
