import tkinter as tk
from tkinter import messagebox

from project_maker import ProjectMaker


class ProjectMakerApp:

    def __init__(self, root):
        self.root = root

        self.root.title("Project Maker")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.project_maker = ProjectMaker()

        self.build_main_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ==================================================
    # Main Menu
    # ==================================================

    def build_main_window(self):
        self.clear_window()

        title = tk.Label(
            self.root,
            text="Project Maker",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=(30, 20))

        subtitle = tk.Label(
            self.root,
            text="What would you like to create?"
        )
        subtitle.pack(pady=(0, 20))

        project_button = tk.Button(
            self.root,
            text="Create Project",
            width=25,
            command=self.show_project_dialog
        )
        project_button.pack(pady=5)

        client_button = tk.Button(
            self.root,
            text="Create Client",
            width=25,
            command=self.show_client_dialog
        )
        client_button.pack(pady=5)

    # ==================================================
    # Project Dialog
    # ==================================================

    def show_project_dialog(self, client_name=None):
        self.clear_window()

        title = tk.Label(
            self.root,
            text="Create Project",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(20, 20))

        # ------------------------------
        # Client Name
        # ------------------------------

        client_frame = tk.Frame(self.root)
        client_frame.pack(pady=5)

        tk.Label(
            client_frame,
            text="Client Name:",
            width=15,
            anchor="e"
        ).pack(side="left", padx=5)

        client_entry = tk.Entry(
            client_frame,
            width=30
        )
        client_entry.pack(side="left")

        # If we're creating the first project
        # for a newly created client, fill in
        # the client name automatically.
        if client_name:
            client_entry.insert(0, client_name)
            client_entry.config(state="disabled")

        # ------------------------------
        # Project Name
        # ------------------------------

        project_frame = tk.Frame(self.root)
        project_frame.pack(pady=5)

        tk.Label(
            project_frame,
            text="Project Name:",
            width=15,
            anchor="e"
        ).pack(side="left", padx=5)

        project_entry = tk.Entry(
            project_frame,
            width=30
        )
        project_entry.pack(side="left")

        # ------------------------------
        # Buttons
        # ------------------------------

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=25)

        back_button = tk.Button(
            button_frame,
            text="Back",
            width=10,
            command=self.build_main_window
        )
        back_button.pack(side="left", padx=5)

        create_button = tk.Button(
            button_frame,
            text="Create",
            width=10,
            command=lambda: self.create_project(
                client_entry,
                project_entry
            )
        )
        create_button.pack(side="left", padx=5)

        project_entry.focus()

    def create_project(self, client_entry, project_entry):
        # Get client name
        #
        # Even when the entry is disabled,
        # .get() still works.
        client_name = client_entry.get().strip()
        project_name = project_entry.get().strip()

        # ------------------------------
        # Validate input
        # ------------------------------

        if not client_name:
            messagebox.showerror(
                "Missing Client",
                "Please enter a client name."
            )
            return

        if not project_name:
            messagebox.showerror(
                "Missing Project",
                "Please enter a project name."
            )
            return

        # ------------------------------
        # Create project
        # ------------------------------

        success, message = self.project_maker.create_project(
            client_name,
            project_name
        )

        # ------------------------------
        # Handle result
        # ------------------------------

        if success:
            # No success dialog.
            # Simply return to the main menu.
            self.build_main_window()

        else:
            # Only show a dialog if something went wrong.
            messagebox.showerror(
                "Error",
                message
            )

    # ==================================================
    # Client Dialog
    # ==================================================

    def show_client_dialog(self):
        self.clear_window()

        title = tk.Label(
            self.root,
            text="Create Client",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=(25, 20))

        # ------------------------------
        # Client Name
        # ------------------------------

        client_frame = tk.Frame(self.root)
        client_frame.pack(pady=10)

        tk.Label(
            client_frame,
            text="Client Name:",
            width=15,
            anchor="e"
        ).pack(side="left", padx=5)

        client_entry = tk.Entry(
            client_frame,
            width=30
        )
        client_entry.pack(side="left")

        # ------------------------------
        # Buttons
        # ------------------------------

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=30)

        back_button = tk.Button(
            button_frame,
            text="Back",
            width=10,
            command=self.build_main_window
        )
        back_button.pack(side="left", padx=5)

        create_button = tk.Button(
            button_frame,
            text="Create",
            width=10,
            command=lambda: self.create_client(client_entry)
        )
        create_button.pack(side="left", padx=5)

        client_entry.focus()

    def create_client(self, client_entry):
        client_name = client_entry.get().strip()

        # ------------------------------
        # Validate input
        # ------------------------------

        if not client_name:
            messagebox.showerror(
                "Missing Client",
                "Please enter a client name."
            )
            return

        # ------------------------------
        # Create client
        # ------------------------------

        success, message = self.project_maker.create_client(
            client_name
        )

        # ------------------------------
        # Handle result
        # ------------------------------

        if success:
            # No success dialog.
            #
            # Immediately move to the project
            # creation screen for this client.
            self.show_project_dialog(client_name)

        else:
            # Only show a dialog if something went wrong.
            messagebox.showerror(
                "Error",
                message
            )


# ======================================================
# Start Application
# ======================================================

if __name__ == "__main__":
    root = tk.Tk()

    app = ProjectMakerApp(root)

    root.mainloop()