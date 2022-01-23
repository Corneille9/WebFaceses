import cv2
import numpy as np
import face_recognition
import os


class FaceRecognition:
    def __init__(self, path='ImagesBasic'):
        self.path = path
        self.images = []
        self.classNames = []
        self.myList = os.listdir(path)

    def build_classNames(self):
        for cl in self.myList:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])

    def find_encodings(self, images):
        encodeList = []
        for image in images:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # TODO do try cach here
            encode = face_recognition.face_encodings(image)[0]
            encodeList.append(encode)
        return encodeList

    def detect_face(self, file='ImagesBasic/corneille1.jpg'):
        self.build_classNames()
        encodeListKnown = self.find_encodings(self.images)
        print('Encoding Complete')

        detected_faces = []
        # success, img = cap.read()
        img = face_recognition.load_image_file(file)
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        detect = False
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print("facedir", faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                detected_faces.append({"UploadFileName": file, "detected": 'True', "name": self.classNames[matchIndex].upper(), "facedir": round(faceDis[0], 2)})
                detect = True
        if not detect:
            detected_faces.append(({"UploadFileName": file, "detected": 'False'}))
        return detected_faces
