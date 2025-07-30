# Zc calculation for bacterial Thi4 proteins

This repository contains code and protein sequences for calculating the Zc (average oxidation number of carbon value) calculation for 2,365 bacterial Thi4 protein sequences in the paper **"Mining bacterial (meta)genomes for enzymes active in aerobic, mesophilic conditions"** (submitted to *Analytical Biochemistry*). 

The Zc calculation is based on the methodology described in:
**Dick, J. M., & Shock, E. L. (2011). Calculation of the relative chemical stabilities of proteins as a function of temperature and redox chemistry in a hot spring. PLoS One, 6(8), e22782. https://doi.org/10.1371/journal.pone.0022782**

## Description

The carbon oxidation state (Zc) is a measure of the average oxidation state of carbon atoms in proteins. The Zc value is calculated using the formula:


$\overline{Z_C} = \frac{Z - n_H + 2(n_O + n_S) + 3n_N}{n_C}$


where $n_C, n_H, n_N, n_O$ and $ n_S$ are the numbers of the respective subscripted elements in the chemical formula. 


## Requirements

- Python 3.6+
- BioPython
- pandas

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/thi4-zc-calculator.git
cd thi4-zc-calculator
```

2. Install required packages:
```bash
pip install biopython pandas
```

Or using conda:
```bash
conda install -c bioconda biopython pandas
```

## Usage

### Command Line Interface

```bash
python thi4_zc_calculator.py <input_fasta_file> <output_csv_file>
```

### Example

```bash
python thi4_zc_calculator.py data/Bacterial_catalytic_THI4.fasta output/Zc.csv
```

### Input Format

The input file should be in FASTA format with protein sequences:
```
>sequence_id_1
MKLAVLGAAGIGSTLAQILAAQGAKVIAFERDPELKKLKEAYGVQVTTD...
>sequence_id_2
MKLAILLGAAGIGSTLAQLLSAYGAKVICFERDPELKKLKEAYGLQVTTD...
```

### Output Format

The output CSV file contains two columns:
- `GenBank`: Sequence identifier from the FASTA header
- `Zc`: Calculated carbon oxidation state value

```csv
GenBank,Zc
sequence_id_1,-0.234567
sequence_id_2,-0.198765
```

## Algorithm Details

The tool uses predefined values for:
- **Carbon oxidation states (Pox)**: Mean carbon oxidation values for each of the 20 standard amino acids
- **Carbon atom counts (Cox)**: Number of carbon atoms in each amino acid side chain

Invalid sequences or amino acids not in the standard 20 will result in NaN values in the output.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or issues, please open an issue on GitHub or contact juannanzhou@ufl.edu.