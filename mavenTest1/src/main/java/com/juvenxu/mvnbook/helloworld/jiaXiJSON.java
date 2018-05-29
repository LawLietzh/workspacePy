package com.juvenxu.mvnbook.helloworld;
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.TypeReference;

import java.util.List;
import java.util.Map;

/**
 * Created by zhangheng on 2017/11/8.
 *
 * 测试 fastJosn 的使用
 *
 */
public class jiaXiJSON {
    public static void main(String[] args) {
        String jsonString2 = "[{\"param5\":\"value5\",\"param3\":\"value3\",\"param4\":\"value4\",\"param1\":\"value1\",\"param2\":\"value2\"}," +
                              "{\"p1\":\"v1\",\"p2\":\"v2\",\"p3\":\"v3\",\"p4\":\"v4\",\"p5\":\"v5\"}]";
        System.out.println(jsonString2);
        List<Map<String, String>> mapList = JSON.parseObject(jsonString2, new TypeReference<List<Map<String, String>>>() {});
        System.out.println(mapList.size());
        for (Map<String, String> stringObjectMap : mapList) {
            System.out.println(stringObjectMap.size());
            for (String s : stringObjectMap.keySet()) {
                System.out.println(s + "==>" + stringObjectMap.get(s));
            }
        }
        System.out.println("===================================================");


        String s = "{   \"answer_type\" : \"faq\",   \"confidence\" : \"44.6355\",   \"cost_ms\" : 321,   \"info\" : [      {         \"answer\" : \"如何登录票据理财，请<a href=\\\"http://piaoju.gome.com.cn/?intcmp=jridx-jrhead-13\\\"><strong><span style=\\\"color: rgb(51,102,255);\\\">点击这里</span></strong></a>进入票据理财哦~\",         \"class1Id\" : 100047,         \"class1Name\" : \"票据理财\",         \"class2Id\" : 100048,         \"class2Name\" : \"投资\",         \"id\" : 341,         \"knowledgeStatus\" : 1,         \"link\" : \"\",         \"question\" : \"怎样进入票据理财\",         \"relate\" : [],         \"validBeginTime\" : \"2017-11-01 14:23:07\",         \"validEndTime\" : \"2037-11-01 14:23:07\"      },      {         \"answer\" : \"投注协议仔细看~请<a href=\\\"http://help.gome.com.cn/question/5644.html\\\"><strong><span style=\\\"color: rgb(51,102,255);\\\">点击这里</span></strong></a>哦~\",         \"class1Id\" : 100076,         \"class1Name\" : \"国美彩票\",         \"class2Id\" : 100083,         \"class2Name\" : \"彩票协议\",         \"id\" : 538,         \"knowledgeStatus\" : 1,         \"link\" : \"\",         \"question\" : \"彩票电话投注委托协议\",         \"relate\" : [],         \"validBeginTime\" : \"2017-11-01 14:23:00\",         \"validEndTime\" : \"2037-11-01 14:23:00\"      },      {         \"answer\" : \"亲，申请企业采购请<a href=\\\"http://enterprise.gome.com.cn/liuyan/\\\"><strong><span style=\\\"color: rgb(51,102,255);\\\">点击这里</span></strong></a>哦~\",         \"class1Id\" : 100101,         \"class1Name\" : \"企业采购\",         \"class2Id\" : 100102,         \"class2Name\" : \"采购\",         \"id\" : 634,         \"knowledgeStatus\" : 1,         \"link\" : \"\",         \"question\" : \"如何申请企业采购？\",         \"relate\" : [],         \"validBeginTime\" : \"2017-11-01 14:22:58\",         \"validEndTime\" : \"2037-11-01 14:22:58\"      }   ],   \"msg\" : \"success\",   \"status\" : 0,   \"type\" : 300}";


        Map<String, Object> map = JSONObject.parseObject(s);
        String all_information = map.get("info").toString();
        //System.out.println(all_information);
        List<Map<String, String>> mapList2 = JSONObject.parseObject(all_information, new TypeReference<List<Map<String, String>>>() {});
        System.out.println(mapList2.size());
        for (int i = 0; i < mapList2.size(); i++) {

            System.out.println(mapList2.get(i).size());

            for (String s1 : mapList2.get(i).keySet()) {

                if (s1.equals("question") || s1.equals("answer")) {
                    System.out.println(s1 + "==>" + mapList2.get(i).get(s1));
                }
            }

            //System.out.println(question+"     "+answer);

                // 解析 某一个字段
            String answer_type = map.get("answer_type").toString();
            System.out.println("  answer_type  : "+answer_type);




        }
    }
}