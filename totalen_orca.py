import csv

def extract_energy_if_job_finished_normally(filename, output_csv):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Check if ORCA terminated normally
    job_status_finish = any("ORCA TERMINATED NORMALLY" in line for line in lines)

    if not job_status_finish:
        print("ORCA job does not terminated normally")
        return

    # Search for the last 'Total energy:' line
    energy_Eh = None
    for line in reversed(lines):
        if "FINAL SINGLE POINT ENERGY" in line:
            parts = line.split()
            #if parts[-1] == "eV":
            #    try:
            #        energy_ev = float(parts[-2])
            energy_Eh = float(parts[-1])
            #        break
            #    except ValueError:
            #        continue

    if energy_Eh is None:
        print("FINAL SINGLE POINT ENERGY not found")
        return

    # Write to CSV
    with open(output_csv, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
#        writer.writerow(["SCC Converged", "Total Energy (eV)"])
#        writer.writerow(["Yes", energy_ev])
#        writer.writerow(["SCC Converged", "Total Energy (eV)"])
        writer.writerow([ energy_Eh])

#    print(f"Energy written to '{output_csv}': {energy_ev} eV")

# Usage
input_file = "auH.log"
output_file = "totalenergy.csv"
extract_energy_if_job_finished_normally(input_file, output_file)

