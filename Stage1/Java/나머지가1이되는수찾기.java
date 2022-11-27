package Java;

class Solution_나머지 {
    public int solution(int n) {
        int answer = 0;

        for(int i = 2; i < n; i++){
            if(n % i == 1) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}


public class 나머지가1이되는수찾기 {
    public static void main(String[] args){
        Solution_나머지 s = new Solution_나머지();
        
        int t1 = 10;
        int t2 = 12;
        System.out.println(s.solution(t1)); //3
        System.out.println(s.solution(t2)); //11
    }
}
