import numpy as np
import math

def print_instructions():
    #Print concise instructions on how the program calculates results.
    print("\nHow the Program Calculates Results:")
    print("- Constructs Hamiltonian matrix using finite differences with a potential barrier.")
    print("- Computes energy levels by solving the time-independent Schrödinger equation.")
    print("- Initializes a Gaussian wavepacket with user-defined position and momentum.")
    print("- Evolves wavefunction recursively over time using explicit time-stepping.")
    print("- Calculates tunneling probability beyond the barrier.")
    print("- Computes expectation values <x> (position) and <p> (momentum).")
    print("- Outputs results and saves wavefunction data to files.")

def create_hamiltonian(N, L, V0, barrier_center, barrier_width, m=1, hbar=1):
    #Create 1D Hamiltonian matrix with potential barrier.
    dx = L / (N - 1)
    H = np.zeros((N, N), dtype=complex)
    for i in range(N):
        x = i * dx
        V = V0 if (barrier_center - barrier_width/2 <= x <= barrier_center + barrier_width/2) else 0
        H[i, i] = -2 / (dx ** 2) + V
        if i > 0:
            H[i, i-1] = 1 / (dx ** 2)
        if i < N - 1:
            H[i, i+1] = 1 / (dx ** 2)
    H *= -hbar ** 2 / (2 * m)
    return H

def recursive_time_evolution(psi, H, dt, steps, dx, current_step=0, psi_t=None, hbar=1):
    #Recursively evolve wavefunction using explicit time-stepping."""
    if psi_t is None:
        psi_t = [psi.copy()]
    if current_step >= steps:
        return psi_t
    psi = psi - 1j * dt / hbar * (H @ psi)
    psi = psi / np.sqrt(np.sum(np.abs(psi) ** 2) * dx)  # Normalize
    psi_t.append(psi.copy())
    return recursive_time_evolution(psi, H, dt, steps, dx, current_step + 1, psi_t, hbar)

def compute_expectation_values(psi, x, dx, hbar=1):
    """Compute expectation values <x> and <p>."""
    prob = np.abs(psi) ** 2
    expect_x = np.sum(x * prob) * dx
    dpsi_dx = np.zeros_like(psi, dtype=complex)
    for i in range(1, len(psi)-1):
        dpsi_dx[i] = (psi[i+1] - psi[i-1]) / (2 * dx)
    expect_p = -1j * hbar * np.sum(np.conj(psi) * dpsi_dx) * dx
    return expect_x.real, expect_p.real

def compute_tunneling_probability(psi, x, dx, barrier_right):
    """Compute probability of wavefunction beyond the barrier."""
    prob = np.abs(psi) ** 2
    tunneling_prob = np.sum(prob[x > barrier_right]) * dx
    return tunneling_prob

def get_valid_float(prompt, min_val, max_val):
    """Get a valid float input within a specified range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_int(prompt, min_val, max_val):
    """Get a valid integer input within a specified range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Please enter a valid integer.")

