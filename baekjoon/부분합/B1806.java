import java.util.*;
import java.io.*;

public class B1806 {
  static int N, S, sum = 0, min = 10000000;
  static int[] nums;
  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    S = Integer.parseInt(st.nextToken());
    nums = new int[N + 1];

    st = new StringTokenizer(br.readLine());
    for (int i = 0 ;i < N; i++) nums[i] = Integer.parseInt(st.nextToken());

    int low = 0, high = 0;
    sum = nums[0];

    while (high < N) {
      if (sum < S) sum += nums[++high];
      else {
        min = Math.min(min, high - low + 1);
        sum -= nums[low++];
      }
    }
    if (min == 10000000) System.out.println(0);
    else System.out.println(min);
  }
}
