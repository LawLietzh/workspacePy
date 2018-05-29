package com.juvenxu.mvnbook.helloworld;

import org.junit.Test;
import  com.juvenxu.mvnbook.helloworld.HelloWorld ;
/**
 * Created by zhangheng on 2017/11/4.
 * 测试类
 */
public class HelloWordTest {
    @Test
    public void testSayHello()
    {
        HelloWorld helloWord = new HelloWorld();
        String result = helloWord.sayHello();

        System.out.println("result:   "+result);
    }
}
