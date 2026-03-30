#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create chemical diagrams."""

def draw_chem_diagram(chem_name, mode="show", outdir="."):

    if not os.path.isdir(outdir):
        os.mkdir(outdir)
    
    smiles = cirpy.resolve(chem_name, 'smiles')
    
    if not isinstance(smiles, str):
        raise RuntimeError(
            f"\"{chem_name}\" is not a known chemical identifier to the Chemical "
            f"Identifier Resolver (http://cactus.nci.nih.gov/chemical/structure)"
        )
    
    if mode=="show":
        pika.draw_smiles(smiles)    
    elif mode=="svg":
        pika.svg_from_smiles(smiles, f"{outdir}/{chem_name}.svg")
    elif mode=="png":
        pika.png_from_smiles(smiles, f"{outdir}/{chem_name}.png")
    else: 
        raise ValueError(f"\"{mode}\" is not a known mode for draw_chem_diagram")