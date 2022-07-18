import java.util.*;

public class B3055 {
  static String[] map;
  static int[][] visited;
  static Queue <Node>q;
  static int R,C;
  static int[] dx = {1,-1, 0,0};
  static int[] dy = {0,0,1,-1};
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    R = Integer.parseInt(sc.next());
    C = Integer.parseInt(sc.next());

    map = new String[R];
    visited = new int[R][C];
    q = new LinkedList<Node>();

    for (int i = 0 ;i < R; i++){
      String line = sc.next();
      for (int j = 0 ; j < C; j++) {
        if (j == 0) map[i] = "";
        map[i] += line.charAt(j);
        if (line.charAt(j) == '*') q.add(new Node(j,i, '*'));
        visited[i][j] = 0;
      }
    }

    for (int y = 0; y < R; y++){
      for (int x = 0; x < C; x++){
        if (map[y].charAt(x) == 'S') q.add(new Node(x, y, 'S'));
      }
    }
    if (!bfs()) System.out.println("KAKTUS");
  }

  static boolean bfs(){
    while (!q.isEmpty()){
      Node n = q.poll();

      if (n.type == 'S' && map[n.y].charAt(n.x) == 'D') {
        System.out.println(visited[n.y][n.x]);
        return true;
      }

      for (int i = 0; i < 4; i++){
        int nx = n.x + dx[i];
        int ny = n.y + dy[i];

        if (nx >= 0 && ny >= 0 && nx < C && ny < R && visited[ny][nx] == 0){
          if (n.type == '*' && map[ny].charAt(nx) == '.'){
            q.add(new Node(nx, ny, n.type));
            visited[ny][nx] = visited[n.y][n.x] + 1;
          }
          else if (n.type == 'S' && (map[ny].charAt(nx) == '.' || map[ny].charAt(nx) == 'D')){
            q.add(new Node(nx, ny, n.type));
            visited[ny][nx] = visited[n.y][n.x] + 1;
          }
        }
      }
    }
    return false;
  }
}

class Node {
  int x,y;
  char type;
  public Node(int x, int y, char type){
    this.x = x;
    this.y = y;
    this.type = type;
  }
}