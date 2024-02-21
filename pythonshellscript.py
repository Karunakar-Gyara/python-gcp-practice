import subprocess
import os
subprocess.run(['chmod', '+x', '/c/Users/karun/pythonprograms/stop.sh'], check=True)
#print(f"The script '{'/c/Users/karun/pythonprograms/stop.sh'}' is now executable.")


subprocess.run(['bash', 'stop.sh'], check=True)
print(f"The script '{'stop.sh'}' has been executed.")
