import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class BO1541 {
  public static void main(String[] args) throws Exception {
    int sum = Integer.MAX_VALUE;
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), "-");

    while (st.hasMoreTokens()) {
      int temp = 0;
      StringTokenizer st2 = new StringTokenizer(st.nextToken(), "+");
      while (st2.hasMoreTokens()) {
        temp += Integer.parseInt(st2.nextToken());
      }
      if (sum == Integer.MAX_VALUE) {
        sum = temp;
      } else {
        sum -= temp;
      }
    }
    System.out.println(sum);

  }

}