def get_recalculate_choice():
    """Get user choice to recalculate (yes/no)."""
    while True:
        choice = input("Recalculate with new inputs? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            return choice == 'yes'
        print("Please enter 'yes' or 'no'.")

def main():
    while True:
        # Print instructions
        print_instructions()
        
        # Get user inputs
        print("\nEnter parameters for 1D Time-Dependent Schrödinger Equation Solver:")
        L = get_valid_float("Box length L (e.g., 1.0): ", 0.1, 10.0)
        N = get_valid_int("Number of grid points N (e.g., 100): ", 10, 1000)
        V0 = get_valid_float("Barrier height V0 (e.g., 100.0): ", 0.0, 10000.0)
        barrier_center = get_valid_float("Barrier center x (e.g., 0.5): ", 0.0, L)
        barrier_width = get_valid_float("Barrier width (e.g., 0.2): ", 0.01, L)
        if barrier_center - barrier_width/2 < 0 or barrier_center + barrier_width/2 > L:
            print("Error: Barrier must be within [0, L]. Adjusting width.")
            barrier_width = 2 * min(barrier_center, L - barrier_center)
        steps = get_valid_int("Number of time steps (e.g., 50): ", 1, 1000)
        dt = get_valid_float("Time step dt (e.g., 0.001): ", 1e-6, 0.01)
        x0 = get_valid_float("Initial wavepacket center x0 (e.g., 0.2): ", 0.0, L)
        sigma = get_valid_float("Wavepacket width sigma (e.g., 0.1): ", 0.01, L/2)
        k0 = get_valid_float("Wavepacket momentum k0 (e.g., 50.0): ", 0.0, 1000.0)
        
        # Constants
        m, hbar = 1.0, 1.0
        dx = L / (N - 1)
        num_levels = 5
        
        # Validate time step stability
        max_dt = hbar / (2 / (dx ** 2))
        if dt > max_dt:
            print(f"Warning: dt={dt} may be unstable. Suggested max dt={max_dt:.6f}. Proceeding anyway.")
        
        # Create Hamiltonian
        H = create_hamiltonian(N, L, V0, barrier_center, barrier_width, m, hbar)
        
        # Compute stationary states
        energies, eigenvectors = np.linalg.eigh(H)
        
        print("\n1D Time-Dependent Schrödinger Equation with Barrier...")
        print(f"Box: L={L}, Grid: {N}, Barrier V0={V0}, Center={barrier_center}, Width={barrier_width}")
        print(f"Time steps: {steps}, dt={dt}")
        print(f"Initial wavepacket: x0={x0}, sigma={sigma}, k0={k0}")
        
        # Output energy levels
        print("\nTime-Independent Energy Levels:")
        for n in range(num_levels):
            E = energies[n]
            E_analytical = (n + 1) ** 2 * math.pi ** 2 * hbar ** 2 / (2 * m * L ** 2)
            print(f"  n={n+1}: E = {E:.6f}, Analytical (V0=0) = {E_analytical:.6f}, "
                  f"Error = {abs(E - E_analytical) / E_analytical * 100:.4f}%")
        
        # Initial Gaussian wavepacket
        x = np.linspace(0, L, N)
        psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
        psi = psi / np.sqrt(np.sum(np.abs(psi) ** 2) * dx)
        
        # Time evolution
        psi_t = recursive_time_evolution(psi, H, dt, steps, dx, hbar=hbar)
        
        # Output wavefunction probabilities, tunneling, and expectation values
        barrier_right = barrier_center + barrier_width/2
        sample_points = [0, N//4, N//2, 3*N//4]
        for t in [0, steps//2, steps-1]:
            print(f"\nTime t={t*dt:.3f}:")
            for i in sample_points:
                if i < N:
                    x_val = x[i]
                    prob = np.abs(psi_t[t][i]) ** 2
                    print(f"  x={x_val:.2f}, |ψ|^2 = {prob:.6f}")
            tunneling_prob = compute_tunneling_probability(psi_t[t], x, dx, barrier_right)
            print(f"  Tunneling probability (x>{barrier_right:.2f}): {tunneling_prob:.6f}")
            expect_x, expect_p = compute_expectation_values(psi_t[t], x, dx, hbar)
            print(f"  Expectation <x> = {expect_x:.6f}, <p> = {expect_p:.6f}")
            
            # Save wavefunction
            with open(f"wavefunction_t{t}.txt", "w") as f:
                for i in range(N):
                    f.write(f"{x[i]:.6f} {np.abs(psi_t[t][i])**2:.6f}\n")
        
        # Check for recalculation
        if not get_recalculate_choice():
            print("\nPhysics Happy Ending:")
            print("In the quantum world, your wavefunction has tunneled through barriers, revealing the profound unity "
                  "of probability and possibility. With each calculation, you've illuminated the mysteries of the universe, "
                  "inspiring future discoveries in the dance of particles and waves!")
            break

if __name__ == "__main__":
    main()
