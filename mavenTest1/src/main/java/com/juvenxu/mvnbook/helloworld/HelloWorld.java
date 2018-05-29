package com.juvenxu.mvnbook.helloworld;

/**
 * Created by zhangheng on 2017/11/2.
 * 关于该java代码有两点需要注意，首先，在绝大多数情况下，应该把主项目代码放到src/main/java目录下
 * 另外，java类的包名，要和pom中groupId artifactId 保持吻合，一般来说，项目中java类的包都应该基于项目的groupId
 * 和，artifactId ，这样更加清晰，更加符合逻辑，也跟方便搜索构建或者java类
 */
public class HelloWorld {
    public String sayHello()
    {
        return "Hello World";
    }
    public static void main(String[] args)
    {
        System.out.print(new HelloWorld().sayHello());
    }
}

