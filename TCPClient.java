import java.io.*;
import java.net.*;

public class TCPClient {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 8000);
            System.out.println("Connected to server");

            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));

            String message;
            while (true) {
                message = consoleReader.readLine();
                if (message.equals("exit")) {
                    break;
                }

                writer.println(message);

                String response = reader.readLine();
                System.out.println("From Server: " + response);
                
            }
            socket.close();
            

            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
