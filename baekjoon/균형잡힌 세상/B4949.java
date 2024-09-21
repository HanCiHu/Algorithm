import java.io.*;
import java.util.*;

public class B4949 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String s = br.readLine();

    while (!s.equals(".")) {
      boolean flag = true;
      Stack<Character> stack = new Stack<>();
      for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == '[' || s.charAt(i) == '(') {
          stack.push(s.charAt(i));
        }
        else if (s.charAt(i) == ']') {
          if (stack.isEmpty() || stack.peek() != '[') {
            flag = false;
            break;
          }
          else  {
            stack.pop();
          }
        }
        else if (s.charAt(i) == ')') {
          if (stack.isEmpty() || stack.peek() != '(') {
            flag = false;
            break;
          }
          else  {
            stack.pop();
          }
        }
      }
      if (!stack.isEmpty()) flag = false;
      if (flag) {
        System.out.println("yes");
      } else {
        System.out.println("no");
      }
      s = br.readLine();
    };
  }
}
