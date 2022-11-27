package Java;

import java.util.*;

public class Main_1072 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        long x = sc.nextInt();
        long y = sc.nextInt();

        long z = getPercent(x, y);


        if(z >= 99) System.out.println("-1");
        else{
            long start = 0;
            long end = 2000000000;

            while(start < end){
                long mid = (start + end) / 2;
                long ret = getPercent(x + mid, y + mid);
                
                if(ret > z) end = mid;
                else start = mid + 1;
            }

            System.out.println(end);
        }
    }

    static long getPercent(long x, long y){
        return ((long) y * 100 / x);
    }
}
