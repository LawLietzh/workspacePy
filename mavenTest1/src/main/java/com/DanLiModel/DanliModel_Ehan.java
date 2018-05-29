package com.DanLiModel;

/**
 * Created by zhangheng on 2017/12/9.
 * 从名字上来说，饿汉和懒汉，
 饿汉就是类一旦加载，就把单例初始化完成，保证getInstance的时候，单例是已经存在的了，
 而懒汉比较懒，只有当调用getInstance的时候，才回去初始化这个单例。

 饿汉式天生就是线程安全的，可以直接用于多线程而不会出现问题，
 */
// 饿汉单例 ，在类 初始化时，已经自行实例化
public class DanliModel_Ehan {
    private DanliModel_Ehan(){}
    private  static  final DanliModel_Ehan single = new DanliModel_Ehan();
    //静态工作方法
    public  static  DanliModel_Ehan getInstace(){
        return  single;
    }

}
