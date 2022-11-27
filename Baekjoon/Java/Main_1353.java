package Java;

import java.util.*;

public class Main_1353 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int s = sc.nextInt();
        int p = sc.nextInt();

        if(s==p){
            System.out.println("1");
            return;
        }

        double prev = -1;
        for(int i = 2; ; i++){
            double curr = Math.pow(1.0 * s / i, i);
            if(prev > curr){
                System.out.println("-1");
                return;

            }
            if(p <= curr){
                System.out.println(i);
                return;
            }
            prev = curr;
        }

    }    
}
