Robotics Logger
===============

Asynchronous Logging System for Space Concordia Robotics Division
------------------------------------------------------------------

### How to use

You must include the  logger from roboticslogger and multiprocessing
<code>
from roboticslogger.logger import Logger
from multiprocessing import Process, Pipe
</code>

Then create an instance of the logger
<code>
myLogger = Logger()
</code>

Create a parent and child communication pipe
<code>
parent_conn, child_conn = Pipe()
</code>

Create a process, link it to the logger instance run function and start it
<code>
p = Process(target=myLogger.run, args=(child_conn,))
p.start()
</code>


This is how you send messages to the logger
<code>
parent_conn.send(["info", "wtf"])

parent_conn.send(["warn", "maybe"])

parent_conn.send(["crit", "yea"])

parent_conn.send(["err", "wat"])
</code>

This is how you close the logger
<code>
parent_conn.send(["done"])
parent_conn.close()
</code>


# You don't need to close the connection each time you send a message.


