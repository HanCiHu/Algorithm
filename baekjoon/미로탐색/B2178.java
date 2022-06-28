import java.io.*;
import java.util.*;

public class B2178 {
  static int map[][];
  static int N;
  static int M;

  static int dx[] = {0,0, 1, -1};
  static int dy[] = {1, -1, 0,0};
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());

    N = Integer.parseInt(st.nextToken());
    M = Integer.parseInt(st.nextToken());

    map = new int[N][M];

    for (int i = 0; i < N; i++){
      String s = br.readLine();
      for (int j = 0; j < M; j++){
        map[i][j] = s.charAt(j) - '0';
      }
    }

    Queue<Location> q = new LinkedList<>();
    q.add(new Location(0, 0));

    while (!q.isEmpty()){
      Location l = q.poll();

      if (l.x == M - 1 && l.y == N - 1){
        System.out.println(map[l.y][l.x]);
        break;
      }

      for (int i = 0; i < 4; i++){
        int nx = l.x + dx[i];
        int ny = l.y + dy[i];

        if (nx >= 0 && ny >=0 && nx < M && ny < N && map[ny][nx] == 1){
          q.add(new Location(nx, ny));
          map[ny][nx] = map[l.y][l.x] + 1;
        }
      }
    }
  }
}

class Location {
  int x;
  int y;

  public Location(int x, int y){
    this.x = x;
    this.y = y;
  }
}
