Robotics Logger
===============

Asynchronous Logging System for Space Concordia Robotics Division
------------------------------------------------------------------

You must include the  logger from roboticslogger and multiprocessing
    from roboticslogger.logger import Logger

    from multiprocessing import Process, Pipe

Then create an instance of the logger
    myLogger = Logger()

Create a parent and child communication pipe
    parent_conn, child_conn = Pipe()

Create a process, link it to the logger instance run function and start it
    p = Process(target=myLogger.run, args=(child_conn,))
    
    p.start()

This is how you send messages to the logger
    parent_conn.send(["info", "wtf"])

    parent_conn.send(["warn", "maybe"])
    
    parent_conn.send(["crit", "yea"])
    
    parent_conn.send(["err", "wat"])

This is how you close the logger
    parent_conn.send(["done"])
    
    parent_conn.close()
    

* You don't need to close the connection each time you send a message.
