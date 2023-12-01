import maya.cmds as cmds

def select_adjacent_faces(selected_faces, select_count, deselect_count):
    # Deselect all faces first
    cmds.select(clear=True)

    # Select adjacent faces based on the provided counts
    for i, face in enumerate(selected_faces):
        if i % (select_count + deselect_count) < select_count:
            cmds.select(face, add=True)

def prompt_for_values():
    select_count = cmds.promptDialog(
        title='Input Values',
        message='Enter value for select_count:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel'
    )

    if select_count == 'OK':
        select_count = int(cmds.promptDialog(query=True, text=True))
        deselect_count = cmds.promptDialog(
            title='Input Values',
            message='Enter value for deselect_count:',
            button=['OK', 'Cancel'],
            defaultButton='OK',
            cancelButton='Cancel',
            dismissString='Cancel'
        )
        
        if deselect_count == 'OK':
            deselect_count = int(cmds.promptDialog(query=True, text=True))
            return select_count, deselect_count

    return None, None

# Prompt the user for values
prompt_result = prompt_for_values()

if prompt_result[0] is not None and prompt_result[1] is not None:
    select_count, deselect_count = prompt_result

    # Get the currently selected faces
    selected_faces = cmds.ls(selection=True, flatten=True)

    if not selected_faces:
        cmds.warning("Please select faces before running the script.")
    else:
        # Check if the selection is a valid loop of faces
        if not cmds.polyEvaluate(selected_faces, faceComponent=True):
            cmds.warning("Please select a loop of faces.")
        else:
            # Run the function with the specified variables
            select_adjacent_faces(selected_faces, select_count, deselect_count)
