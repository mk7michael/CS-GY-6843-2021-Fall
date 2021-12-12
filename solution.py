from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   # Fill in start
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, port))
   #print("socket connection established")
   # Fill in end

   recv = clientSocket.recv(1024).decode()
   # print("recv = " + recv)

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   # print("recv1 = " + recv1)

   # Send MAIL FROM command and print server response.
   # Fill in start
   mailFrom = "MAIL FROM:<>\r\n"
   clientSocket.send(mailFrom.encode())
   recv2 = clientSocket.recv(1024).decode()
   # print("recv2 = " + recv2)
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   rcptTo = "RCPT TO:<>\r\n"
   clientSocket.send(rcptTo.encode())
   recv3 = clientSocket.recv(1024).decode()
   # print("recv3 = " + recv3)
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   data = "DATA\r\n"
   clientSocket.send(data.encode())
   recv4 = clientSocket.recv(1024).decode()
   # print("recv4 = " + recv4)
   # Fill in end

   # Send message data.
   # Fill in start
   clientSocket.send(msg.encode())
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   clientSocket.send(endmsg.encode())
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   quit = "QUIT\r\n"
   clientSocket.send(quit.encode())
   recv5 = clientSocket.recv(1024).decode()
   # print("recv5 = " + recv5)
   clientSocket.close()
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')
