// 5
// 4 1 5 2 3
// 5
// 1 3 7 9 5

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BO1920 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int n = Integer.parseInt(br.readLine());

    int[] arr = new int[n];
    st = new StringTokenizer(br.readLine(), " ");
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }
    Arrays.sort(arr);

    int m = Integer.parseInt(br.readLine());
    st = new StringTokenizer(br.readLine(), " ");
    int[] arr2 = new int[m];
    for (int i = 0; i < m; i++) {
      arr2[i] = Integer.parseInt(st.nextToken());
    }

    StringBuilder sb = new StringBuilder();

    for (int el : arr2) {
      if (Arrays.binarySearch(arr, el) >= 0) {
        sb.append(1).append('\n');
      } else {
        sb.append(0).append('\n');
      }
    }

    System.out.println(sb);

  }

}
