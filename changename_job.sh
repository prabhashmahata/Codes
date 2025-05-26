#!/bin/bash

X=1
while [ $X -le 890 ]
do
    cd TRAJ$X/ || { echo "Directory TRAJ$X not found"; exit 1; }
    if [[ -f "batch_job.sh" ]]; then
        # Construct the new job name
        new_job_name="NX_tr$X"
        # Update the job name inside batch_job.sh
        sed -i "s/^#SBATCH --job-name=.*/#SBATCH --job-name=$new_job_name/" "batch_job.sh"
    else
        echo "batch_job.sh not found in TRAJ$X"
    fi
    cd ../
    X=$((X+1))
done

