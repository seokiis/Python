import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BO10814 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    String[][] arr = new String[N][];

    for (int i = 0; i < N; i++) {
      String[] s = br.readLine().split(" ");
      arr[i] = new String[] { s[0], s[1] };
    }

    Arrays.sort(arr, (e1, e2) -> {
      return Integer.parseInt(e1[0]) - Integer.parseInt(e2[0]);
    });

    for (String[] el : arr) {
      System.out.println(el[0] + " " + el[1]);
    }

  }

}
