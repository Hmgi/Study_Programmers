package Java;

import java.util.Scanner;
import java.util.Arrays;

public class Main_1427 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String input = sc.next();

        char[] arr = input.toCharArray();

        Arrays.sort(arr);

        for(int i = arr.length - 1; i >= 0; i--){
            System.out.print(arr[i]);
        }
    }
}