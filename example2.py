#!/usr/bin/env python3

import hipo_cppyy
import sys
import matplotlib.pyplot as plt

#############
# if on ifarm, some backends may not work with X11 forwarding, so use AGG instead and just write to a file;
# if you want to see plots interactively and locally, comment out these lines and call `plt.show()` at the end
import matplotlib
matplotlib.use('Agg')
#############

# include the header files that you need
hipo_cppyy.include('hipo4/reader.h')
# then import the bound namespaces (must be after including the headers)
from cppyy.gbl import hipo
# now you may use the C++ hipo code as if it were Python!

# parse arguments
if(len(sys.argv)==1):
    print(f'USAGE: {__file__} [HIPO FILE] [NUM_EVENTS (default = all events)]')
    exit(2)
inFile    = sys.argv[1]
numEvents = int(sys.argv[2]) if len(sys.argv)>2 else 0

# open the HIPO file
reader = hipo.reader(inFile)
banks  = reader.getBanks(["REC::Particle", "RUN::config"]);

# define arrays to hold data for histograms
pids = [ 211, -211, 11, -11, 2212 ]
momentum_arr = {}
for pid in pids:
    momentum_arr[pid] = { 'px': [], 'py': [], 'pz': [] }

# event loop
iEvent = 0
while(reader.next(banks) and (numEvents==0 or iEvent < numEvents)):
    print(f'read event {iEvent} ==========================')
    iEvent += 1

    # read the banks; must be same order as in `reader.getBanks([...])` call
    particleBank, configBank = banks

    # get the event number
    evnum = configBank.getInt('event', 0)

    # select 2 pi+s and an electron only
    num_pions = 0
    num_electrons = 0
    for row in range(particleBank.getRows()):
        if(particleBank.getInt('pid', row) == 211):
            num_pions += 1
        if(particleBank.getInt('pid', row) == 11):
            num_electrons += 1
    if(num_pions!=2 or num_electrons!=1):
        continue

    # loop through the particle bank; if it's a pi+, add its momentum to `momentum_arr`
    for row in range(particleBank.getRows()):
        for pid, arr0 in momentum_arr.items():
            if(particleBank.getInt('pid', row) == pid):
                for var, arr in arr0.items():
                    momentum = particleBank.getFloat(var, row)
                    print(f'{pid} -- {var}: {momentum}')
                    arr.append(momentum)

# plot the momenta
n_bins = 50
pt_range = [-2, 2]
pz_range = [0, 12]
fig, axs = plt.subplots(1, 2, tight_layout=True)
axs[0].hist2d(
        momentum_arr[211]['px'],
        momentum_arr[211]['py'],
        bins  = (n_bins, n_bins),
        range = [pt_range, pt_range],
        )
axs[1].hist(
        momentum_arr[211]['pz'],
        bins  = n_bins,
        range = pz_range,
        )
axs[0].set_xlabel('$p_x$')
axs[0].set_ylabel('$p_y$')
axs[1].set_xlabel('$p_z$')
for ax in axs:
    ax.set_title("$\pi^+$ Momentum Distribution")
plt.savefig('plot.png')
print('wrote plots to plot.png')
# plt.show() # uncomment this if you want to see the plots interactively
