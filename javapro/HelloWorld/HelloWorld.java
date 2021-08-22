package javapro.HelloWorld;

import java.util.Scanner;

public class HelloWorld {
    // public static void main(String[] args) {
    // final double PI = 3.14; // PI是一个常量
    // var sb = new StringBuilder();
    // int x = 10;
    // System.out.printf("HelloWorld, Sharm.\n");
    // System.out.println(x);
    // char a = 'A';
    // char zh = '中';
    // String str = "中国";
    // System.out.println(a);
    // System.out.println(zh);
    // System.out.println(str);
    // short s = 1234;
    // int i = 123;
    // int y = s + i; // s自动转型为int
    // short z = (short) (s + y); // 编译错误!
    // System.out.println(z);
    // }
    // 计算前N个自然数的和
    // public static void main(String[] args) {
    // int n = 100;
    // // TODO: sum = 1 + 2 + ... + n
    // int sum = 0;
    // for (int i = 1; i <= n; i++) {
    // sum += i;
    // }

    // System.out.println(sum);
    // System.out.println(sum == 5050 ? "测试通过" : "测试失败");
    // int n4 = (int) 1.2e20; // 2147483647
    // System.out.println(n4);
    // }
    public static void main(String[] args) {
        for (String arg : args) {
            if ("-version".equals(arg)) {
                System.out.println("v 1.0");
                break;
            }
        }
    }
}

class Persont {
    int age;
    public  void Persont(int age){
        this.age = age;
    }
    public void run() {
    }
}