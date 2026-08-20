# Introducing: betterPowerSchedule (bPS)

betterPowerSchedule is the next-version of PowerSchedule. It help user to schedule the computer to shut down or restart.

# Compare with PowerSchedule

||PowerSchedule|betterPowerSchedule|
|---|---|---|
|Latest version|v2.0.0|v1.0.0|
|Framework|tkinter|customtkinter|
|Support|Windows XP+|Windows 10+, macOS and Linux|
|Customizable|No|Yes|
|Comment|No|Yes|
|Accuracy|100% on Windows|100% on Windows and 90% on macOS/Linux|
|Open-Source|-|Available on GitHub and will be on GitLab, BitBucket|
|State of existence|Gone|Available|
|Developer|anlqdev|Flowsine|
|Licence|MIT|MIT|

# How it work?

Windows, macOS and Linux have a command in cmd/Terminal that can schedule the computer to shut down or restart.

So, bPS just run that command on your computer.

> [!TIP]
> Why does bPS use that mechanism instead of performing the action after a countdown within the app itself?
> By using that mechanism, the bPS can be closed without interrupting the counter. This also will not affect the computer's process.

# Download & Installation

### On Windows (stable)

1. Get the download file in [Release page](https://github.com/flowsinecode/betterPowerSchedule/releases)
2. Complete the Installation
3. bPS will be on Start menu

### On macOS and Linux (Beta)

You can't get the download file like Windows because bPS has not yet been exported to an application file like in Windows. But you can try betterPowerSchedule by executing this:

```bash
git clone https://github.com/flowsinecode/betterPowerSchedule bPS
cd bPS
python -m pip install -r requirements.txt
python main.py
```

# How to use

### Start

1. Open bPS
2. Set the timer (h, m, s)
3. Set action (Shut down or Restart)
4. (Option) Set comment (Make it blank to disable)
5. Press Start

### Stop

You just simply press on Stop button

> [!NOTE]
> On macOS and Linux, you have to enter the `sudo` password!

# Screenshot

<img width="379" height="301" alt="image" src="https://github.com/user-attachments/assets/3ae46a49-e558-4297-8417-290dcb605dfa" />

# Report bug

If you found any bugs, feel free to [make a new Issues on GitHub](https://github.com/flowsinecode/betterPowerSchedule/issues/new/choose)!

# Made with ❤ by Flowsine

If you like bPS, please give it a star; I would greatly appreciate it, and it would motivate me to keep developing bPS. Thank you so much! ❤
