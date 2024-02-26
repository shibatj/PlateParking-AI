from tkinter import Tk, Frame, Button, Label, Entry, filedialog
from PIL import Image, ImageTk

def openFile(button):
    global buttons_positions
    buttons_positions = {}
    for btn in buttons:
        buttons_positions[btn] = (btn.grid_info(), btn.cget('text'))

    filepath = filedialog.askopenfilename(initialdir=".",  
                                          title="Open File",
                                          filetypes=(("Image files", "*.jpg *.jpeg *.png"),
                                                     ("Text files", "*.txt"),
                                                     ("All files", "*.*")))
    if filepath:
        if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):  
            original_image = Image.open(filepath)
            resized_image = original_image.resize((75, 75), Image.BICUBIC)
            button.image = ImageTk.PhotoImage(resized_image)
            button.config(image=button.image, text="", bg="black")
        else:  
            pass
        button.clicked = True
        for btn, (position, text) in buttons_positions.items():
            btn.grid(**position)
            btn.config(text=text)

def search_data():
    search_query = entry.get().lower()
    if not search_query:
        print("กรุณาป้อนคำค้นหา")
        return
    
    entry.delete(0, 'end')
    print("Search Query:", search_query)
    
    found = False
    
    for i, btn in enumerate(buttons):
        button_text = btn['text'].lower()
        if search_query in button_text:
            found = True
            btn.config(bg="yellow")
            print("ข้อความ", search_query, "พบอยู่ในช่องจอดรถ A", i + 1)
    
    if found:
        print("ค้นหาสำเร็จ")
    else:
        print("ไม่พบข้อความที่ค้นหา")

def create_button(container, row, col, text):
    button = Button(container, text=text, bg="#00FF00", font=("Arial", 14))  
    button.grid(row=row, column=col, padx=10, pady=25)  
    button.clicked = False
    button.config(command=lambda b=button: openFile(b))
    return button

def reset_all_buttons_text():
    for i, button in enumerate(buttons, start=1):
        button.config(image='', text=f"A{i:02d}", bg="#00FF00", state="normal")
        button.image = None  

main_window = Tk()
main_window.title("Parking Lot")
main_window.geometry("800x400")

parking_frame = Frame(main_window)
parking_frame.grid(row=0, column=0, padx=10, pady=10)

search_frame = Frame(main_window)
search_frame.grid(row=1, column=0, padx=10, pady=10)

buttons_text_row1 = ["A01", "A02", "A03", "A04", "A05"]
buttons_text_row2 = ["A06", "A07", "A08", "A09", "A10"]

buttons = []

for row, buttons_text in enumerate([buttons_text_row1, buttons_text_row2], start=1):
    for col, text in enumerate(buttons_text, start=0):
        button = create_button(parking_frame, row, col, text)
        buttons.append(button)

search_label = Label(search_frame, text="ค้นหาป้ายทะเบียน", font=("Arial", 16))
search_label.grid(row=0, column=0, padx=10, pady=10)

entry = Entry(search_frame, width=30, font=("Arial", 16))
entry.grid(row=0, column=1, padx=10, pady=10)

search_button = Button(search_frame, text="ค้นหา", command=search_data, font=("Arial", 14), bg="#FFFFCC", fg="black")
search_button.grid(row=0, column=2, padx=10, pady=10)

reset_button = Button(search_frame, text="รีเซ็ต", command=reset_all_buttons_text, font=("Arial", 14), bg="#FF3333", fg="black")
reset_button.grid(row=0, column=3, padx=10, pady=10)


main_window.mainloop()