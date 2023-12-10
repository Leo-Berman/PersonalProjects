public class JayceRewrite {
  public static int Power(int A, int B, int C){
    if(B!=0) return Power(A,B-1,A*C);
    return C;
  }
  public static Boolean isCubed(int A, int B){
    // Find the power
    // Declaring a bool
    int a = Power(B,3,1);
    Boolean MyBool = false;

    if(a>A){
      System.out.print("Power can't be found as ");
      System.out.print(B);
      System.out.println("^3 is greater than A");
      return MyBool;
    }

    // Check to see if the test number is the actual number if so return true if not eh
    if(A==a){
      System.out.print(B);
      System.out.print("^3 = ");
      System.out.print(a);
      System.out.print(" = ");
      System.out.println(A);
      MyBool = true;
    }

    // Otherwise, check the next number and return false?? Idk what you're trying to do
    if (a<A){
        System.out.print(B);
        System.out.print("^3 = ");
        System.out.print(a);
        System.out.print(" does not equal ");
        System.out.println(A);
        MyBool = isCubed(A,B+1);
    }
    return MyBool;
  }
  public static void main(String[] args){
    int a = 125;
    int b = 1;
    // Asking if 125 is 5^3?
    System.out.println(isCubed(a,b));
  }
}