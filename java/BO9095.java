import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BO9095 {
  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    for (int i = 0; i < N; i++) {
      int n = Integer.parseInt(br.readLine());
      int[] dp = new int[n + 1];
      dp[0] = 1;
      dp[1] = 1;
      if (n >= 2) {
        dp[2] = 2;
      }
      for (int j = 3; j <= n; j++) {
        dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3];
      }
      System.out.println(dp[n]);
    }

  }

}
