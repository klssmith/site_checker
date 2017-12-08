#!/usr/bin/env python3

import tkinter as tk
# import tkMessageBox
import urllib.request
from hello_world import Application


root = tk.Tk()
app = Application(master=root)




url = 'http://example.com'

try:
    response = urllib.request.urlopen(url)
    app.mainloop()

    print(response.getcode())
except urllib.error.HTTPError as e:

    print(e.getcode())
