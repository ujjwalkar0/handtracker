import cv2
import mediapipe as mp
import time

class HandTracking:
    def show_fps(self):
        self.pTime = 0
        self.cTime = 0
        
    def take_video(self,path):
        self.cap = cv2.VideoCapture(path)
        
    def detect_hand(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def others(self):
        while True:
                success, img = self.cap.read()
                img = cv2.flip(img,1)
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                results = self.hands.process(imgRGB)
                #print(results.multi_hand_landmarks) 
                
                if results.multi_hand_landmarks:
                    for handlms in results.multi_hand_landmarks:
                        for id_,lm in enumerate(handlms.landmark):
                            #print(id_,lm)
                            
                            h,w,c = img.shape
                            cx, cy = int(lm.x*w), int(lm.y*h)
                            
                            print(id_,cx,cy)

                            if id_ == 4:
                                cv2.circle(img,(cx,cy-50),25,(255,0,255), cv2.FILLED)


                        self.mpDraw.draw_landmarks(img,handlms, self.mpHands.HAND_CONNECTIONS)
                
                try:
                    self.cTime = time.time()
                    fps = 1/(self.cTime - self.pTime)
                    self.pTime = self.cTime

                    cv2.putText(img, str(fps), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255), 3)
                
                except:
                    pass

                cv2.imshow("Image", img)
                cv2.waitKey(1)


