package Java;

import java.util.*;

class Solution_구명보트 {
    public int solution(int[] people, int limit) {
        int answer = 0;

        Arrays.sort(people);

        int min = 0;

        for (int max = people.length - 1; min <= max; max--){
            if (people[min] + people[max] <= limit) min++;
            answer++;
        }
        
        return answer;
    }
}

public class 구명보트 {
    public static void main(String[] args){

        Solution_구명보트 s = new Solution_구명보트();

        int[] p1 = {70, 50, 80, 50};
        int l1 = 100;

        int[] p2 = {70, 80, 50};
        int l2 = 100;

        System.out.println(s.solution(p1, l1));
        System.out.println(s.solution(p2, l2));
    }
}
