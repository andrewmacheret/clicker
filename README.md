# clicker.py

An auto-clicker script that runs in python on macOS and listens to the capslock key state.

# usage

1. compile and test `CheckModKeys`

    ```
    gcc -framework Carbon CheckModKeys.m -o CheckModKeys
    ./CheckModKeys capslock
    ```

    `CheckModKeys` should output `1` when capslock is pressed, and `0` if it is not.

2. install requirements for pyautogui

    ```
    pip3 install pyobjc-framework-Quartz
    pip3 install pyobjc-core
    pip3 install pyobjc
    pip3 install pyautogui
    ```

3. run it

    ```
    python3 clicker.py
    ```

    The script will loop forever...
      * If capslock key is set, click as fast as possible
      * If capslock key is not set, do nothing
