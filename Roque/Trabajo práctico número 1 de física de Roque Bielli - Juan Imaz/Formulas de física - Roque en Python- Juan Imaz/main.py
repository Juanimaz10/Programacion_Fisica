from constants import * 

option = int(input(Beginning_Menu))

if option == 1:

    print(Energies_Types)

elif option == 2:
        
        def Ionization_energy( wavelength = 0 ):
            CTE_PLANCK = 6.626e-34 
            VELOCITY_LIGHT = 3e8
            ionization_energy = CTE_PLANCK * VELOCITY_LIGHT / wavelength
            return ionization_energy

        wavelength = float(input(Wavelength_Number))
        ionization_energy_equation = Ionization_energy(wavelength)
        print(Ionization_Energy,ionization_energy_equation, Joules) 

elif option == 3:

    def Zero_point_energy( frequency = 0 ): 
        H_BAR = 1.0545718e-34
        omega = 2 * 3.141592653589793 * frequency
        zero_point_energy = 0.5 * H_BAR * omega
        return zero_point_energy
    
    frequency = float(input(Oscilator_Number))
    zero_point_energy_equation = Zero_point_energy(frequency)
    print(Zero_Point_Energy , zero_point_energy_equation, Joules)

elif option == 4:

    def Desintegration_energy( initial_mass = 0, final_mass= 0 ): 
        VELOCITY_LIGHT = 3e8
        delta_mass = initial_mass - final_mass
        desintegration_energy = delta_mass * VELOCITY_LIGHT**2
        return desintegration_energy
    
    initial_mass = float(input(Initial_Mass_Number))
    final_mass = float(input(Final_Mass_Number))
    desintegration_energy_equation = Desintegration_energy(initial_mass, final_mass)
    print(Desintegration_Energy , desintegration_energy_equation, Joules)

elif option == 5:

    def Electric_energy(voltage = 0, current = 0, time = 0): 
        electric_energy = voltage * current * time
        return electric_energy
    
    voltage = float(input(Voltage_Number))
    current = float(input(Current_Number))
    time = float(input(Time_Number))
    electric_energy_equation = Electric_energy(voltage, current, time)
    print(Electric_Energy ,electric_energy_equation, Joules)

elif option == 6:

    def Electric_potential_energy(q1 = 0, q2 = 0, distance = 0): 
        KE = 8.99e9
        electric_potential_energy = ( KE * ( ( q1 * q2 ) / distance ) )
        return electric_potential_energy
    
    q1 = float(input(First_Charge_Number))
    q2 = float(input(Second_Charge_Number))
    distance = float(input(Distance_Between_Charges))
    electric_potential_energy_equation = Electric_potential_energy(q1, q2, distance)
    print(Electric_Potential_Energy, electric_potential_energy_equation, Joules)

elif option == 7:

    def Kinetic_energy(mass = 0, velocity = 0):
        kinetic_energy = 0.5 * mass * (velocity**2)
        return kinetic_energy
    
    mass = float(input(Mass_Number))
    velocity = float(input(Velocity_Number))
    kinetic_energy_equation = Kinetic_energy(mass, velocity)
    print(Kinetic_Energy, kinetic_energy_equation,Joules)

elif option == 8:

    def Chemical_energy( delta_mass = 0 ): 

        VELOCITY_LIGHT = 3e8

        energy_from_mass = delta_mass * VELOCITY_LIGHT**2
        return energy_from_mass

    delta_mass = float(input("Introduce la diferencia de masa (kg): "))
    energy_equation= Chemical_energy(delta_mass)
    print(Chemical_Energy, energy_equation, Joules)

elif option == 9:

    def Potential_energy(mass = 0, height = 0, gravity=9.8):

        potential_energy = mass * gravity * height
        return potential_energy

    mass = float(input(Mass_Number))
    height = float(input(Height_Number))
    potential_energy_equation = Potential_energy(mass, height)
    print(Potential_Energy, potential_energy_equation ,Joules)

else:
    print(Another_Option)