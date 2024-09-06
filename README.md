# PyMOL PowerPack 

Power up your PyMOL 🧬 with this PowerPack of commands 🚀 

**Background.** As someone who designs proteins, I have my favorite ways of doing things, especially in PyMOL. This PowerPack adds the features to PyMOL that make my work easy. 


## Installation 

There are two steps. First, obtain the Powerpack from the releases page or using Git 

```
git clone https://github.com/dacarlin/pymol-powerpack.git
```

Second, add this line to your `.pymolrc` file:

```
run path/to/pymol-powerpack/commands.py
```

You can find your `.pymolrc` in your home folder, or open it from within PyMOL. 🎉


## Available commands 

- `align_all(target=None)`. Align all structures in the session to the provided `target` using structural alignment. If no target is provided, align everything to the first structure in the list of structures 
- `fetch_af(uniprot_accession)`. Using the provided UniProt accession, attempt to fetch an AlphaFold prediction for the sequence. (Does no computation, just a `GET` request to the AlphaFold database server.)