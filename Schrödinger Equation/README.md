# **1D Time-Dependent Schrödinger Equation Solver**

This Python application simulates the time evolution of a particle in a one-dimensional box. It demonstrates fundamental quantum phenomena such as **quantum tunneling**, and calculates key properties like **position** and **momentum expectation values**.

## **Features**

- **Hamiltonian Construction**: Builds a 1D Hamiltonian matrix with a user-defined potential barrier.  
- **Time Evolution**: Simulates the time evolution of a Gaussian wave packet using an explicit time-stepping method.  
- **Quantum Tunneling**: Computes the probability of the particle tunneling through the potential barrier.  
- **Expectation Values**: Calculates the expectation values of position ⟨x⟩ and momentum ⟨p⟩ at various time steps.  
- **Energy Level Analysis**: Finds stationary energy states and compares them to analytical solutions for a particle in a box.  
- **Interactive Input**: Prompts the user for key parameters, enabling easy experimentation.  
- **Data Export**: Saves wavefunction data at selected time points to text files for plotting and analysis.

## **How to Run**

### **Prerequisites**

Save this file as `README.md`. Ensure Python and NumPy are installed.

```bash
pip install numpy
```

### **Execution**

Run the simulation with:

```bash
python main.py
```

The program will then guide you through prompts to define simulation parameters.

## **User Inputs**

The program requires the following parameters:

| Parameter              | Description                                                                 | Example |
|-------------------------|-----------------------------------------------------------------------------|---------|
| **Box length L**        | Size of the 1D box                                                         | 1.0     |
| **Grid points N**       | Number of spatial grid points (higher = more accuracy, slower computation) | 100     |
| **Barrier height V0**   | Height of the potential barrier                                            | 100.0   |
| **Barrier center x**    | Position of the barrier's center                                           | 0.5     |
| **Barrier width**       | Width of the potential barrier                                             | 0.2     |
| **Time steps**          | Number of simulation steps                                                 | 50      |
| **Time step dt**        | Size of each time step                                                     | 0.001   |
| **Wavepacket center x0**| Initial center position of the Gaussian wave packet                        | 0.2     |
| **Wavepacket width σ**  | Width of the wave packet (smaller = more certain position, less certain p) | 0.1     |
| **Momentum k0**         | Initial momentum of the wave packet                                        | 50.0    |

## **Output**

The program produces:

1. **Instructions** – overview of the simulation.  
2. **Parameter Summary** – recap of user inputs.  
3. **Energy Levels** – calculated values vs. analytical solutions.  
4. **Time Evolution Results** – for selected times (t = 0, mid, final):  
   - Probability density ∣ψ∣² at sample points.  
   - Total tunneling probability.  
   - Expectation values ⟨x⟩ and ⟨p⟩.

Data files are saved as `wavefunction_t0.txt`, `wavefunction_t<mid>.txt`, and `wavefunction_t<final>.txt`. Each contains two columns: **position** and **probability density**.

## **Future Improvements**

- **Performance Optimization**: Use vectorized NumPy operations instead of explicit loops.  
- **Visualization**: Add matplotlib plots for wavefunction evolution.  
- **GUI/Web Interface**: Develop an interactive GUI or web app.  
- **Advanced Potentials**: Extend to double wells and other potentials.  
- **Error Handling**: Add stricter validation (e.g., barrier must fit inside box).

### Important Note for Code in Place Implementation

This program's full functionality, including the saving of wavefunction data to `.txt` files, is designed for a standard Python environment. Due to the sandboxed nature of the Code in Place IDE, file-saving operations are not supported, and this part of the code will not function. The rest of the program's core features, such as the console output and calculations, will work as described. Check [Code in Place](https://codeinplace.stanford.edu/cip4/share/XvcOx4b3aESAdLDbro7T) project now!
