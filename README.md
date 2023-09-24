# N9k-Memory-Monitoring
Memory leak monitoring

# Usage
Start the script using simple while loop or shut/no-shut commands:
```
from cli import *
import cisco 
intf = ['2','3','5','6','7','8','9']
for i in intf:
	cli('configure terminal ; interface ethernet2//1 - 4 ; sleep 10 ; shut ; sleep 1 ; no shut')

# Run Memory monitor script to observe memory leak
