#!/usr/bin/env python3

import os
import sys
import application

if os.path.sep == '/' and os.geteuid() != 0:
    sys.exit(
        """
        You need to have root privileges to run this script.
        Please try again, this time using 'sudo'. Exiting.
        """
    )

app = application.Application()
app.mainloop()