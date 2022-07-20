import java.util.*;
import java.io.*;

public class B1202 {
  static int N, K;
  static jewel[] jewels;
  static int[] bag;
  public static void main(String[] args) throws Exception{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    jewels = new jewel[N];
    bag = new int[K];

    for (int i = 0; i < N ;i ++){
      st = new StringTokenizer(br.readLine());
      jewels[i] = new jewel(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
    }
    for (int i = 0; i < K; i++) bag[i] = Integer.parseInt(br.readLine());

    Arrays.sort(bag);
    Arrays.sort(jewels, Comparator.comparingInt(jewel::getM));
    PriorityQueue<jewel> pq = new PriorityQueue<>(Comparator.comparingInt(jewel::getV).reversed());

    long sum = 0;
    int ji = 0;
    
    for (int i = 0; i < bag.length; i++){
      while (ji < N && bag[i] >= jewels[ji].M) pq.add(jewels[ji++]);
      if (!pq.isEmpty()) sum += pq.poll().V;
    }
    System.out.println(sum);
  }
}

class jewel {
  int M, V;
  public jewel (int M, int V){
    this.M = M;
    this.V = V;
  }

  int getM() {return M;}
  int getV() {return V;}
}