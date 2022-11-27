package Java;

import java.util.*;

class Solution_신고결과 {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, HashSet<String>> map = new HashMap<>();
        Map<String, Integer> idx = new HashMap<>();

        for(int i = 0; i < id_list.length; i++){
            String name = id_list[i];
            map.put(name, new HashSet<>());
            idx.put(name, i);
        }

        for(String s : report){
            String[] str = s.split(" ");
            String from = str[0]; 
            String to = str[1];
            map.get(to).add(from);
        }

        for(int i = 0; i < id_list.length; i++){
            HashSet<String> send = map.get(id_list[i]);
            if(send.size() >= k){
                for(String name : send){
                    answer[idx.get(name)]++;
                }
            }
        }
        return answer;
    }
}

public class 신고결과받기 {
    public static void main(String[] args){
        Solution_신고결과 s = new Solution_신고결과();
        String[] id = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"};
        int k = 2;

        int[] r = s.solution(id, report, k);
        
        for(int i = 0; i < r.length; i++){
            System.out.println(r[i]);
        }
    }
}
