package com.juvenxu.mvnbook;

/**
 * Created by zhangheng on 2017/11/4.
 * 练习static方法的用法
 * http://www.cnblogs.com/dolphin0520/p/3799052.html
 */
public class thisTest {
    public static void main(String[] args)
    {
        //static 方法就是没有this的方法。在static方法内部不能调用非静态方法，反过来是可以的。
        //可以在没有创建任何对象的前提下，仅仅通过类本身来调用static方法，这实际上真是static方法的主要用途。
        //很显然，被static 关键字修饰的方法或变量不需要依赖于对象来进行访问，只要类被加载，姐可以通过类名去进行访问
        //static 方法一般称作静态方法，由于静态方法不依赖于任何对象就可以进行访问，
        //静态变量和非静态变量的区别：静态变量被所有对象所共享
        //staitc 代码块 用来形成静态代码块以优化程序性能。static 块可以置于类中任何地方，雷子可以有
        //多个static块，在类被加载的时候，会按照static 块的顺序来执行每个static块，并且会执行一次。（只会在类加载的时候执行一次，）
        // 很多时候，会将一些只需要进行一次的初始化操作都放在 static代码中进行



    }
}
