# This is simple python file which checks the SCC CONVERGENCE in detailed.out file of dftb+ followed by collected the results in another file and file
# file name is totalen.py
import csv

def extract_energy_if_scc_converged(filename, output_csv):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Check if SCC converged
    scc_converged = any("SCC converged" in line for line in lines)

    if not scc_converged:
        print("SCC did not converge.")
        return

    # Search for the last 'Total energy:' line
    energy_ev = None
    for line in reversed(lines):
        if "Total energy:" in line:
            parts = line.split()
            if parts[-1] == "eV":
                try:
                    energy_ev = float(parts[-2])
                    break
                except ValueError:
                    continue

    if energy_ev is None:
        print("Total energy line not found.")
        return

    # Write to CSV
    with open(output_csv, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
#        writer.writerow(["SCC Converged", "Total Energy (eV)"])
#        writer.writerow(["Yes", energy_ev])
#        writer.writerow(["SCC Converged", "Total Energy (eV)"])
        writer.writerow([ energy_ev])

#    print(f"Energy written to '{output_csv}': {energy_ev} eV")

# Usage
input_file = "detailed.out"
output_file = "totalenergy.csv"
extract_energy_if_scc_converged(input_file, output_file)

