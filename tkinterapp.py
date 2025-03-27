import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser, simpledialog

class TkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Full Tkinter App")
        self.root.geometry("600x400")
        
        # Creating Menu Bar
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        
        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Edit Menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Change Color", command=self.change_color)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        
        # Label
        self.label = tk.Label(root, text="This is a Tkinter App", font=("Arial", 14))
        self.label.pack(pady=10)
        
        # Button
        self.button = tk.Button(root, text="Click Me", command=self.show_message)
        self.button.pack(pady=5)
        
        # Entry
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)
        
        # Text Widget
        self.text_widget = tk.Text(root, height=5, width=40)
        self.text_widget.pack(pady=5)
        
        # Checkbutton
        self.check_var = tk.IntVar()
        self.check_button = tk.Checkbutton(root, text="Check Me", variable=self.check_var)
        self.check_button.pack(pady=5)
        
        # Radio Buttons
        self.radio_var = tk.StringVar(value="Option 1")
        self.radio1 = tk.Radiobutton(root, text="Option 1", variable=self.radio_var, value="Option 1")
        self.radio2 = tk.Radiobutton(root, text="Option 2", variable=self.radio_var, value="Option 2")
        self.radio1.pack()
        self.radio2.pack()
        
        # Scale
        self.scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale.pack()
        
        # Listbox
        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=5)
        self.listbox.insert(1, "Item 1")
        self.listbox.insert(2, "Item 2")
        self.listbox.insert(3, "Item 3")
        
        # Combobox
        from tkinter import ttk
        self.combobox = ttk.Combobox(root, values=["Select", "Option 1", "Option 2"])
        self.combobox.current(0)
        self.combobox.pack()
        
        # Canvas
        self.canvas = tk.Canvas(root, width=200, height=100, bg="lightgray")
        self.canvas.pack()
        self.canvas.create_rectangle(20, 20, 100, 50, fill="blue")
        
        # Message Box
        self.message_button = tk.Button(root, text="Show Info", command=self.show_info)
        self.message_button.pack()
    
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("File Opened", f"Opened: {file_path}")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            messagebox.showinfo("File Saved", f"Saved: {file_path}")
    
    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.root.configure(bg=color)
    
    def show_message(self):
        messagebox.showinfo("Message", f"You entered: {self.entry.get()}")
    
    def show_info(self):
        user_input = simpledialog.askstring("Input", "Enter something:")
        if user_input:
            messagebox.showinfo("User Input", f"You entered: {user_input}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()
