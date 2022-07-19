import java.io.*;
import java.util.*;

class B2003{
  static int N, target, sum = 0, low = 0, high = 0, ans = 0;
  static int[] nums;
  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    target = Integer.parseInt(st.nextToken());
    nums = new int[N + 1];

    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) nums[i] = Integer.parseInt(st.nextToken());

    sum = nums[0];

    while (high < N){
      if (sum < target) {
        high++;
        sum += nums[high];
      }
      else if (sum >= target) {
        if (sum == target) ans++;
        sum -= nums[low];
        low++;
      }
    }
    System.out.println(ans);
  }
}