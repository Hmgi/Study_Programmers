package Java;

import java.util.*;

public class Main_2303{

    static int[][] arr;
    static int n;
    static int[] max;

    public static void main(String[] args){
        
        initArr();
        
        max = new int[n];
        int answer = 0;
        int idx = 1;
        for(int i = 0; i < n; i++){
            max[i] = findMax(i);
            if(answer <= max[i]){
                answer = max[i];
                idx = i;
            }
        }

        System.out.println(idx + 1);
    }

    static void initArr(){
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        arr = new int[n][5];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < 5; j++){
                arr[i][j] = sc.nextInt();
            }
        }
    }

    static int findMax(int index){
        int max = 0;

        for(int i = 0; i < 3; i++){
            for(int j = i + 1; j < 4; j++){
                for(int k = j + 1; k < 5; k++){
                    if((arr[index][i]+arr[index][j]+arr[index][k]) % 10 > max) max = (arr[index][i]+arr[index][j]+arr[index][k]) % 10;
                }
            }
        }

        return max;
    }
}

/*
3
7 5 5 4 9
1 1 1 1 1
2 3 3 2 10
*/