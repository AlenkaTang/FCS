import java.io.*;
import java.net.*;

public class TCPServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8000);

            while (true) {
                Socket socket = serverSocket.accept();
                
                BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                String message;
                while ((message = reader.readLine()) != null) {
                    String reversedMessage = new StringBuilder(message).reverse().toString();
                    writer.println(reversedMessage);
                }

                socket.close();
                System.out.println("Client disconnected");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
