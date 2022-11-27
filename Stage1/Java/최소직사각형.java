package Java;

class Solution {
    public int solution(int[][] sizes){
        int min = 1;
        int max = 1;
        int min_temp, max_temp;
        
        for(int i = 0; i < sizes.length; i++){
            if(sizes[i][0] > sizes[i][1]) {
                max_temp = sizes[i][0];
                min_temp = sizes[i][1];
            }
            else{
                max_temp = sizes[i][1];
                min_temp = sizes[i][0];
            }

            if(max < max_temp) max = max_temp;
            if(min < min_temp) min = min_temp;
        }


        return max * min;
    }
}

public class 최소직사각형{
    public static void main(String[] args){
        Solution test = new Solution();
        int arr[][] = {{60,50},{30,70},{60, 30},{80, 40}};
        System.out.println(test.solution(arr));
    }
}