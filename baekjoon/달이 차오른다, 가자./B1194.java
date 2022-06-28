import java.io.*;
import java.util.*;

public class B1194 {
  static char map[][];
  static boolean visit[][][];

  static int [] dx = {0, 0, 1, -1};
  static int [] dy = {1, -1, 0, 0};
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    map = new char[N][M];
    visit = new boolean[N][M][1 << 6];

    Queue<Node> q = new LinkedList<>();

    for (int i = 0; i < N; i++){
      map[i] = br.readLine().toCharArray();
      for (int j = 0; j < M; j++){
        if (map[i][j] == '0'){
          q.add(new Node(j, i, 0, 0));
        }
      }
    }
    while (!q.isEmpty()){
      Node tempNode = q.poll();

      if (map[tempNode.y][tempNode.x] == '1'){
        System.out.println(tempNode.cnt);
        return ;
      }

      for (int i = 0 ;i < 4; i++){
        int nx = tempNode.x + dx[i];
        int ny = tempNode.y + dy[i];

        int key = tempNode.key;
        int cnt = tempNode.cnt;

        if (nx >= 0 && ny >= 0 && nx < M && ny < N){
          if (!visit[ny][nx][key]){
            if (map[ny][nx] == '.' || map[ny][nx] == '1' || map[ny][nx] == '0'){
              q.add(new Node(nx, ny, key, cnt + 1));
              visit[ny][nx][key] = true;
            }
            else if (map[ny][nx] >= 'a' && map[ny][nx] <= 'f'){
              int tmpKey = key | (1 << (map[ny][nx] - 'a'));
              q.add(new Node(nx, ny, tmpKey, cnt + 1));
              visit[ny][nx][tmpKey] = true;
            }
            else if (map[ny][nx] >= 'A' && map[ny][nx] <= 'F'){
              int tmpKey = 1 << (map[ny][nx] - 'A');
              if ((key & tmpKey) > 0){
                q.add(new Node(nx, ny, key, cnt + 1));
                visit[ny][nx][key] = true;
              }
            }
          }
        }
      }
    }
    System.out.println(-1);
  }
}

class Node {
  int x;
  int y;
  int key;
  int cnt;
  public Node (int x,int y,int key,int cnt){
    this.x = x;
    this.y = y;
    this.key = key;
    this.cnt = cnt;
  }
}
