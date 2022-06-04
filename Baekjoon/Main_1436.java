import java.util.*;

public class Main_1436{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int goal = sc.nextInt();
        int count = 1;
        int num = 666;
        while(goal != count){
            num++;

            if(String.valueOf(num).contains("666")){
                count++;
            }
        }

        System.out.println(num);
    }
}