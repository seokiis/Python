// 3 5
// OOOPO
// OIOOX
// OOOXP

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BO21736 {

  static int[] dx = { 0, 0, 1, -1 };
  static int[] dy = { 1, -1, 0, 0 };

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;
    st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    char[][] arr = new char[n][m];

    // for (int i = 0; i < n; i++) {
    // st = new StringTokenizer(br.readLine());
    // for (int j = 0; j < m; j++) {
    // arr[i][j] = st.nextToken().charAt(0);
    // }
    // }

    for (int i = 0; i < n; i++) {
      arr[i] = br.readLine().toCharArray();
    }

    int result = 0;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (arr[i][j] == 'I') {
          result = bfs(arr, i, j, n, m);
        }
      }
    }

    System.out.println(result == 0 ? "TT" : result);

  }

  public static int bfs(char[][] arr, int x, int y, int n, int m) {
    int cnt = 0;
    Queue<int[]> q = new LinkedList<>();
    boolean visited[][] = new boolean[n][m];
    q.add(new int[] { x, y });
    while (!q.isEmpty()) {
      int[] cur = q.poll();
      visited[cur[0]][cur[1]] = true;
      for (int i = 0; i < 4; i++) {
        int nx = cur[0] + dx[i];
        int ny = cur[1] + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
          if (arr[nx][ny] == 'P') {
            q.add(new int[] { nx, ny });
            visited[nx][ny] = true;
            cnt++;
          }
          if (arr[nx][ny] == 'O') {
            visited[nx][ny] = true;
            q.add(new int[] { nx, ny });
          }
        }

      }
    }
    return cnt;
  }
}