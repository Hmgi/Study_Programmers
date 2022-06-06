import java.util.*;

public class Main_2822{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int[] score = new int[8];
        int[] checkQ = new int[5];
        int totalScore = 0;
        int idx = 0;

        for(int i = 0; i < score.length; i++){
            score[i] = sc.nextInt();
        }

        int[] temp = score.clone();

        Arrays.sort(score);

        for(int i = score.length-1; i >= 3; i--){
            totalScore += score[i];
            checkQ[idx] = findIndex(temp, score[i]);
            idx++;
        }

        System.out.println(totalScore);
        
        Arrays.sort(checkQ);

        for(int i = 0; i < checkQ.length; i++){
            System.out.print(checkQ[i] + " ");
        }
    }

    static int findIndex(int[] arr, int score){
        for(int i = 0; i < arr.length; i++){
            if(score == arr[i]) return i + 1;
        }
        return -1;
    }
}