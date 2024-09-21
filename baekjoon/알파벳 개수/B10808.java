import java.util.*;

public class B10808 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String s = sc.next();
    int[] alphabetCount = new int[26];

    for (int i = 0; i < s.length(); i++) {
      alphabetCount[(int) s.charAt(i) - (int)'a']++;
    }

    for (int i = 0; i < alphabetCount.length; i++) {
      System.out.print(alphabetCount[i]);
      System.out.print(' ');
    }
  }
}