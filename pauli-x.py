import matplotlib.pyplot as plt
import os
from qiskit import *
from qiskit_aer.primitives import SamplerV2
from qiskit.visualization import plot_bloch_multivector

# __________________________________________________________________________ ||
# Configurables
# __________________________________________________________________________ ||
output_dir = 'output/pauli-x/'

def main():

    # ______________________________________________________________________ ||
    # Create a quantum circuit with a single qubit
    # ______________________________________________________________________ ||
    qc = QuantumCircuit(1)

    # ______________________________________________________________________ ||
    # Apply the PauliX-gate on the qubit
    # ______________________________________________________________________ ||
    qc.x(0)
    qc.measure_all()
    
    # ______________________________________________________________________ ||
    # Draw the circuit
    # ______________________________________________________________________ ||
    os.makedirs(output_dir,exist_ok=True)
    fig = qc.draw('mpl')
    fig.savefig(os.path.join(output_dir,'circuit.png'))

    # ______________________________________________________________________ ||
    # Execute the circuit on a simulation backend
    # ______________________________________________________________________ ||
    sampler = SamplerV2()
    job = sampler.run([qc], shots=128)
    job_result = job.result()
    print(f"Counts for quantum circuit : {job_result[0].data.meas.get_counts()}")

if __name__ == '__main__':
    main()
