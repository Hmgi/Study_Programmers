package Java;

import java.util.Collections;
import java.util.PriorityQueue;

public class 야근지수 {
    public static void main(String[] args) {
        Solution_야근 s = new Solution_야근();

        int[] works = {4, 3, 3};
        int n = 4;

        System.out.println(s.solution(n, works)); // 12
    }
}

class Solution_야근 {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        for (int j : works) {
            q.offer(j);
        }

        while(n > 0) {
            int work = q.poll();
            if(work == 0) break; //더 이상 줄일 수 있는 일이 없음.
            work -= 1; //일 한시간 줄인다.
            q.offer(work);
            n -= 1; // 남은 작업 시간 한시간 줄인다.
        }

        long answer = 0;
        for(int work : q) {
            answer += (long) work * work;
        }
        return answer;
//        long answer = 0;
//        while(n > 0){
//            Arrays.sort(works);
//            works[works.length - 1] -= 1;
//            n -= 1;
//        }
//
//        for (int work : works) {
//            if(work < 0) work = 0;
//            answer += (long) work * work;
//        }
//
//        return answer;
    }
}
