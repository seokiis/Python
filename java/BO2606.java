import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BO2606 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    int N = Integer.parseInt(br.readLine());
    int M = Integer.parseInt(br.readLine());

    List<List<Integer>> graph = new ArrayList<>();

    // List<Integer>[] arr = new ArrayList[N + 1];
    // for (int i = 0; i < N + 1; i++) {
    // arr[i] = new ArrayList<>();
    // }

    for (int i = 0; i < N + 1; i++) {
      graph.add(new ArrayList<>());
    }

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      graph.get(a).add(b);
      graph.get(b).add(a);
    }

    boolean[] visited = new boolean[N + 1];
    int count = bfs(graph, visited, 1) - 1;

    System.out.println(count);
  }

  public static int bfs(List<List<Integer>> graph, boolean[] visited, int start) {
    Queue<Integer> q = new LinkedList<>();
    q.add(start);
    visited[start] = true;

    int count = 0;
    while (!q.isEmpty()) {
      int x = q.poll();
      count++;

      for (int i = 0; i < graph.get(x).size(); i++) {
        int y = graph.get(x).get(i);

        if (!visited[y]) {
          q.add(y);
          visited[y] = true;
        }
      }
    }

    return count;

  }

}
