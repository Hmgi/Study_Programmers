import java.util.*;

public class Main_5555 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        String target = sc.next();
        int line = sc.nextInt();
        int answer = 0;
        for(int i = 0; i < line; i++){
            
            String s = sc.next();

            s += s;

            if(s.contains(target)) answer ++;
            
        }
        System.out.println(answer);
    }
}
