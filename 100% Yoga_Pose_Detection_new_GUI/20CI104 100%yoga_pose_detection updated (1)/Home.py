import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
#import xgboost as xgb
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Yoga Pose Detection Using Machine Learning")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('WhatsApp Image 5.jpeg')
image2 = image2.resize((1400, 740), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#
label_l1 = tk.Label(root, text="YOGA POSE DETECTION SYSTEM",font=("Times New Roman", 35, 'bold'),
                    background="seashell", fg="purple", width=50, height=1, bd=4)
label_l1.place(x=0, y=0)




# def help():
#     frame_alpr = tk.LabelFrame(root, text=" --Yoga Poses-- ", width=900, height=550, bd=5, font=('times', 14, ' bold '),bg="SeaGreen1")
#     frame_alpr.grid(row=0, column=0, sticky='nw')
#     frame_alpr.place(x=450, y=120)

#     image3 = Image.open('v.jpg')
#     image3 = image3.resize((200, 200), Image.ANTIALIAS)
#     background_image3 = ImageTk.PhotoImage(image3)
#     background_label3 = tk.Label(root, image=background_image3,text="Vajrasan",compound='bottom')
#     background_label3.image = background_image3
#     background_label3.place(x=500, y=150)
    
#     image4 = Image.open('sar.jpg')
#     image4 = image4.resize((200, 200), Image.ANTIALIAS)
#     background_image4 = ImageTk.PhotoImage(image4)
#     background_label4 = tk.Label(root, image=background_image4,text="Sarvangasan",compound='bottom')
#     background_label4.image = background_image4
#     background_label4.place(x=700, y=150)
    
    
#     image5 = Image.open('shi.jpg')
#     image5 = image5.resize((200, 200), Image.ANTIALIAS)
#     background_image5 = ImageTk.PhotoImage(image5)
#     background_label5 = tk.Label(root, image=background_image5,text="Shirsasan",compound='bottom')
#     background_label5.image = background_image5
#     background_label5.place(x=900, y=150)
    
#     image6 = Image.open('ch.jpg')
#     image6 = image6.resize((200, 200), Image.ANTIALIAS)
#     background_image6 = ImageTk.PhotoImage(image6)
#     background_label6 = tk.Label(root, image=background_image6,text="Chakrasan",compound='bottom')
#     background_label6.image = background_image6
#     background_label6.place(x=1100, y=150)
    
#     image7 = Image.open('s.jpg')
#     image7 = image7.resize((200, 200), Image.ANTIALIAS)
#     background_image7 = ImageTk.PhotoImage(image7)
#     background_label7 = tk.Label(root, image=background_image7,text="Shavasan",compound='bottom')
#     background_label7.image = background_image7
#     background_label7.place(x=500, y=400)
    
#     image8 = Image.open('g.jpg')
#     image8 = image8.resize((200, 200), Image.ANTIALIAS)
#     background_image8 = ImageTk.PhotoImage(image8)
#     background_label8 = tk.Label(root, image=background_image8,text="Gomukhaasan",compound='bottom')
#     background_label8.image = background_image8
#     background_label8.place(x=700, y=400)
    
#     image9 = Image.open('b.jpg')
#     image9 = image9.resize((200, 200), Image.ANTIALIAS)
#     background_image9 = ImageTk.PhotoImage(image9)
#     background_label9 = tk.Label(root, image=background_image9,text="Bhadraasan",compound='bottom')
#     background_label9.image = background_image9
#     background_label9.place(x=900, y=400)
    
#     image10 = Image.open('d.jpg')
#     image10 = image10.resize((200, 200), Image.ANTIALIAS)
#     background_image10 = ImageTk.PhotoImage(image3)
#     background_label10 = tk.Label(root, image=background_image10,text="Dhanurasan",compound='bottom')
#     background_label10.image = background_image10
#     background_label10.place(x=1100, y=400)
    
  
    ########################### use upper img ++++++++++++++++++++++++++++++++++

    
    #################################################################################
    
    
def help():
    frame_alpr = tk.LabelFrame(root, text=" --Yoga Poses-- ", width=760, height=600, bd=5, font=('times', 14, ' bold '),bg="Seashell")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=435, y=80)

    image3 = Image.open('WhatsApp Image 6.jpeg')
    image3 = image3.resize((705, 545), Image.ANTIALIAS)
    background_image3 = ImageTk.PhotoImage(image3)
    background_label3 = tk.Label(root, image=background_image3,compound='bottom')
    background_label3.image = background_image3
    background_label3.place(x=457, y=108)
    
# def XGBOOST():
#         xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1,
#                         max_depth = 5, alpha = 10, n_estimators = 10)
#         xg_reg.fit(X_train,y_train)
#         rmse = np.sqrt(mean_squared_error(y_test, preds))
#         params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1,
#                         'max_depth': 5, 'alpha': 10}

#         cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3,
#                             num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)
#         print("RMSE: %f" % (rmse))


#         preds = xg_reg.predict(X_test)
#         rmse = np.sqrt(mean_squared_error(y_test, preds))
#         print("RMSE: %f" % (rmse))
#         RMSE: 10.569356
#         params = {"objective":"reg:linear",'colsample_bytree': 0.3,'learning_rate': 0.1,
#                         'max_depth': 5, 'alpha': 10}

#         cv_results = xgb.cv(dtrain=data_dmatrix, params=params, nfold=3,
#                             num_boost_round=50,early_stopping_rounds=10,metrics="rmse", as_pandas=True, seed=123)
#         cv_results.head()

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def action():
   
    from subprocess import call
    call(["python","GUI_Master.py"])
    

#################################################################################################################
def window():
    root.destroy()



button3 = tk.Button(root, text="Recognize Yoga Pose",command=action, bd=4, width=16, height=1, bg="purple", fg="white",font=('times', 19, ' bold '))
button3.place(x=40, y=220)

# button3 = tk.Button(root, text="",command=XGBOOST, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
# button3.place(x=100, y=220)

button3 = tk.Button(root, text="Help",command=help, width=16, height=1, bg="purple", bd=4, fg="white",font=('times', 19, ' bold '))
button3.place(x=40, y=320)

exit = tk.Button(root, text="Exit", command=window, width=8, height=1, font=('times', 19, ' bold '), bg="red",fg="white", bd=4)
exit.place(x=80, y=420)

root.mainloop()