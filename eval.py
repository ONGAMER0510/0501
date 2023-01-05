from tensorflow import keras
model= keras.models.load_model('.\saved\Colab.h5')
import os,cv2
import numpy as np
import threading
import time
from threading import Thread
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import time
from playsound import playsound 
img=1
fight=0
non_fight=0
cap=cv2.VideoCapture()
stat=False
cap.open('rtsp://admin:sgis12345@172.16.16.132:554/Streaming/Channels/1601/')
success,frame=cap.read()
framesstat=[]
final=0
# def play():
#     playsound('./Alert.wav')
# sound=threading.Thread(target=play).start()
def GUI():
    global SS
    path="./LOGO.png"
    image = Image.open(path)
    Logo = image.resize((85,85))
    window = tk.Tk()
    window.geometry("850x400+550+325")
    window.title("NAZAR AI")
    INFO='''
    The young generation is the future of the world and its development. If they learn and practice\n\n skills like good communication skills, global citizenship and non violence, then the world is\n\n guaranteed to become a better place. But on the flip side if these same students during their\n\n learning years learn to be physically violent, to bully people then the effects of this will be\n\n adverse in the future both for the students themselves and the world too. This is why the students\n\n must be monitored in school to ensure that they do not pick up these bad habits. To do\n\n this, many schools install a CCTV monitoring system in their school. But it is not possible\n\n for a person to sit and monitor all of them for each and every minute. This is why, to ensure\n\n reduction of physical violence in schools, and ultimately in the outside world too, our project is\n\n the perfect solution.
    '''
    window.iconbitmap('./favicon.ico')
    frame = tk.Frame(master=window, width=500, height=75, bg="#1e1c22")
    img=ImageTk.PhotoImage(Logo)
    frame1 = tk.Frame(master=window, width=850, height=75,bg="#fff")
    BUTFIT1=tk.Frame(master=frame1, width=850, height=40,bg="#cecece",borderwidth='2')
    SS=btn = tk.Button(BUTFIT1, text = '       Start       ',font=("Ciutadella Rounded Dark",12), bd = '1',padx=30,pady=15)
    def start():
        global SS
        global stat
        if stat==False:
            stat=True
            SS.config(text="        Stop        ")
        else:
            stat=False
            SS.config(text="       Start       ")
    def openf():
        path=r"C:\Science\Violence-Detection-in-Videos-master\fight_frames"
        os.path.realpath(path)
        os.startfile(path)
    Title = tk.Label(frame, text="  NAZAR AI", fg="white",bg="#102233",font=("Ciutadella Rounded Light",30),image=img,compound=tk.LEFT)
    frame1 = tk.Frame(master=window, width=850, height=75,bg="#adefd1")
    BUTFIT1=tk.Frame(master=frame1, width=850, height=40,bg="#cecece",borderwidth='2')
    SS=btn = tk.Button(BUTFIT1, text = '       Start       ',font=("Ciutadella Rounded Dark",12), bd = '1',padx=30,pady=15,command=start,bg='#00203f', fg='#adefd1')
    # frame2 = tk.Frame(master=window, width=850, height=75,bg="#cecece")
    BUTFIT2=tk.Frame(master=frame1, width=850, height=75,bg="#cecece",borderwidth='2')
    FL=btn = tk.Button(BUTFIT2, text = 'Abnormal Images', bd = '1',font=("Ciutadella Rounded Dark",12),padx=30,pady=15,command=openf,bg='#00203f',fg='#adefd1')
    frame3 = tk.Frame(master=window, width=850, height=75,bg="#cecece")
    FL3 = tk.Label(frame3, text='What is our project about', padx=10,font=("Ciutadella Rounded Dark",24),bg="#ff4747",fg="white")
    FL2 = tk.Label(frame3, text=INFO,font=("Ciutadella Rounded Dark",17),bg="#ff4747",fg="white")
    frame7 = tk.Frame(master=window, width=500, height=25, bg="#1e1c22")
    datetimeshow = tk.Label(frame7, text="", bg="#1e1c22",fg="white",padx=10)
    def timef():
        while True:
            try:
                timenow = datetime.now().strftime(r'%d/%m/%Y   %H:%M')
                datetimeshow.config(text=timenow)
                time.sleep(10)
            except RuntimeError:
                pass
    threadtime = Thread(target = timef)
    threadtime.start()
    frame.pack(fill=tk.X, side=tk.TOP)
    datetimeshow.pack(fill=tk.X, side=tk.RIGHT)
    frame7.pack(fill=tk.X, side=tk.BOTTOM)
    Title.pack(fill=tk.X, side=tk.TOP)
    frame1.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)
    # SS1.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    BUTFIT1.pack(side=tk.TOP, expand=True)
    SS.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    # frame2.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    # FL1.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    BUTFIT2.pack(side=tk.TOP, expand=True)
    FL.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    frame3.pack(fill=tk.BOTH,side=tk.LEFT, expand=True)
    FL3.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    FL2.pack(fill=tk.BOTH,side=tk.TOP, expand=True)
    # LOOMS.pack(fill=tk.X, side=tk.TOP)
    # Loom1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # RPM.pack(fill=tk.X, side=tk.TOP)
    # RPM1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # Reading.pack(fill=tk.X, side=tk.TOP)
    # Reading1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # Weft.pack(fill=tk.X, side=tk.TOP)
    # Weft1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # frame5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # Warp.pack(fill=tk.X, side=tk.TOP)
    # Warp1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # frame6.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # Efficiency.pack(fill=tk.X, side=tk.TOP)
    # Efficiency1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    window.mainloop()

