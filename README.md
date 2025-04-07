# SMILES to Molecular Structure Converter  
A Python tool that converts SMILES codes into 2D molecular visualizations using RDKit. 

##  Features  
* **Input**: Accepts any valid [SMILES notation](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)  
* **Output**: Generates publication-ready 2D structures
* ## Example Output
![Aspirin Structure](/Screenshot2.png)
*Generated from SMILES: `CC(=O)OC1=CC=CC=C1C(=O)O`*

## Run
```bash
git clone https://github.com/Intisarakkila/smilesto2dstructure
cd smilesto2dstructure
pip install -r requirements.txt
python app.py
