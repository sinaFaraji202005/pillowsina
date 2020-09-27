import settings
def change_state(new_state):
    pass

def main_menu():
    print(
    """
    Please Choose:
    1. Insert new pic
    2. Export New File
    3. Edit
    4. Exit
    """)

def insert_menu():
    pass

def export_menu():
    pass

def edit_menu():
    pass

def state_error():
    def is_int(n):
        try:
            int(n)
            return True
        except ValueError:
            return False

