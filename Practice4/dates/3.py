
from datetime import datetime

now = datetime.now()
new_time = now.replace(microsecond=0)

print("Original:", now)
print("Without microsec:", new_time)