import cv2

def blur_faces(image_path, output_path):
    is_video = image_path.endswith(('.mp4', '.avi'))
    if is_video:
        blur_faces_video(image_path, output_path)
    else:
        blur_faces_image(image_path, output_path)

def blur_faces_image(image_path, output_path):
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]
        face = cv2.GaussianBlur(face, (99, 99), 30)
        image[y:y+h, x:x+w] = face
    cv2.imwrite(output_path, image)

def blur_faces_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.GaussianBlur(face, (99, 99), 30)
            frame[y:y+h, x:x+w] = face
        out.write(frame)
    cap.release()
    out.release()
