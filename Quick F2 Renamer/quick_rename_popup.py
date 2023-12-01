import maya.cmds as cmds

def show_dialog():
    # Prompt the user to enter some text
    dialog = cmds.window(title='Quick Rename by Nasho3D')
    cmds.columnLayout(adjustableColumn=True)

    # Prompt the user to enter some text
    result = cmds.promptDialog(
        title='Quick Rename by Nasho3D',
        button=['Rename', 'Cancel'],
        defaultButton='Rename',
        cancelButton='Cancel',
        dismissString='Cancel'
    )

    # If the user clicks "Rename," retrieve the entered text and display it in the dialog box
    if result == 'Rename':
        user_text = cmds.promptDialog(query=True, text=True)

        sl_obj = cmds.ls(sl=1)
        cmds.rename(sl_obj[0], user_text)

# Call the function to show the dialog box
show_dialog()