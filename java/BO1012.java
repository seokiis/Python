import java.util.*;
import java.io.*;

public class BO1012 {

  static int[] dx = { 1, -1, 0, 0 };
  static int[] dy = { 0, 0, 1, -1 };

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int N = Integer.parseInt(br.readLine());
    for (int i = 0; i < N; i++) {

      st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      int k = Integer.parseInt(st.nextToken());

      int[][] arr = new int[n][m];
      for (int j = 0; j < k; j++) {
        st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        arr[x][y] = 1;
      }

      // arr 돌면서 bfs
      int ans = 0;
      for (int x = 0; x < n; x++) {
        for (int y = 0; y < m; y++) {
          if (arr[x][y] == 1) {
            bfs(arr, x, y);
            ans++;
          }
        }
      }
      System.out.println(ans);

    }
  }

  public static void bfs(int[][] arr, int x, int y) {
    Queue<int[]> q = new LinkedList<>();
    q.add(new int[] { x, y });

    while (!q.isEmpty()) {
      int[] cur = q.poll();
      for (int i = 0; i < 4; i++) {
        int nx = cur[0] + dx[i];
        int ny = cur[1] + dy[i];

        if (nx >= 0 && ny >= 0 && nx < arr.length && ny < arr[0].length && arr[nx][ny] == 1) {
          // visited 처리
          arr[nx][ny] = arr[nx][ny] - 1;
          q.add(new int[] { nx, ny });
        }
      }

    }

  }
}
