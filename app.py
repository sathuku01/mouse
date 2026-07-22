import time
import subprocess
import re

import bear



# Idle threshold (3 minutes)
IDLE_SECONDS = 10
triggered = False

def get_idle_time():
    result = subprocess.run(
        [
            "gdbus", "call",
            "--session",
            "--dest", "org.gnome.Mutter.IdleMonitor",
            "--object-path", "/org/gnome/Mutter/IdleMonitor/Core",
            "--method", "org.gnome.Mutter.IdleMonitor.GetIdletime"
        ], 
        capture_output=True,
        text=True,
        check=True,
    )
    # Output looks like: "(uint64 12345,)"
    idle_ms = int(re.search(r"uint64 (\d+)", result.stdout).group(1))

    return idle_ms / 1000

while True:
    idle = get_idle_time()


    if idle >= IDLE_SECONDS and not triggered:
        bear.execute()

        print("Moved mouse after 3 minutes idle.")
        triggered = True

    elif idle < IDLE_SECONDS:
        # User has interacted again
        triggered = False

    time.sleep(1)
