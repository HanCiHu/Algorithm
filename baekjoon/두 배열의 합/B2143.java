import java.util.*;
import java.io.*;

public class B2143 {
  static long T, cnt = 0;
  static int N, M;
  static long[] num1;
  static long[] num2;
  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    T = Long.parseLong(br.readLine());

    N = Integer.parseInt(br.readLine());
    num1 = new long[N];
    StringTokenizer st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) num1[i] = Integer.parseInt(st.nextToken());

    M = Integer.parseInt(br.readLine());
    num2 = new long[M];
    st = new StringTokenizer(br.readLine());
    for (int i = 0 ; i < M; i++) num2[i] = Integer.parseInt(st.nextToken());

    List<Long> subA = new ArrayList<>();
    List<Long> subB = new ArrayList<>();

    for (int i = 0 ;i < N; i++){
      Long sum = num1[i];
      subA.add(sum);
      for (int j = i + 1; j < N; j++){
        sum += num1[j];
        subA.add(sum);
      }
    }
    for (int i = 0;i < M; i++){
      long sum = num2[i];
      subB.add(sum);
      for (int j = i + 1; j < M; j++){
        sum += num2[j];
        subB.add(sum);
      }
    }
    
    Collections.sort(subA);
    Collections.sort(subB, Comparator.reverseOrder());

    int pA = 0, pB = 0;

    while (pA < subA.size() && pB < subB.size()){
      long res = subA.get(pA) + subB.get(pB);

      if (res > T) pB++;
      else if (res < T) pA++;
      else {
        long cntA = 0;
        long cntB = 0;
        long a = subA.get(pA);
        long b = subB.get(pB);
        while (pA < subA.size() && subA.get(pA) == a) {
          cntA++;
          pA++;
        }
        while (pB < subB.size() && subB.get(pB) == b) {
          cntB++;
          pB++;
        }
        cnt += (cntA * cntB);
      }
    }
    System.out.println(cnt);
  }
}
