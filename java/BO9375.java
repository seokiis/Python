// Map

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class BO9375 {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st;

    int N = Integer.parseInt(br.readLine());

    for (int i = 0; i < N; i++) {
      int M = Integer.parseInt(br.readLine());
      Map<String, List<String>> map = new HashMap<>();

      for (int j = 0; j < M; j++) {
        st = new StringTokenizer(br.readLine());
        String name = st.nextToken();
        String type = st.nextToken();

        /**
         * Map에 key가 존재하지 않으면 새로운 ArrayList를 생성하여 put
         * 첫 번째 인자 type : 맵에서 찾을 키
         * 두 번째 인자 k->new ArrayList<>() : 키가 존재하지 않을 때 실행할 람다 함수
         * 
         * 만약 type 키가 맵에 이미 존재한다면, 해당 키에 연결된 값(리스트)을 반환합니다.
         * 만약 type키가 맵에 존재하지 않는다면, 새로운 ArrayList생성 후 put
         * 
         * if (!map.containsKey(type)) {
         * map.put(type, new ArrayList<>());
         * }
         * map.get(type).add(name);
         */
        map.computeIfAbsent(type, k -> new ArrayList<>()).add(name);

      }

      /**
       * Map 출력
       */
      // for (Map.Entry<String, List<String>> entry : map.entrySet()) {
      // System.out.println(entry.getKey() + ": " + entry.getValue());
      // }

      int count = 1;
      for (List<String> value : map.values()) {
        count *= (value.size() + 1);
      }
      System.out.println(count - 1);
    }

  }

}
