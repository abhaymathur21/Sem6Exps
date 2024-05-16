import tkinter as tk
import subprocess

class TerminalApp:
    def __init__(self, master):
        self.master = master
        master.title("Terminal")

        self.output_text = tk.Text(master, height=20, width=50)
        self.output_text.pack()

        self.input_entry = tk.Entry(master, width=50)
        self.input_entry.pack()
        self.input_entry.bind('<Return>', self.handle_input)

    def handle_input(self, event):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.output_text.insert(tk.END, '>> ' + user_input + '\n')

        # Execute the command entered by the user
        try:
            output = subprocess.check_output(user_input, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            self.output_text.insert(tk.END, output)
        except subprocess.CalledProcessError as e:
            self.output_text.insert(tk.END, f"Error: {e.output}")

        # Scroll to the end of the output
        self.output_text.see(tk.END)

def main():
    root = tk.Tk()
    app = TerminalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
