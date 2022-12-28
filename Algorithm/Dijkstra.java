import java.util.ArrayList;
import java.util.PriorityQueue;

public class Dijkstra {
    static class Node{
        int v; //간선
        int cost; //가중치

        public Node(int v, int cost) {
            this.v = v;
            this.cost = cost;
        }
    }

    //각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
    static ArrayList<Node>[] graph;
    //방문한 적이 있는지 체크하는 목적의 리스트
    static boolean[] visit;
    //최단 거리 테이블
    static int[] dist;

    public static void main(String[] args){

        int v = 6;
        int k = 1;

        int[][] roots = {{1, 2, 2}, {1, 3, 5}, {1, 4, 3}
                , {2, 3, 7}, {2, 6, 10}, {2, 6, 10}
                , {3, 4, 1}, {3, 5, 2}, {3, 6, 5}, {3, 1, 5}, {3, 2, 7}
                , {4, 5, 7}, {4, 3, 1}, {4, 1, 3}
                , {5, 6, 2}, {5, 2, 10}, {5, 3, 5}};


        graph = new ArrayList[v + 1];
        dist = new int[v + 1];
        visit = new boolean[v + 1];

        for (int i = 1; i <= v; i++) {
            graph[i] = new ArrayList<>();
            dist[i] = Integer.MAX_VALUE; //최대값으로 초기화, 최단거리를 찾기 위함.
        }
        for(int[] root : roots){
            graph[root[0]].add(new Node(root[1], root[2]));
        }
        //다익스트라 알고리즘 수행
        dijkstra(k);

        for (int i = 1; i <= v; i++) {
            System.out.println(dist[i] == Integer.MAX_VALUE ? "INF" : dist[i]);
        }
    }

    static void dijkstra(int start) {
        //우선 순위 큐 사용, 가중치를 기준으로 오름차순한다.
        PriorityQueue<Node> q = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
        //시작 노드에 대해서 초기화
        q.add(new Node(start, 0));
        dist[start] = 0;

        while (!q.isEmpty()) {
            //현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리 한다.
            Node now = q.poll();

            if (!visit[now.v]) {
                visit[now.v] = true;
            }

            for (Node next : graph[now.v]) {

                //방문하지 않았고, 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧을 경우
                if (!visit[next.v] && dist[next.v] > now.cost + next.cost) {
                    dist[next.v] = now.cost + next.cost;
                    q.add(new Node(next.v, dist[next.v]));
                }
            }
        }
    }
}

