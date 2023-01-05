from email.mime import image
import time
from threading import Thread
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
path=r"C:\Users\admin\Desktop\Ojas\Creations\Images\Jeetex Logo.png"
image = Image.open(path)
Logo = image.resize((85,85))
window = tk.Tk()
window.geometry("850x400+550+325")
window.title("Jeetex Loom Viewer")
INFO='''
The young generation is the future of the world and its development. If they learn and practice\n\n skills like good communication skills, global citizenship and non violence, then the world is\n\n guaranteed to become a better place. But on the flip side if these same students during their\n\n learning years learn to be physically violent, to bully people then the effects of this will be\n\n adverse in the future both for the students themselves and the world too. This is why the students\n\n must be monitored in school to ensure that they do not pick up these bad habits. To do\n\n this, many schools install a CCTV monitoring system in their school. But it is not possible\n\n for a person to sit and monitor all of them for each and every minute. This is why, to ensure\n\n reduction of physical violence in schools, and ultimately in the outside world too, our project is\n\n the perfect solution.
'''
window.iconbitmap(r'F:\Ojas SSD\Ojas\Python\Arduino Serial\Jeetex icon.ico')
frame = tk.Frame(master=window, width=500, height=75, bg="#1e1c22")
img=ImageTk.PhotoImage(Logo)
Title = tk.Label(frame, text="  NAZAR AI", fg="white",bg="#1e1c22",font=("Ciutadella Rounded Light",30),image=img,compound=tk.LEFT)
frame1 = tk.Frame(master=window, width=850, height=75,bg="#fff")
BUTFIT1=tk.Frame(master=frame1, width=850, height=40,bg="#cecece",borderwidth='2')
SS=btn = tk.Button(BUTFIT1, text = '       Start       ',font=("Ciutadella Rounded Dark",12), bd = '1',padx=30,pady=15,command=start)
# frame2 = tk.Frame(master=window, width=850, height=75,bg="#cecece")
BUTFIT2=tk.Frame(master=frame1, width=850, height=75,bg="#cecece",borderwidth='2')
FL=btn = tk.Button(BUTFIT2, text = 'Abnormal Images', bd = '1',font=("Ciutadella Rounded Dark",12),padx=30,pady=15,command=openf)
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
