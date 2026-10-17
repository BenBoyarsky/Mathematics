import subprocess
from pathlib import Path

#find directory containing this script
project_dir = Path(__file__).resolve().parent

#compile C++
subprocess.run(
    ["g++", "diceAvg.cpp", "-o", "diceAvg"],
    cwd=project_dir,
    check=True
)

#run c++ simulation
subprocess.run(
    ["./diceAvg"],
    cwd=project_dir,
    check=True
)

#run Python graph
subprocess.run(
    ["python3", 'graph.py'],
    cwd=project_dir,
    check=True
)