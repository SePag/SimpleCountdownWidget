# Beautiful Simple Countdown Widget

![Alt Text](http://pagel-sebastian.de/images/countdownWidget.gif)

This is a simple countdown widget for Python, implemented with tkinter. As tkinter is part of the Python standard library, no additional sources are required. Calling the `start()` method launches a separate process which runs the gui thread. After the countdown finishes, the process terminates.

Usage example:

```python
from CountdownWidget import CountdownWidget

if __name__ == "__main__":
    countdownWidget = CountdownWidget(countdownMs = 10000)
    countdownWidget.start()
```



