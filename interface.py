import tkinter as tk
from database import check_command
from voice_engine import say

class Virtualassisstant(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MLRIT CHATBOT")
        self.geometry("800x600")
        self.configure(bg="white")

        print("Hi. I'm MLRIT CHATBOT. What can I do for you?")
        say("Hi. I am M L R I T CHATBOT. What can I do for you?", self)

        self.label = tk.Label(self, text="MLRIT ChatBot", font=("Times New Roman", 48, "bold"), bg="white", fg='blue')
        self.label.pack(pady=30)

        self.label = tk.Label(self, text="What can I do for you?", font=("Arial", 16), bg="white", fg="black")
        self.label.pack()

        self.entry = tk.Entry(self, font=("Arial", 12), bg="white", fg="black", width=40)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.on_submit)

        self.search_area = tk.Text(self, font=("Arial", 12), bg="white", fg="black", width=60, height=8)
        self.search_area.pack(pady=20)

        self.button = tk.Button(self, text="Submit", font=("Arial", 12, "bold", "italic"), bg="black", fg="white", width=20, height=2, command=self.on_submit)
        self.button.pack(pady=20)

    def on_submit(self, event=None):
        text1 = self.entry.get().lower()
        check_command(text1, self)

    def ex(self, text1, command):
        self.search_area.insert(tk.END, "YOU: " + command + "\n")
        self.search_area.insert(tk.END, "MLRIT: " + text1 + "\n")
        self.entry.delete(0, tk.END)

if __name__ == '__main__':
    app = Virtualassisstant()
    app.mainloop()
