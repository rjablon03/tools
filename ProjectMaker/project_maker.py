import os


class ProjectMaker:

    def __init__(self):
        self.base_path = (
            r"C:\Users\ryan.m.jablonski"
            r"\OneDrive - Koops, Inc"
            r"\Desktop\Projects"
        )

    def create_project(self, client_name, project_name):
        path = os.path.join(
            self.base_path,
            client_name,
            project_name
        )

        try:
            os.makedirs(path)

            os.mkdir(os.path.join(path, "Resources"))
            os.mkdir(os.path.join(path, "Code"))
            os.mkdir(os.path.join(path, "Backups"))

            return True, f"Project '{project_name}' created successfully."

        except FileExistsError:
            return False, (
                f"One or more directories in '{path}' already exist."
            )

        except PermissionError:
            return False, (
                f"Permission denied: Unable to create '{path}'."
            )

        except Exception as e:
            return False, f"An error occurred: {e}"

    def create_client(self, client_name):
        path = os.path.join(
            self.base_path,
            client_name
        )

        try:
            os.mkdir(path)

            return True, f"Client '{client_name}' created successfully."

        except FileExistsError:
            return False, (
                f"The client folder '{client_name}' already exists."
            )

        except PermissionError:
            return False, (
                f"Permission denied: Unable to create '{path}'."
            )

        except Exception as e:
            return False, f"An error occurred: {e}"