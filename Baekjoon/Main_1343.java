import java.util.Scanner;

public class Main_1343 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String arr = "";

        String input = sc.next();

        input = input.replaceAll("XXXX", "AAAA");
        input = input.replaceAll("XX", "BB");

        if(input.contains("X")){
            System.out.println("-1");
        }
        else{
            System.out.println(input);
        }

    }
}