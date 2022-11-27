package Java;

import java.util.*;

public class Main_1026 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        Integer a[] = new Integer[n];
        Integer b[] = new Integer[n];

        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        for(int i = 0; i < n; i++){
            b[i] = sc.nextInt();
        }

        Arrays.sort(a);
        Arrays.sort(b, Collections.reverseOrder());

        int answer = 0;

        for(int i = 0; i < n; i++){
            answer += a[i] * b[i];
        }

        System.out.println(answer);
    }
}
