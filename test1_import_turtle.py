import turtle #sử dụng hàm lớp để vẽ đồ họa
colors = ['red','purple','blue','green','green','yellow','orange']
    #chọn màu
t = turtle.Pen()
#đối tượng này dùng để vẽ
t.speed(0)
#tốc độ vẽ
turtle.bgcolor('black')
#màu nền của turtle
for x in range (360):#vòng lặp 360 như hình tròn
	t.pencolor(colors[x%6])#đặt màu x chia cho 6 là 360/6 là sẽ vẽ 6 màu
	t.width(x/100+1)#độ dày của đường vẽ
	t.forward(x)#di chuyển t về phía trước nên là đường vẽ sẽ càng ngày càng dài
	t.left(59)#đi qua bên trái 1 góc 59 độ ngược chiều kim đồng hồ
    #?có cách nào để đẹp hơn không nhỉ