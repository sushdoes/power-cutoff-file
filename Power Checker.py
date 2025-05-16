import psutil
import time
from datetime import datetime

# Function to get the power status (whether plugged in or not)
def get_power_status():
    battery = psutil.sensors_battery()
    return battery.power_plugged

def main():
    was_plugged = get_power_status()
    last_logged_time = time.time()  # Time of last log entry
    debounce_time = 2  # 2 seconds debounce period
    last_state = was_plugged  # Last logged state (plugged or unplugged)
    
    try:
        while True:
            time.sleep(1)  # Check every second
            is_plugged = get_power_status()
            current_time = time.time()

            # Check if state has changed and if enough time has passed since last log
            if is_plugged != last_state and current_time - last_logged_time >= debounce_time:
                message = None
                if is_plugged:
                    message = "Power supply connected!"
                else:
                    message = "Power supply disconnected!"
                
                # Print the message to the terminal
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")
                
                last_state = is_plugged  # Update last logged state
                last_logged_time = current_time  # Update last log time

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
