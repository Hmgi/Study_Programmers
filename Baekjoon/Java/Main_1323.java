package Java;

import java.util.*;
public class Main_1323 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();
        long calc = n;
        int answer = 0;
        HashSet<Long> set = new HashSet<>();

        while(true){
            answer++;
            calc %= k;

            if(calc == 0) break;

            if(!set.add(calc)){
                System.out.println(-1);
                return;
            }
            calc = appendNum(calc, n);
            //System.out.println(calc);
        }
        System.out.println(answer);
    }

    static long appendNum(long num, int n){
        String temp = Long.toString(num) + Integer.toString(n);
        return Long.parseLong(temp);
    }
}
