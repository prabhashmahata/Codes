# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 16:51:34 2025

@author: prabh
"""
# Import the requite library
import numpy as np
import csv
 
# read the input geometry
with open(file="geom.xyz",mode="r") as f:
    lines=f.readlines()
natoms=int(lines[0])
comment=lines[1].strip()
#comment2=lines[1]
#print('com1=',comment1)
#print('com2=',comment2)

# read the atomic symbol and corresponding coordinate
atoms=[]
for line in lines[2:]:
     #print(f"{line}")
#     print(f"{line[1]}")
     columns=line.split()
     #print(columns[0],columns[1],columns[2],columns[3])
     symb=columns[0]
    # print(type(symb),symb)
     coords=np.array([float(columns[1]),float(columns[2]),float(columns[3])])
     #print(type(coords),coords)
     atoms.append((symb,coords))
#print(atoms[0])
#print(atoms)

#Find the H1 and H2 
H1_symb, H1_coords=atoms[6]
H2_symb,H2_coords=atoms[7]
#print(H1_symb,H1_coords)
#print(H2_symb, H2_coords)

#Find the midpoint and Unit Vector
midpoint=(H1_coords+H2_coords)/2
#print(midpoint)
vecH1H2=H2_coords-H1_coords
#print(vecH1H2)
unit_vec=vecH1H2/np.linalg.norm(vecH1H2)
#print(unit_vec)

#create the distance range and new H2 coords. H1 will be fixed but the H2 will move 
#move and other Au coord will be fixed

interdis_HH=np.arange(0.7, 10, 0.2)
#print(interdis_HH)
counter=1  # Initializing the counter
with open("hhdistance.csv" , mode='w',newline='') as csvfile:
    csv_out=csv.writer(csvfile)
    csv_out.writerow(["H-H distacne"])
    for indx, dis in enumerate(interdis_HH,1):
        new_H2=midpoint+dis*unit_vec
        #print(new_H2)
        
        #new atoms preparations
        new_atoms=atoms[:7]+[(H2_symb,new_H2)]
    
    
        #Write the new geometry in .xyz format
        new_fname=f"geom{indx}.xyz"
        with open(new_fname,'w') as file_out:
            file_out.write(f"{natoms}\n")
            file_out.write(f"H-H distance:{dis:.2f} Å \n")
            for symb,coord in new_atoms:
                file_out.write(f"{symb:<2}  {coord[0]: .8f}  {coord[1]: .8f}  {coord[2]: .8f}\n")
        csv_out.writerow([f"{dis:.2f}"])
        counter +=1
        print(f"new_fname{file_out}")
