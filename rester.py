import time
from plyer import notification

# Configuration
BREAK_DURATION_MINUTES = int(input("Enter break duration in minutes (default is 20, which is recommended): ") or 20)
TITLE = "Rest Your Eyes!"
MESSAGE = "20 minutes passed. Look away from the screen for 20 seconds."

def send_notification():
    """Sends a notification to the operating system."""
    print("Sending notification...")
    
   # Send the notification
    notification.notify(
        title = TITLE,
        message = MESSAGE,
        # app_icon = "icon.ico", # You can add an icon path here (optional)
        timeout = 10
    )

def run():
    """Main loop of the program."""
    print(f"Program started! You will be notified every {BREAK_DURATION_MINUTES} minutes.")

    while True:
        duration_minute = BREAK_DURATION_MINUTES * 60  # Convert minutes to seconds
        time.sleep(duration_minute) # Wait for the specified break duration.
        
        send_notification()  # Send the notification after the wait.
               

if __name__ == "__main__":
    run()
