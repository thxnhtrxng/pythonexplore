import tkinter as tk
import time 
import math

WIDTH = 400
HEIGHT = 400 #đây là kích thước cửa sổ  

root = tk.Tk()#Dòng này tạo một đối tượng gốc của tkinter, là cửa sổ chính của ứng dụng.
root.title("Analog Clock")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")#tạo ra bảng vẽ rồi gắn vào root
canvas.pack()#dòng này đặt canvas vào cửa sổ chính để nó hiện trên root

def update_clock():#cập nhật đồng hồ mỗi khi thời gian thay đổi
    canvas.delete("all")            #vẽ lại , lấy thời gian cứ thế lặp đi lặp lại là đồng hồ sẽ chạy
    now = time.localtime()
    hour = now.tm_hour % 12
    minute = now.tm_min
    second = now.tm_sec

    #vẽ khung đồng hồ 
    canvas.create_oval(2, 2, WIDTH, HEIGHT, outline="black",width=2)
    for i in range(12):
        angle = i * math.pi/6 - math.pi/2
        x = WIDTH/2 +0.7 * WIDTH/2 * math.cos(angle)
        y = HEIGHT/2 + 0.7 * WIDTH/2 * math.sin(angle)
        if i == 0:
            canvas.create_text(x,y-10,text=str(i+12),font=("Helvetica",12))
        else:
            canvas.create_text(x,y,text=str(i),font=("Helvetica",12))
    for i in range(60):
        angle = i * math.pi/30 - math.pi/2
        x1 = WIDTH/2 +0.8 * WIDTH/2 * math.cos(angle)
        y1 = HEIGHT/2 + 0.8 * HEIGHT/2 * math.sin(angle)
        x2 = WIDTH/2 +0.9 * WIDTH/2 * math.cos(angle)
        y2 = HEIGHT/2 + 0.9 * HEIGHT/2 * math.sin(angle)
        if i % 5 == 0:
            canvas.create_line(x1,y1,x2,y2,fill="black",width=3)
        else:
            canvas.create_line(x1,y1,x2,y2,fill="black",width=1)
            #vẽ kim giờ
    hour_angle = (hour + minute/60)*math.pi/6 - math.pi/2
    hour_x = WIDTH/2 + 0.5 * WIDTH/2 * math.cos(hour_angle)
    hour_y = HEIGHT/2 + 0.5 * HEIGHT/2 * math.sin(hour_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,hour_x,hour_y,fill="black",width=6)
            #vẽ kim phút
    minute_angle = (minute + second/60)*math.pi/30 - math.pi/2
    minute_x = WIDTH/2 + 0.7 * WIDTH/2 * math.cos(minute_angle)
    minute_y = HEIGHT/2 + 0.7 * HEIGHT/2 * math.sin(minute_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,minute_x,minute_y,fill="black",width=4)
            #vẽ kim giây
    second_angle = second * math.pi/30 - math.pi/2
    second_x = WIDTH/2 + 0.6 * WIDTH/2 * math.cos(second_angle)
    second_y = HEIGHT/2 + 0.6 * WIDTH/2 * math.sin(second_angle)
    canvas.create_line(WIDTH/2,HEIGHT/2,second_x,second_y,fill="red",width=2)
    canvas.after(1000, update_clock) #lặp lại mỗi 1000ms là 1s để update thời gian

update_clock()  #Gọi hàm một lần để khởi đầu quá trình cập nhật đồng hồ.
root.mainloop() #duy trì cửa sổ chính cho đến khi người dùng đóng
