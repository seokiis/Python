import java.io.*;
import java.util.*;

public class BO11659 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    int[] arr = new int[N + 1];
    int[] dp = new int[N + 1];

    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= N; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
      dp[i] = dp[i - 1] + arr[i];
    }

    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < M; i++) {
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());

      sb.append(dp[end] - dp[start - 1]).append("\n");
    }

    System.out.println(sb);
  }
}
