package Java;

public class Main_4673{
    public static void main(String[] args){

        boolean[] arr = new boolean[10001];
        
        for(int i = 1; i < 10001; i++){
            int num = d(i);

            if(num < 10001) arr[num] = true;
        }

        for(int i = 1; i < 10001; i++){
            if(!arr[i]) System.out.println(i);
        }
    }

    static int d(int num){
        int sum = num;
        while(num != 0){
            sum += (num % 10);
            num /= 10;
        }
        return sum;
    }
}