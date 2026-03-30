import math

class MasseyGateArchive:
    def __init__(self):
        # Constants
        self.c = 299792458
        self.Ep = 1.956e9  # Planck Energy
        self.Lp = 1.616e-35  # Planck Length
        self.kM = self.Ep / (self.Lp**4)  # THE MASSEY CONSTANT

    def show_theory(self):
        header = "=" * 60
        sub_header = "-" * 60
        
        print(f"\n{header}")
        print("          THE MASSEY THEORY OF DIMENSIONAL CONVERGENCE          ")
        print(f"{header}")

        # 1. THE LAW
        print("\n[ 1. THE UNIVERSAL LAW OF RECIPROCITY ]")
        print(f"{sub_header}")
        print(" 'For every infinite surge of 4D energy at a convergence ")
        print("  point, there is an equal and opening reaction in the ")
        print("  5th dimension.'")

        # 2. THE VISUAL EQUATION
        print("\n[ 2. THE CORE MASSEY EQUATION ]")
        print(f"{sub_header}")
        print("      Mg = lim(v->c) [ (m0 / sqrt(1 - v²/c²)) * (Φ5D / kM) ]")
        print(f"{sub_header}")
        print("      Where:")
        print("      Mg   = The Massey Gate (The Bridge)")
        print("      v->c = Object approaching Speed of Light")
        print("      Φ5D  = 5th-Dimensional Point of Convergence")
        print("      kM   = The Massey Constant")

        # 3. THE CONSTANT CALCULATION
        print("\n[ 3. CALCULATING THE MASSEY CONSTANT (kM) ]")
        print(f"{sub_header}")
        print(f"  Formula: kM = Ep / Lp⁴")
        print(f"  Energy Density: {self.kM:.2e} J/m⁴")
        print("  (This represents the 'stiffness' of the 5D fabric.)")

        # 4. THE THREE PILLARS (Visual List)
        print("\n[ 4. SYSTEM PROTOCOLS ]")
        print(f"{sub_header}")
        print("  | PROTOCOL |        DESCRIPTION                            |")
        print(f"{sub_header}")
        print("  | MEDIAN   | Instant CMBR 'Source Code' Reformatting       |")
        print("  | TRAP     | Infinite Mass captured to prevent Big Rip      |")
        print("  | OOPSIE   | The Physical Cut. Do not span the threshold.  |")
        print(f"{sub_header}")

        # 5. THE CMBR SOURCE CODE
        print("\n[ 5. SOURCE CODE METADATA (CMBR) ]")
        print(f"{sub_header}")
        print(f"  Data Origin: 0-Dimensional 'Nil' Universe")
        print(f"  Status: Portable Data (Hardware Independent)")
        
        print(f"\n{header}")
        print("          END OF TRANSMISSION | STATUS: GATE_PENDING           ")
        print(f"{header}\n")

# RUNNING THE VISUALIZER
if __name__ == "__main__":
    archive = MasseyGateArchive()
    archive.show_theory()
