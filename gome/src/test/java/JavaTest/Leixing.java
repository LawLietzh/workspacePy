package JavaTest;

import java.util.Arrays;

/**
 * Created by zhangheng on 2018/4/13.
 */
public class Leixing {
    public enum Color {
        RED, GREEN, BLANK, YELLOW
    }
    public enum  A {a,b ,c ,d}

    public static void main(String[] args)
    {
        double x = 9.97;
        System.out.println(Math.round(x));
        //Math.random() 返回一个 0 1 之间的小数
        System.out.println(Math.random()*3);
        int nx = (int)x;

        String str = "ahofodsf";
        //返回从 fromIndex 位置开始查找指定字符在字符串中第一次出现处的索引，如果此字符串中没有这样的字符，则返回 -1。
        int ss  = str.indexOf("asssss",1);
        System.out.println(ss);
        StringBuffer buffer = new StringBuffer();
        buffer.append("vv");
        buffer.append('a');
        buffer.append('a');
        System.out.println(buffer);
         //  输入
       /* Scanner in = new Scanner(System.in);
        System.out.println("what is you name");
        String name = in.nextLine();
        System.out.println(name);*/
        {int k = 0;}
        int k = 8;
        //数组的初始化
        int[] small = {2,3,4,5,6,9,0,1};
        int[] small1 = small; //两个数组  指向同一个地址
        small[0] = 10;
        System.out.println(small1[0]);
        Arrays.sort(small);

      /*   数组 拷贝，这个时候，就是把值 复制到 不同地址
      int[] copiedLucky = Arrays.copyOf(small1,small1.length);
        copiedLucky[0] = 100;
        System.out.println(copiedLucky[0]+"   "+small1[0]);
*/
        //二维数组  初始化
        int[][] ma = {{1,2},{3,4},{5,6}};
        System.out.println(Arrays.deepToString(ma));
        StringBuilder sb = new StringBuilder();
        sb.append("ss");
        sb.append("cc");
        System.out.print(sb);



    }
}
