# This is code for a smoking cessation paper with Dr. Garcia and Dr. Dench

# as always

print("Hello World! :)")

# First, use pip install pymdptoolbox[LP] to install https://github.com/sawcordwell/pymdptoolbox

import mdptoolbox, mdptoolbox.example
P, R = mdptoolbox.example.rand(10, 3)
pi = mdptoolbox.mdp.PolicyIteration(P, R, 0.9)
pi.run()

print(pi)
