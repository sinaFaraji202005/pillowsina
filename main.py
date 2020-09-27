import settings
import functions
user_exit = False
state = "main_menu"
while not user_exit:
    if state in settings.MENUS_VALID_STATES:
        if state == "main_menu":
            functions.main_menu()
        elif state == "insert":
            functions.insert_menu()
        elif state == "export":
            functions.export_menu()
        elif state == "edit":
            functions.edit_menu()
    else:
        functions.state_error()


