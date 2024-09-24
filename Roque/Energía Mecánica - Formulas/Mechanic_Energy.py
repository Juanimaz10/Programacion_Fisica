from Constants import *

"Mechanic_Energy"
mass = float(input(mass_data))
velocity = float(input(velocity_data))
height = float(input(height_data)) 
Kinetic_Energy = 1/2*mass*(velocity)**2
Potencial_Energy = mass*gravity*height
Mechanic_Energy = Kinetic_Energy + Potencial_Energy
print(mechanic_energy_result,Mechanic_Energy)

"conservatives_forces"

Conservatives_forces = 0*Mechanic_Energy

"No_conservatives_forces"

Delta = delta_data
No_Conservatives_forces = Delta*Mechanic_Energy

"Work between No_conservatives_forces"

mass = float(input(mass_data))
velocity = float(input(velocity_data))
height = float(input(height_data)) 
Kinetic_Energy = 1/2*mass*(velocity)**2
Potencial_Energy = mass*gravity*height
Primary_Mechanic_Energy = Kinetic_Energy + Potencial_Energy
print(primary_mechanic_energy_result,Primary_Mechanic_Energy)

mass = float(input(mass_data))
velocity = float(input(velocity_data))
height = float(input(height_data)) 
Kinetic_Energy = 1/2*mass*(velocity)**2
Potencial_Energy = mass*gravity*height
Final_Mechanic_Energy = Kinetic_Energy + Potencial_Energy
print(final_mechanic_energy_result,Final_Mechanic_Energy)



Work_between_No_conservatives_forces = Primary_Mechanic_Energy - Final_Mechanic_Energy
print(work_between_No_conservatives_forces_result,Work_between_No_conservatives_forces)






    


