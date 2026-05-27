from Qa import inputSpacePartitioning
from Qb import edgeCaseTesting
# from Qc import 
from Qd import test_process_reading
from test_smart_energy_monitor_metamorphic import Qe

def main():
    # Qa
    inputSpacePartitioning()
    # Qb
    edgeCaseTesting()
    # Qc

    # Qd
    test_process_reading()
    # Qe
    Qe()



if __name__ == "__main__":
    main()