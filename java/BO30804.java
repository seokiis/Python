// 5
// 5 1 1 2 1

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class BO30804 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];
    st = new StringTokenizer(br.readLine(), " ");

    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    int[] visited = new int[10];
    int left = 0;
    int right = 0;
    int answer = 0;

    while (right < n) {
      visited[arr[right++]]++;
      while (check(visited)) {
        visited[arr[left++]]--;
      }
      answer = Math.max(answer, right - left);
    }

    System.out.println(answer);
  }

  public static boolean check(int[] visited) {
    int count = 0;
    for (int v : visited) {
      if (v != 0)
        count++;
    }
    if (count >= 3)
      return true;
    return false;
  }

}