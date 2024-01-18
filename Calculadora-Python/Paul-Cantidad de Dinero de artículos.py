# Name: Calculator in Pyhton
# Created by: PaulSMRT
# Date: 18/01/2024

evolver = {
    'Cannon': 22,
    'Ice_Wall': 150,
    'Shuriken': 24,
    'Data_Leech': 20,
    'Protector': 270,
    'Blaster': 70,
    'Worms': 80,
    'Access': 116,
    'Shocker': 120,
    'Battering_Ram': 100,
    'Kraken': 60,
    'Wraith': 700,
    'Maniac': 200,
    'Portal': 640
} # Data base of programs and their correspond cost

compiling = '' # It serves to enter the programs to compile
program_library = [] # It serves to save the program you compile
individual_inversion = 0 # It serves to add the multiplied amounts in the Program Library
total = 0 # It serves to return the total of b coins inverted

quantity_program = [] # Servs to save product of programs multiplicates by own cost

print(evolver.items())

while compiling.lower() != "done": # while variable 'compiling' is diferent of 'done':
    if compiling:
        program_library.append(compiling) # Added 'key' of 'evolver' in program library list

        individual_inversion += evolver.get(compiling) # Return a value of  'evolver' and move them to this variable

        quantity = int(input("¿How many programs of this type will you compile? ")) # The user enters the amount of the type of programs he will compile  

        quantity_program.append(f'Total of {quantity} {compiling} for {evolver[compiling]} B-Coins is {evolver[compiling] * quantity}') # Add operation to list

        total += evolver.get(compiling) * quantity # This will multiply the type of program at its own cost.
    
    # Periodically (the print) you will print the previous result in parts.
    compiling = input("Enter the programs that you want to compile(to finish:done) ")

print(f"""
--------------------------------
              
Your buy was:
      
{"\n".join(quantity_program)}

--------------------------------
Total:{total} B-Coins""")