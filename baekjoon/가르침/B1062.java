import java.util.*;

public class B1062 {
  static int N,K;
  static String[] words;
  static boolean[] visited;
  static int selectedCount = 0;
  static int max = 0;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    N = Integer.parseInt(sc.next());
    K = Integer.parseInt(sc.next());

    words = new String[N];
    visited = new boolean[26];

    for (int i = 0; i < N; i++) words[i] = sc.next();

    max = countWords();
    for (int i = 0; i < 26; i++) {
      if (!visited[i]) dfs(i);
    }

    System.out.println(max);
  }

  static void dfs(int index){
//  1. 체크인
    visited[index] = true;
    selectedCount++;
//  2. 목적지인가? : selectedCnt == K 가 되면 목적지 도착
    if (selectedCount == K) max = Math.max(max, countWords());
    else {
//  3. 연결된 곳을 순회 : index + 1 에서 25 번째(알파벳 Z 까지..)
      for (int i = index + 1; i <= 25; i++){
//    4. 갈 수 있는가? : 방문 여부 (Visited)
//      5. 간다 : dfs 호출
        if (!visited[i]) dfs(i);
      }
    }
//  6. 체크아웃
    visited[index] = false;
    selectedCount--;
  }

  static int countWords(){
    int count = 0;
    for (int n = 0; n < N; n++){
      boolean isPossible = true;
      String word = words[n];
      for (int i = 0; i < word.length(); i++){
        if (!visited[word.charAt(i) - 'a']){
          isPossible = false;
          break;
        }
      }
      if (isPossible) count++;
    }

    return count;
  }
}
