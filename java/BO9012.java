import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BO9012 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    for (int i = 0; i < n; i++) {
      String s = br.readLine();
      int cnt = 0;
      for (int j = 0; j < s.length(); j++) {
        if (s.charAt(j) == '(') {
          cnt++;
        } else {
          cnt--;
        }
        if (cnt < 0) {
          break;
        }
      }
      if (cnt == 0) {
        System.out.println("YES");
      } else {
        System.out.println("NO");
      }
    }
  }
}
