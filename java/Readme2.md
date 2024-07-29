1. 정렬

```java
// 1차원 배열
Arrays.sort(arr);

// 2차원 배열
Arrays.sort(arr, (e1, e2) -> {
      if (e1[0] == e2[0]) {
        return e1[1] - e2[1];
      } else {
        return e1[0] - e2[0];
      }
    });
```

하지만 이게 더 빠름!!

```java
ArrayList<Integer> list = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      list.add(Integer.parseInt(br.readLine()));
    }

    Collections.sort(list);
```

2. 배열 출력 방법

```java
    // 1차원 배열
    System.out.println(Arrays.toString(arr));
    // 2차원 배열
    System.out.println(Arrays.deepToString(arr));
```

3. 문자열 비교

```java
String str1="abc"
String str2="ddd"
str1.compareTo(str2);
```

4. 큐

```java
Queue<Integer> q = new LinkedList<>();
```

5.  해시맵

- getOrDefault(key, defaultValue)
- key에 대해 map에 저장 된 value를 반환한다.
- 만약 value가 없을 경우 defaultValue값을 반환한다.

```java
		HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    map.put(key, map.getOrDefault(key, 0) + 1);
```

## 시험치기 전 풀어볼 문제

import java.io._;
import java.util._;

1. 9375
2. 1012
