package Java;

class Solution {
    public int solution(int[] numbers) {
        int answer = 45;

        for(int i = 0; i < numbers.length; i++){
            answer -= numbers[i];
        }
        return answer;
    }
}


public class 없는숫자더하기 {
    public static void main(String[] args){
        Solution s = new Solution();

        int[] t1 = {1, 2, 3, 4, 6, 7, 8, 0};

        System.out.println(s.solution(t1)); //14

        int[] t2 = {5, 8, 4, 0, 6, 7, 9};

        System.out.println(s.solution(t2)); // 6


    }
}