def identifier():
    global success,frame,stat
    success,frame=cap.read()
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    non_fight=1
    fight=1
    size = (frame_width, frame_height)
    result = cv2.VideoWriter('./fight_frames/fights.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    while success:
        if stat:
            # success,frame=cap.read()
            global status
            global final
            status=''
            image=frame
            if image is not None:
                #x = image.img_to_array(img)
                x = np.expand_dims(image, axis=0)
                images = np.vstack([x])
                classes = model.predict(images, batch_size=10)
                print(classes)
                framesstat.append(classes[0][0])
                if classes[0][0]>0.5:
                    status="Fighting"
                    cv2.imwrite(f"./fight_frames/Fight{fight}.jpg", image)
                    # result.write(image
                    fight+=1
                else:
                    # cv2.imwrite(f"./fight_frames/nonFight{non_fight}.jpg", image)
                    status="No fight"
                    non_fight+=1
                #   print("frame"+" "+status)
                #   img+=1     
                if (len(framesstat)<4):
                    status=status
                else:
                    final=(sum(framesstat[-3:]))/3
                    # print(final)
                    if final>=0.5:
                        status="Fighting"
                        # send('./fight_frames/fights.avi')
                    else:
                        status="No Fight"
                # final=classes[0][0]
                # print(status)
                # os.remove(r'C:\Science\Violence-Detection-in-Videos-master\fight_frames\fights.avi')
            else:
                pass
def show():
    global status
    global final
    global success,frame
    global stat
    # success,frame=cap.read()
    while success:
        if stat:
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (50, 50)
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            # success,frame=cap.read()
            if final>0.75:
                status="Fighting"
            else:
                status="Not Fighting"
            frame = cv2.putText(frame,f"Fight :{final}", org, font, fontScale, color, thickness, cv2.LINE_AA)
            frame = cv2.putText(frame,f"Nonfight :{1-final}", (50,80), font, fontScale, color, thickness, cv2.LINE_AA)
            frame = cv2.putText(frame,status, (50,115), font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.namedWindow("Violence Detection", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Violence Detection", 1366, 768)
            cv2.imshow("Violence Detection",frame)
            cv2.waitKey(1)
        else:
            pass
def loop():
    while True:
        if stat:
            global success,frame
            success,frame=cap.read()
        else:
            pass
Identifier = threading.Thread(target=identifier)
Showing = threading.Thread(target=show)
SendE = threading.Thread(target=loop)
Gui = threading.Thread(target=GUI)
# Identifier=identifier(success,frame)
Identifier.start()
Showing.start()
SendE.start()
Gui.start()
Identifier.join()
Showing.join()
SendE.join()
Gui.join()
cap.release()