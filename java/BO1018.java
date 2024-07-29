import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.StringTokenizer;
import java.io.IOException;

public class BO1018 {

  public static String[][] WhiteFirst = new String[][] {
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" }
  };

  public static String[][] BlackFirst = new String[][] {
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" },
      { "B", "W", "B", "W", "B", "W", "B", "W" },
      { "W", "B", "W", "B", "W", "B", "W", "B" }
  };

  public static void main(String[] args) throws IOException {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    String[][] arr = new String[N][M];
    for (int i = 0; i < N; i++) {
      arr[i] = br.readLine().split("");
    }

    int min = Integer.MAX_VALUE;

    for (int i = 0; i < N - 7; i++) {
      for (int j = 0; j < M - 7; j++) {
        min = Math.min(min, check(WhiteFirst, arr, i, j));
        min = Math.min(min, check(BlackFirst, arr, i, j));
      }
    }

    System.out.println(min);

  }

  static int check(String[][] first, String[][] arr, int x, int y) {
    int cnt = 0;
    for (int i = x; i < x + 8; i++) {
      for (int j = y; j < y + 8; j++) {
        if (!arr[i][j].equals(first[i - x][j - y])) {
          cnt++;
        }
      }
    }
    return cnt;
  }

}