import time
import subprocess
import re

import bear

print("Script started")

# Idle threshold (3 minutes)
IDLE_SECONDS = 10
triggered = False

def get_idle_time():
    print("Getting idle time...")
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
    print(f"Got idle ms: {idle_ms}")
    return idle_ms / 1000

print("Entering loop")
while True:
    print("Top of loop")
    idle = get_idle_time()
    print(f"Idle time: {idle:.1f}s, triggered: {triggered}")

    if idle >= IDLE_SECONDS and not triggered:
        print("About to call bear.execute()")
        bear.execute()
        print("Returned from bear.execute()")
        print("Moved mouse after 3 minutes idle.")
        triggered = True

    elif idle < IDLE_SECONDS:
        # User has interacted again
        print("User interacted, resetting triggered")
        triggered = False

    print("Sleeping 1 second")
    time.sleep(1)
