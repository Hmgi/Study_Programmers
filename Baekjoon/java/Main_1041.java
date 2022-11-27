package java;

import java.util.*;

public class Main_1041 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[] dice = new int[6];
        
        long n = sc.nextInt();

        for(int i = 0; i < dice.length; i++){
            dice[i] = sc.nextInt();
        }

        if(n != 1){
            long min_3 = find_min3(dice);
            long min_2 = find_min2(dice);
            long min_1 = find_min1(dice);

            long sum = 4 * min_3;
            sum += (8 * n - 12) * min_2;
            sum += (n - 2) * (5 * n - 6) * min_1;
            System.out.println(sum);
        }
        else{
            System.out.println(one_dice(dice));
        }
        
    }

    static long find_min3(int[] arr){
        long min = 0;

        //0 - 5
        min += (arr[0] < arr[5]? arr[0] : arr[5]);
        //1 - 4
        min += (arr[1] < arr[4]? arr[1] : arr[4]);
        //2 - 3
        min += (arr[2] < arr[3]? arr[2] : arr[3]);

        return min;
    }

    static long find_min2(int[] arr){
        long min = arr[0] + arr[1];

        for(int i = 0; i < arr.length; i++){
            for(int j = i + 1; j < arr.length; j++){
                if(i + j == 5) continue;
                if(min > arr[i] + arr[j]) min = arr[i] + arr[j];
            }
        }
        return min;
    }

    static long find_min1(int[] arr){
        long min = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < min) min = arr[i];
        }
        return min;
    }

    static long one_dice(int[] arr){
        long min = 0;
        long max = 0;

        for(int i = 0; i < arr.length; i++){
            min += arr[i];
            if(max < arr[i]) max = arr[i];
        }

        return min - max;
    }
}
