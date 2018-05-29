package com.juvenxu.mvnbook.helloworld;

import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.TypeReference;
import net.sf.json.JSONArray;
import net.sf.json.JSONObject;
import java.util.Map;
import java.util.HashMap;

import com.alibaba.fastjson.JSON;
/**
 * Created by zhangheng on 2017/11/15.
 * 练习jsonlib的使用，构造 和解析 json数据的方法示例
 * http://blog.csdn.net/hechenghai/article/details/45842717
 */
public class JsonLib {
    public static void  main(String[] str)
    {
        //json格式数据解析对象
        JSONObject jo = new JSONObject();


        List list = new ArrayList();
        list.add("first");
        list.add("second");
        //List集合转换成json 方法
        JSONArray jsonArray2 = JSONArray.fromObject( list );
        System.out.println(jsonArray2);//  输出：["first","second"]

        // Map 集合转换成 json

        Map map = new HashMap();
        map.put("name", "json");
        map.put("bool", Boolean.TRUE);
        map.put("int", new Integer(1));
        map.put("arr", new String[] { "a", "b" });
        map.put("func", "function(i){ return this.arr[i]; }");
        JSONObject json = JSONObject.fromObject(map);
        System.out.println(json);//{"arr":["a","b"],"bool":true,"func":function(i){ return this.arr[i]; },"name":"json","int":1}

        // 数组转换成json
        boolean[] boolArray = new boolean[] { true, false, true };
        JSONArray jsonArray1 = JSONArray.fromObject(boolArray);

      // 构造Json数据，包括一个map和一个Employee对象
        jo.put("map", json);
        jo.put("array", jsonArray1);
        jo.put("list", jsonArray2);
        System.out.println("\n最终构造的JSON数据格式：");
        System.out.println(jo.toString());
        System.out.println("===================================================");
        String ddd = "["+jo.toString()+"]";
        System.out.println(ddd);
        List<Map<String, String>> mapList = JSON.parseObject(ddd, new TypeReference<List<Map<String, String>>>() {});
        for (Map<String, String> stringObjectMap : mapList) {
            for (String s : stringObjectMap.keySet()) {
                System.out.println(s + "==>" + stringObjectMap.get(s));
            }
        }
        System.out.println("===================================================");
        //String  strjson = "{"map":{"arr":["a","b"],"bool":true,"func":function(i){ return this.arr[i]; },"name":"json","int":1},"array":[true,false,true],"list":["first","second"]}";



        /*
        解析json 数据
         */
        JSONObject jb = JSONObject.fromObject(jo.toString());
        //解析map
        JSONObject ja = jb.getJSONObject("map");

        for (Object k:ja.keySet()){
            Object v = ja.get(k);
            System.out.println("k:"+k+"     v:"+v);
        }





    }
}
