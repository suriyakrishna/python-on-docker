from datetime import datetime
import os

n = int(os.environ.get("N_TIMES", 60))

while n > 0:
    print(f"Hello-{n} from python inside docker")
    n -= 1