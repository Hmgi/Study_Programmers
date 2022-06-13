import java.util.*;

public class Main_1789 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        long num = sc.nextLong();
        long sum = 0;
        int answer = 0;
        int i = 1;
        while(true){
            if(sum > num) break;
            sum += i;
            answer ++;
            i ++;
        }

        System.out.println(answer - 1);
    }    
}
