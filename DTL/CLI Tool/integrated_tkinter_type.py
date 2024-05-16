import tkinter as tk
from rich import print as rprint
import subprocess
from PyInquirer import prompt

class TerminalApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Terminal")

        self.output_text = tk.Text(self, height=20, width=50)
        self.output_text.pack()

        self.input_entry = tk.Entry(self, width=50)
        self.input_entry.pack()

        self.execute_button = tk.Button(self, text="Execute", command=self.handle_input)
        self.execute_button.pack()

    def handle_input(self):
        user_input = self.input_entry.get()
        self.input_entry.delete(0, tk.END)
        self.output_text.insert(tk.END, '>> ' + user_input + '\n')

        # Execute command based on user input
        if user_input == "hi":
            self.say_hi()
        elif user_input == "hello":
            self.say_hello()
        elif user_input == "list":
            self.list_files()
        elif user_input == "new_dir":
            self.create_new_directory()
        elif user_input == "custom_new_dir":
            self.create_custom_directory()
        elif user_input == "new_file":
            self.create_new_file()
        else:
            rprint("[red]Command not recognized[/red]")

        # Keep focus on the input entry
        self.input_entry.focus_set()

    def say_hi(self):
        # self.output_text.insert(tk.END, "[red bold]Hi[/red bold] [yellow]World[/yellow]\n")
        self.output_text.insert(tk.END, "Hi User\n")

    def say_hello(self):
        self.output_text.insert(tk.END, "Hello User\n")

    def list_files(self):
        output = subprocess.check_output('dir', shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        self.output_text.insert(tk.END, output)

    def create_new_directory(self):
        subprocess.run('mkdir new_dir', shell=True)
        self.output_text.insert(tk.END, "New directory created successfully!\n")

    def create_custom_directory(self):
        usernames = ["Abhay", "Naman", "Shreya", "Shruti"]

        # Create a dialog box to select username
        dialog = tk.Toplevel(self)
        dialog.title("Select Username")

        selected_username = tk.StringVar(dialog)
        selected_username.set(usernames[0])  # Set default value

        label = tk.Label(dialog, text="Select any one username: ")
        label.pack()

        username_dropdown = tk.OptionMenu(dialog, selected_username, *usernames)
        username_dropdown.pack()

        confirm_button = tk.Button(dialog, text="Confirm", command=lambda: self.confirm_custom_directory(selected_username.get(), dialog))
        confirm_button.pack()

    def confirm_custom_directory(self, selected_username, dialog):
        dialog.destroy()  # Close the dialog window

        self.output_text.insert(tk.END, "=============================================\n")
        self.output_text.insert(tk.END, "Enter folder name :\n")
        folder_name = self.input_entry.get()

        subprocess.run(f"mkdir {folder_name}_created_by_{selected_username}", shell=True)
        self.output_text.insert(tk.END, "New directory created successfully!\n")


    def create_new_file(self):
        file_types = ["README.md", "requirements.txt", "setup.sh"]

        # Create a dialog box to select file type
        dialog = tk.Toplevel(self)
        dialog.title("Select File Type")

        selected_file_type = tk.StringVar(dialog)
        selected_file_type.set(file_types[0])  # Set default value

        label = tk.Label(dialog, text="Select the file you want to create: ")
        label.pack()

        file_type_dropdown = tk.OptionMenu(dialog, selected_file_type, *file_types)
        file_type_dropdown.pack()

        confirm_button = tk.Button(dialog, text="Confirm", command=lambda: self.show_content_dialog(selected_file_type.get(), dialog))
        confirm_button.pack()

    def show_content_dialog(self, selected_file_type, parent):
        parent.destroy()  # Close the file type selection dialog

        content_dialog = tk.Toplevel(self)
        content_dialog.title("Enter Content")

        label = tk.Label(content_dialog, text=f"Enter content for {selected_file_type}:")
        label.pack()

        content_entry = tk.Text(content_dialog, height=10, width=50)
        content_entry.pack()

        confirm_button = tk.Button(content_dialog, text="Confirm", command=lambda: self.save_file(selected_file_type, content_entry.get("1.0", "end-1c"), content_dialog))
        confirm_button.pack()

    def save_file(self, selected_file_type, content, dialog):
        dialog.destroy()  # Close the content entry dialog

        with open(selected_file_type, 'w') as file:
            file.write(content)

        self.output_text.insert(tk.END, "=============================================\n")
        self.output_text.insert(tk.END, "New file created successfully!\n")



def main():
    app = TerminalApp()
    app.mainloop()

if __name__ == "__main__":
    main()
