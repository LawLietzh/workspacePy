package com.DanLiModel;

/**
 * Created by zhangheng on 2017/12/9.
 *
 * java的单例模式，这里主要介绍三种:  懒汉式单例，恶汉式单例 和 登记式单例
 * 单例模式 有一下特点：
 * 单例类 只能有一个实例
 * 单例类必须自己创建自己的唯一实例
 * 单例类 必须给所有其他对象提供这一实例
 *
 *单例模式确保某个类 只有一个实例，而且执行实例化 并向整个系统提供这个 实例。在计算机系统中，线程池、缓存
 * 日志对象，对话框，打印机显卡驱动等对象 常被设计成单例、这些应用都或多 或少 具有资源管理的功能。每台计算机可以有
 * 若干个打印机，但只有一个 printer Spooler 以避免两个打印作业同事输出到打印机中。
 *
 * 总之，选择单例模式就是为了避免不一致状态，避免政出多头。

 */
//懒汉模式
public class danLi_Test
{
    public static int t  = 0;
    // 通过构造方法 限定为private 避免了类在外部被实例化 ，在同一个虚拟机 范围内，danLi_Test 的唯一实例只能 通过
    //getInstance() 方法访问
    private  danLi_Test(){}
    private static  danLi_Test single = null;
    // 静态工厂方法
    public static danLi_Test getInstance(){
        if(single == null){
            single = new danLi_Test();
            t = t+1;
            System.out.println(" jianli  ");
        }
        return single;
    }
   public static void main(String[] args)
   {
       danLi_Test aa = new danLi_Test();
       /*getInstance();
       getInstance();

       getInstance();*/
       System.out.println(t);
   }
}
