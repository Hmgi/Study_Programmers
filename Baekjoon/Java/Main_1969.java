package Java;

import java.util.*;
public class Main_1969 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int len = sc.nextInt();

        char[][] dna = new char[num][len];
        char[] answer = new char[len];


        for(int i = 0; i < num; i++){
            char[] temp = sc.next().toCharArray();
            for(int j = 0; j < temp.length; j++){
                dna[i][j] = temp[j];
            }
        }

        for(int i = 0; i < len; i++){
            int temp[] = {0, 0, 0, 0};
            for(int j = 0; j < num; j++){
                if(dna[j][i] == 'A') temp[0]++;
                else if(dna[j][i] == 'C') temp[1]++;
                else if(dna[j][i] == 'G') temp[2]++;
                else temp[3]++;
            }

            int index = findIndex(temp);
            if(index == 0) answer[i] = 'A';
            else if(index == 1) answer[i] = 'C';
            else if(index == 2) answer[i] = 'G';
            else answer[i] = 'T';
        }

        for(int i = 0; i < answer.length; i++){
            System.out.print(answer[i]);
        }

        int HD = 0;
        for(int i = 0; i < num; i++){
            for(int j = 0; j < len; j++){
                if(dna[i][j] != answer[j]) HD++;
            }
        }
        System.out.println("");
        System.out.println(HD);
    }

    static int findIndex(int[] arr){
        int index = 0;
        int max = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > max){
                max = arr[i];
                index = i;
            }
        }
        return index;
    }
}
