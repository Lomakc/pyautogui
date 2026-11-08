import time
import pyautogui

def auto_type(text: str, delay_before_start: int = 5, interval: float = 0.05):
    """
    Automates typing a given string.

    :param text: The text string to type.
    :param delay_before_start: Seconds to wait before starting (allows switching to the target window).
    :param interval: Delay in seconds between each keystroke to simulate natural typing.
    """
    # Countdown to give time to focus the desired text input field
    for remaining in range(delay_before_start, 0, -1):
        print(f"Starting in {remaining} seconds... Focus your target window.", end="\r")
        time.sleep(1)
    print("\nTyping started...")

    # Type the text character by character
    pyautogui.write(text, interval=interval)
    
    # Optionally press Enter at the end
    # pyautogui.press('enter')

if __name__ == "__main__":
    message = "Hello, this text is being typed automatically using Python!"
    auto_type(message, delay_before_start=5, interval=0.05)
