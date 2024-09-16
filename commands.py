import os
import urllib.request

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

def align_all(target=None):
    """Align all objects in this session to the provided `target`"""

    objects = cmd.get_names("objects")
    if not target:
        target = objects[0]
    assert target in objects, f"Specified target \"{target}\" not found in list of {len(objects)} objects" 

    objects.remove(target)

    for obj in objects:
        cmd.super(obj, target)

    cmd.orient()


def download_alphafold_pdb(name, folder, verbose=False):
    """Download an AlphaFold prediction. Assumes a valid identifier 
    and will throw an error if it gets a 404 from the server"""

    name = name.upper() 
    url = f"https://alphafold.ebi.ac.uk/files/AF-{name}-F1-model_v4.pdb"
    filename = f"AF-{name}-F1-model_v4.pdb"
    filepath = os.path.join(folder, filename)
    if verbose:
        print(f"{filepath=} {url=}")
    os.makedirs(folder, exist_ok=True)
    urllib.request.urlretrieve(url, filepath)
    if verbose:
        print(f"File downloaded to: {filepath}")
    return filepath


def fetch_af(uniprot_accession):
    """Attempt to fetch an AlphaFold prediction for your UniProt accession"""

    downloads_path = cmd.get("fetch_path")
    print(f"Downloading AlphaFold structure of {uniprot_accession} to {downloads_path=}")

    try:
        path = download_alphafold_pdb(uniprot_accession, downloads_path)
        cmd.load(path, format="pdb")
    except Exception as e:
        print("Something went wrong when fetching:")
        print(e)


#################################
# Declare them for use in PyMOL #
#################################

cmd.extend("align_all", align_all)
cmd.extend("aa", align_all)  # short form 
cmd.extend("fetch_af", fetch_af)
