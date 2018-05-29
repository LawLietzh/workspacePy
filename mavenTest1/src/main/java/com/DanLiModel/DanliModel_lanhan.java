package com.DanLiModel;

/**
 * Created by zhangheng on 2017/12/9.
 */
// 懒汉模式  没有考虑线程安全
public class DanliModel_lanhan {
    public static int t  = 0;
    // 通过构造方法 限定为private 避免了类在外部被实例化 ，在同一个虚拟机 范围内，danLi_Test 的唯一实例只能 通过
    //getInstance() 方法访问
    private  DanliModel_lanhan(){}
    private static  DanliModel_lanhan single = null;
    // 静态工厂方法
    public static DanliModel_lanhan getInstance(){
        if(single == null){
            single = new DanliModel_lanhan();
        }
        return single;
    }
    //解决 线程不安全  1  在getInstance 方法上加上 同步

  /* public static   synchronized  DanliModel_lanhan  getInstance1(){
        if(single == null){
            single = new DanliModel_lanhan();
            System.out.println(" jianli  ");
        }
        return single;
    }*/

  //解决 线程不安全  2   静态内部类
  /*public class Singleton {
      private static class LazyHolder {
          private static final Singleton INSTANCE = new Singleton();
      }
      private Singleton (){}
      public static final Singleton getInstance() {
          return LazyHolder.INSTANCE;
      }
  }*/

    public static void main(String[] args)
    {

       // getInstance1();
       getInstance();

       getInstance();
        System.out.println(t);
    }
}
