import java.io.*;
import java.util.StringTokenizer;

public class BO30802 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] sizeArr = new int[6];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 6; i++) {
            sizeArr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int cnt = 0;
        for (int i = 0; i < 6; i++) {
            cnt += sizeArr[i] / T + (sizeArr[i] % T == 0 ? 0 : 1);
        }
        System.out.println(cnt);
        System.out.println(N / P + " " + N % P);

        br.close();

    }
}