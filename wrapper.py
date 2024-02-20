import subprocess


input_array = ["1","2","3","4","5"]


subprocess.run(["clang", "ccprog.c", "-o", "ccprog"])
process = subprocess.run(["./ccprog"] + input_array, capture_output = True, text = True)
output_variable = process.stdout.strip()

print("C program output:")
print(output_variable)

#HASKELL
subprocess.run(['ghc', 'haskell5.hs'])
process = subprocess.run(['./haskell5'] + [str(x) for x in input_array], text=True, capture_output=True)
output_variable = process.stdout.strip()

print("Haskell program output:")
print(output_variable)

#PROLOG
input_array = ["1","2","3","4","5"]
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'prologcode.pl'], input=prolog_input,
capture_output=True, text=True)
output_result = result.stdout.strip()

print("Prolog program output:")
print(output_result)


#MATLAB

matlab_executable = '/Applications/MATLAB_R2023b.app'


# Load the matlab code
with open('matlabcode1.m', 'r') as file:
 matlabcode = file.read()

# Set up MATLAB environment
Matlab_process = subprocess.Popen([matlab_executable, '-nodisplay', '-nosplash', '-nodesktop'],
stdin=subprocess.PIPE, text=True)

# Send MATLAB script to the MATLAB process
matlab_process.communicate(input=matlabcode)

print("Running MATLAB CODE 1")

matlab_executable = '/Applications/MATLAB_R2023b.app'
matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlabcode1.m'); pause(1);"]
, capture_output=True)

with open('input.txt', 'r') as file:
 line = file.readline()
 input_array = [int(value) for value in line.split()]
 input_array = [str(value) for value in input_array]



with open('c_output.txt', 'w') as f:
 f.write(output_variable)



