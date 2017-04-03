William Christian - wchristian6@gatech.edu
April 3, 2017

CS 3251 Project 2

PYTHON VERSION 2.7

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Files:

-reldat-client ~ the client side of the RELDAT protocol
-reldat-server ~ the client side of the RELDAT protocol
-utils.py ~ common functions shared between hosts
-sample.txt ~ a sample text file to send to serverIP
-DesignDocument.pdf ~ more detail of the RELDAT protocol
-README.txt ~ this file

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How To Run:

Make sure to run using Python 2.7.

To start the server, navigate to the file in terminal in enter the following command:
 -$ python reldat-server <PORT> <WindowSize>
 e.g.) python reldat-server 5099 35

 Next, start the client by entering:
 -$ python reldat-client <IP:PORT> <WindowSize>
 e.g.) python reldat-server 127.0.0.1:5099 35

You will now see the following prompt in the reldat-client terminal:

ENTER: connect, transform <filename.txt>, or disconnect:

You first need to enter 'connect' to establish a connection with the server on the specified port.
e.g.) ENTER: connect, transform <filename.txt>, or disconnect: connect

Once connected, we can send a file to the server as follows:
ENTER: connect, transform <filename.txt>, or disconnect: transform sample.txt

Finally, we can disconnect from the server by typing 'disconnect'
e.g.) ENTER: connect, transform <filename.txt>, or disconnect: disconnect
