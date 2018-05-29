package com.DanLiModel;

/**
 * Created by zhangheng on 2017/12/9.
 */
//懒汉模式  用  静态内部类  既实现了线程安全，又避免了同步带来的性能影响。
public class lanhan_jingtai {
    private  static class LazyHolder{
        private  static  final  lanhan_jingtai instance = new lanhan_jingtai();

    }
    private  lanhan_jingtai(){}
    public  static  final lanhan_jingtai getInstace(){
        return LazyHolder.instance;
    }
}
