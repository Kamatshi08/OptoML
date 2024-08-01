import os, sys
import os.path
import numpy as np
import argparse

def parse_bin(frame, board):
    print(f"Parsing frame {frame}, board {board}")
    samples = None
    
    # Open files for writing
    rx0_i = open(f"frames/rx{0 + (board * 4)}_i_{frame}.py", "w")
    rx1_i = open(f"frames/rx{1 + (board * 4)}_i_{frame}.py", "w")
    rx2_i = open(f"frames/rx{2 + (board * 4)}_i_{frame}.py", "w")
    rx3_i = open(f"frames/rx{3 + (board * 4)}_i_{frame}.py", "w")

    rx0_q = open(f"frames/rx{0 + (board * 4)}_q_{frame}.py", "w")
    rx1_q = open(f"frames/rx{1 + (board * 4)}_q_{frame}.py", "w")
    rx2_q = open(f"frames/rx{2 + (board * 4)}_q_{frame}.py", "w")
    rx3_q = open(f"frames/rx{3 + (board * 4)}_q_{frame}.py", "w")

    # Initialize files with NumPy array definitions
    rx0_q.write("import numpy as np\nrx0_real = np.array([")
    rx0_i.write("import numpy as np\nrx0_imag = np.array([")
    rx1_q.write("import numpy as np\nrx1_real = np.array([")
    rx1_i.write("import numpy as np\nrx1_imag = np.array([")
    rx2_q.write("import numpy as np\nrx2_real = np.array([")
    rx2_i.write("import numpy as np\nrx2_imag = np.array([")
    rx3_q.write("import numpy as np\nrx3_real = np.array([")
    rx3_i.write("import numpy as np\nrx3_imag = np.array([")

    print(f"Opening file: frames/board_{board}_frame_{frame}.bin")
    # Read binary data
    with open(f'frames/board_{board}_frame_{frame}.bin', 'rb') as f:
        samples = np.fromfile(f, dtype=np.int16)
    
    print(f"Number of samples: {len(samples)}")
    num_samples = int(len(samples)/8)
    print(f"Number of sample sets: {num_samples}")
    
    # Write data to files
    for i in range(num_samples):
        j = i * 8
        rx0_q.write(f"{samples[j]},")
        rx0_i.write(f"{samples[j + 1]},")
        rx1_q.write(f"{samples[j + 2]},")
        rx1_i.write(f"{samples[j + 3]},")
        rx2_q.write(f"{samples[j + 4]},")
        rx2_i.write(f"{samples[j + 5]},")
        rx3_q.write(f"{samples[j + 6]},")
        rx3_i.write(f"{samples[j + 7]},")

    # Finalize files
    rx0_q.write("])\n")
    rx0_i.write("])\n")
    rx1_q.write("])\n")
    rx1_i.write("])\n")
    rx2_q.write("])\n")
    rx2_i.write("])\n")
    rx3_q.write("])\n")
    rx3_i.write("])\n")

    rx0_q.close()
    rx0_i.close()
    rx1_q.close()
    rx1_i.close()
    rx2_q.close()
    rx2_i.close()
    rx3_q.close()
    rx3_i.close()

Parser = argparse.ArgumentParser(description='')
Parser.add_argument('-nframes', dest="nframes", default=1, help='')
Parser.add_argument('-nboards', dest="nboards", default=1, help='')
Args = Parser.parse_args()

for i in range(int(Args.nboards)):
    for j in range(int(Args.nframes)):
        print(f"Parsing board {i} frame {j}")
        parse_bin(j, i)
