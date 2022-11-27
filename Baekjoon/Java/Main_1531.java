package Java;

import java.util.*;
public class Main_1531 {
    static int[][] arrs = new int[101][101];

    static int down_x;
    static int down_y;
    static int up_x;
    static int up_y;

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int answer = 0;

        initArr();

        for(int i = 0; i < n; i++){
            down_x = sc.nextInt();
            down_y = sc.nextInt();
            up_x = sc.nextInt();
            up_y = sc.nextInt();

            checkQ();
        }

        for(int i = 1; i <= 100; i++){
            for(int j = 1; j <= 100; j++){
                if(arrs[i][j] > m) answer++;
            }
        }

        System.out.println(answer);
    }

    static public void initArr(){
        for(int i = 1; i <= 100; i++){
            for(int j = 1; j <= 100; j++){
                arrs[i][j] = 0;
            }
        }
    }
    
    static public void checkQ(){
        for(int i = down_y; i <= up_y; i++){
            for(int j = down_x; j  <= up_x; j++){
                arrs[i][j]++;
            }
        }
    }
}
