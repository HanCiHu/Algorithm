import java.util.*;

public class B1759 {
  static int L, C, selectedCount = 0;
  static char[] pwKey;
  static String pw;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    L = Integer.parseInt(sc.next());
    C = Integer.parseInt(sc.next());

    pwKey = new char[C];
    pw = "";

    for (int i = 0 ; i < C; i++) pwKey[i] = sc.next().charAt(0);
    Arrays.sort(pwKey);

    for (int i = 0; i < C; i++) dfs(i);

  }
  
  static void dfs(int index){
    pw += pwKey[index];

    if (pw.length() == L) printPw(pw);
    for (int i = index + 1; i < C; i++){
      if (!pw.contains(""+pwKey[i])) {
        dfs(i);
      }
    }
    pw = pw.substring(0, pw.length() - 1);
  }

  static void printPw(String pw){
    int ja = 0;
    int mo = 0;
    for (int i = 0;i < pw.length(); i++){
      if (pw.charAt(i) == 'a' || pw.charAt(i) == 'i' || pw.charAt(i) == 'e' || pw.charAt(i) == 'o' || pw.charAt(i) == 'u') mo++;
      else ja++;
    }
    if (ja >= 2 && mo >= 1) System.out.println(pw);
  }
}
