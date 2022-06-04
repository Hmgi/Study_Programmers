import java.util.*;

public class Main_1475{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        String num = sc.next();

        char[] arr = num.toCharArray();

        int[] sArr = toIntArr(arr);

        System.out.println(checkArr(sArr));
    }

    static int checkArr(int[] arr){
        int[] numBox = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        for(int i = 0; i < arr.length; i++){
            if(arr[i] == 6 || arr[i] == 9){
                if(numBox[6] < numBox[9]){
                    numBox[6]++;
                }
                else{
                    numBox[9]++;
                }
            }

            else{
                numBox[arr[i]]++;
            }
        }
        Arrays.sort(numBox);
        return numBox[numBox.length - 1];
    }

    static int[] toIntArr(char[] arr){
        int[] tArr = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            tArr[i] = arr[i] - '0';
        }
        return tArr; 
    }
}