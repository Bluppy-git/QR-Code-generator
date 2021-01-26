import tkinter
import qrcode

def generate(event):
    bs = bs_in.get()
    bo = bo_in.get()
    text = data.get()
    name = save.get()
    qr = qrcode.QRCode(box_size = bs, border = bo)
    qr.add_data(text)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(name + ".png")


top = tkinter.Tk()
top.title("QR-Code generator")

data = tkinter.Entry(top)
bs_in = tkinter.Entry(top)
bo_in = tkinter.Entry(top)
save = tkinter.Entry(top)


data.grid(row=1, columnspan=5)
bs_in.grid(row=3, columnspan=5)
bo_in.grid(row=5, columnspan=5)
save.grid(row=7, columnspan=5)

#Tasten Symbol und Koordinate

QR_Code_text = tkinter.Label(top, text = " Enter Text for the QR Code ")
QR_Code_text.grid(row=0,column=0)

QR_Code_size = tkinter.Label(top,text=" Enter the size of QR Code ")
QR_Code_size.grid(row=2,column=0)

QR_Code_border = tkinter.Label(top,text=" Enter the border of QR Code ")
QR_Code_border.grid(row=4,column=0)

QR_Code_name = tkinter.Label(top,text=" Enter the name of QR Code ")
QR_Code_name.grid(row=6,column=0)

QR_Code_name = tkinter.Label(top,text=" ")
QR_Code_name.grid(row=9,column=0)

generate_QR_Code = tkinter.Button(top,text=" generate QR Code ")
generate_QR_Code.grid(row=10,column=0)

QR_Code_name = tkinter.Label(top,text=" You find the generated QR-Code in the same folder as this QR-Code generator ")
QR_Code_name.grid(row=11,column=0)


#Auszuführender Befehl beim drücken der Taste

generate_QR_Code.bind("<Button-1>", generate)


top.mainloop()