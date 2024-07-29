import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BO1260 {
  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int v = Integer.parseInt(st.nextToken());

    int[][] arr = new int[n + 1][n + 1];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      arr[x][y] = 1;
      arr[y][x] = 1;
    }

    boolean[] visited = new boolean[n + 1];
    dfs(arr, visited, v);
    System.out.println();
    visited = new boolean[n + 1];
    bfs(arr, visited, v);
  }

  public static void dfs(int[][] arr, boolean[] visited, int start) {
    visited[start] = true;
    System.out.print(start + " ");
    for (int i = 1; i < arr.length; i++) {
      if (arr[start][i] == 1 && !visited[i]) {
        dfs(arr, visited, i);
      }
    }
  }

  public static void bfs(int[][] arr, boolean[] visited, int start) {
    Queue<Integer> q = new LinkedList<>();
    q.add(start);
    visited[start] = true;

    while (!q.isEmpty()) {
      int x = q.poll();
      System.out.print(x + " ");
      for (int i = 1; i < arr.length; i++) {
        if (arr[x][i] == 1 && !visited[i]) {
          q.add(i);
          visited[i] = true;
        }
      }
    }
  }

}
