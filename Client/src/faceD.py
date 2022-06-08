import cv2
import numpy as np


class faceDetect:
# חותכת את התמונה מסביב לפנים המזוהות ומחזירה אותה
    def cropPic(self, original_image, y, h, x, w):
        cropped_image = original_image[y:y + h, x:x + w]
        cv2.imshow("cropped", cropped_image)
        return cropped_image
# בדיקת גבולות כדי שהפנים לא יחתכו
    def CheckLimts(self,column, row, width, height):
        r = row - 50
        if r < 0:
            r = 0
        h = height + 100
        if h > 480:
            h = 480
        c = column - 50
        if c < 0:
            c = 0
        w = width + 50
        if w > 640:
            w = 640
        return r, h, c,w

#מתחיל את הצילום כוידאו וכשאר נלחץ מקש כלשהו מוצולמת תמונה
    def startCapture(self):
        cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
        # Load the classifier and create a cascade object for face detection

        face_cascade = cv2.CascadeClassifier(r'..\face_detect_models\haarcascade_frontalface_alt2.xml')

        while True:
            # video
            ret, frame = cap.read()

            frame1 = cv2.resize(frame, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
            # original_image = frame1
            original_image = frame
            grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
            # מספר הפרצופים שזיהה בפורמט של column, row, width, height לכל פרצוף
            detected_faces = face_cascade.detectMultiScale(grayscale_image)
            # עובר על המערך ,רץ כמספר הפרצופים השקיימים שזיהה
            for (column, row, width, height) in detected_faces:
                # BGR - blue green red
                # Enlarge the detect boundaries to get the complete face.
                # Check limits are within 640x480
                r, h, c, w = self.CheckLimts(column, row, width, height)
                cropImgae = self.cropPic(original_image, r, h, c, w)
                #cv2.rectangle(original_image, (column, row), (column + width, row + height), (255, 0, 0), 3)

            cv2.imshow('Image', original_image)
            c = cv2.waitKey(1)
            if c != -1:
                break


        if len(detected_faces) :
            cv2.imwrite(r"../pic_tmp_client/face.jpg", cropImgae)
        cap.release()
        cv2.destroyAllWindows()
        return len(detected_faces)

# class FaceRec():