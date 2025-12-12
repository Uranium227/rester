# Desktop Break Assistant (Rester) 🌿

A simple, customizable Python automation tool designed to prevent eye strain and maintain productivity during long coding sessions.

## 🚀 About the Project
As a developer, it is easy to get lost in code for hours. This script helps you apply the **20-20-20 rule**:
> "Every **20 minutes**, look at something 20 feet away for **20 seconds**."

Unlike static scripts, **this tool allows you to define your own break intervals** at startup.

## 🛠 Built With
* **Python 3.x**
* **Plyer** (For cross-platform notifications)

## 📦 Installation & Usage

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Uranium227/rester.git](https://github.com/Uranium227/rester.git)
    cd rester
    ```

2.  **Install the dependencies**
    ```bash
    pip install plyer
    ```

3.  **Run the script**
    ```bash
    python rester.py
    ```

4.  **Set your preferences**
    Once the script runs, it will ask for input:
    ```text
    Enter break duration in minutes (default is 20, which is recommended): 
    ```
    * Type a number (e.g., `45`) and press Enter.
    * Or simply press **Enter** to use the default 20 minutes.

## ⚙️ Configuration
The script is interactive by default. However, you can modify the core logic inside `rester.py` if needed.

```python
# The script prompts for input at startup:
BREAK_DURATION_MINUTES = int(input("Enter break duration...") or 20)
