from pymol import cmd 

# This file defines commands that can be used in interactive
# PyMOL sessions. To use this file, run it in PyMOL 
#
# run path/to/commands.py 
#
# After doing so, the commands will be available to run. For 
# example, this file defines a command called "align_all". 
# After you run this file with PyMOL, you will be able to use 
# the "align_all" command in the PyMOL window. 

#######################
# Define the commands #
#######################

def align_all(target):
    """Align all objects in this session to the provided `target`"""

    objects = cmd.get_names("objects")
    assert target in objects, f"Specified target \"{target}\" not found in list of {len(objects)} objects" 

    objects.remove(target)

    for obj in objects:
        cmd.super(obj, target)


#################################
# Declare them for use in PyMOL #
#################################

cmd.extend("align_all", align_all)
cmd.extend("aa", align_all)  # short form 
