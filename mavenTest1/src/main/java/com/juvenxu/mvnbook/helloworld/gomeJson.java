package com.juvenxu.mvnbook.helloworld;

import com.alibaba.fastjson.JSONObject;

import java.util.Map;

/**
 * Created by zhangheng on 2018/1/17.
 */
public class gomeJson
{
    public static void main(String[] args) {


        //String s = "{   \"answer_type\" : \"faq\",   \"confidence\" : \"44.6355\",   \"cost_ms\" : 321,   \"info\" : [      {         \"answer\" : \"如何登录票据理财，请<a href=\\\"http://piaoju.gome.com.cn/?intcmp=jridx-jrhead-13\\\"><strong><span style=\\\"color: rgb(51,102,255);\\\">点击这里</span></strong></a>进入票据理财哦~\",         \"class1Id\" : 100047,         \"class1Name\" : \"票据理财\",         \"class2Id\" : 100048,         \"class2Name\" : \"投资\",         \"id\" : 341,         \"knowledgeStatus\" : 1,         \"link\" : \"\",         \"question\" : \"怎样进入票据理财\",         \"relate\" : [],         \"validBeginTime\" : \"2017-11-01 14:23:07\",         \"validEndTime\" : \"2037-11-01 14:23:07\"      },      {         \"answer\" : \"投注协议仔细看~请<a href=\\\"http://help.gome.com.cn/question/5644.html\\\"><strong><span style=\\\"color: rgb(51,102,255);\\\">点击这里</span></strong></a>哦~\",         \"class1Id\" : 100076,         \"class1Name\" : \"国美彩票\",         \"class2Id\" : 100083,         \"class2Name\" : \"彩票协议\",         \"id\" : 538,         \"knowledgeStatus\" : 1,         \"link\" : \"\",         \"question\" : \"彩票电话投注委托协议\",         \"relate\" : [],         \"validBeginTime\" : \"2017-11-01 14:23:00\",         \"validEndTime\" : \"2037-11-01 14:23:00\"      },      {         \"answer\" : \"亲，申请企业采购请<a href=\\\"http://enterprise.gome.com.cn/liuyan/\\\"><strong><span style=\\\"color: rgb(51,102,255);\\\">点击这里</span></strong></a>哦~\",         \"class1Id\" : 100101,         \"class1Name\" : \"企业采购\",         \"class2Id\" : 100102,         \"class2Name\" : \"采购\",         \"id\" : 634,         \"knowledgeStatus\" : 1,         \"link\" : \"\",         \"question\" : \"如何申请企业采购？\",         \"relate\" : [],         \"validBeginTime\" : \"2017-11-01 14:22:58\",         \"validEndTime\" : \"2037-11-01 14:22:58\"      }   ],   \"msg\" : \"success\",   \"status\" : 0,   \"type\" : 300}";
        String s ="{\"code\":0,\"message\":\"\",\"body\":[{\"orderId\":\"19014534185\",\"shippingGroupId\":\"2569727475\",\"realPayAmount\":990.0,\"shippingResumes\":[{\"stateTime\":1515150865102,\"stateDesc\":\"订单已出库\",\"state\":\"EX3\"},{\"stateTime\":1515150862739,\"stateDesc\":\"订单已出库\",\"state\":\"EX2\"}],\"stateUpdateTime\":1515150865102,\"state\":\"DELIVERY\",\"commerceItems\":[{\"imgs\":[\"//gfs17.atguat.net.cn/T1ktJTBTZs1RCvBVdK_80.jpg\"],\"orderId\":\"19014534185\",\"salePrice\":1000.0,\"brandId\":null,\"num\":1,\"name\":\"业务测试专用冰箱Ling-O1\",\"shippingGroupId\":\"2569727475\",\"skuNo\":\"100253719\",\"type\":1,\"categoryId\":null,\"skuId\":\"1000088365\"}]},{\"orderId\":\"19103460347\",\"shippingGroupId\":\"2569661642\",\"realPayAmount\":2000.0,\"shippingResumes\":[{\"stateTime\":1515150780847,\"stateDesc\":\"订单已出库\",\"state\":\"EX3\"},{\"stateTime\":1515150780317,\"stateDesc\":\"订单已出库\",\"state\":\"EX2\"}],\"stateUpdateTime\":1515150780847,\"state\":\"DELIVERY\",\"commerceItems\":[{\"imgs\":[\"//gfs17.atguat.net.cn/T1QXETBKbv1RCvBVdK_80.jpg\"],\"orderId\":\"19103460347\",\"salePrice\":2000.0,\"brandId\":\"guomeidianqi\",\"num\":1,\"name\":\"电商测试8-更改\",\"shippingGroupId\":\"2569661642\",\"skuNo\":\"100253497\",\"type\":1,\"categoryId\":null,\"skuId\":\"1000078147\"},{\"imgs\":[\"//gfs17.atguat.net.cn/T1QXETBKbv1RCvBVdK_80.jpg\"],\"orderId\":\"19103460347\",\"salePrice\":null,\"brandId\":\"guomeidianqi\",\"num\":3,\"name\":\"电商测试8-更改\",\"shippingGroupId\":\"2569661642\",\"skuNo\":\"100253497\",\"type\":2,\"categoryId\":null,\"skuId\":\"1000078147\"},{\"imgs\":[\"//gfs17.atguat.net.cn/T1QXETBKbv1RCvBVdK_80.jpg\"],\"orderId\":\"19103460347\",\"salePrice\":null,\"brandId\":\"guomeidianqi\",\"num\":1,\"name\":\"电商测试8-更改\",\"shippingGroupId\":\"2569661642\",\"skuNo\":\"100253497\",\"type\":2,\"categoryId\":null,\"skuId\":\"1000078147\"}]},{\"orderId\":\"19014474485\",\"shippingGroupId\":\"2569673965\",\"realPayAmount\":1233.0,\"shippingResumes\":[{\"stateTime\":1513160147171,\"stateDesc\":\"您的商品已由北京国美北京配送中心22发出，此单将由国美快递为您派送 ，已分派配送员，请您准备收货，配送员姓名:刘胜利，联系方式:18731369578\",\"state\":\"AC\"},{\"stateTime\":1507538866931,\"stateDesc\":\"订单已出库\",\"state\":\"EX0\"}],\"stateUpdateTime\":1513160147171,\"state\":\"DELIVERY\",\"commerceItems\":[{\"imgs\":[\"//gfs17.atguat.net.cn/T1TtETBmZg1RCvBVdK_80.jpg\"],\"orderId\":\"19014474485\",\"salePrice\":1234.0,\"brandId\":null,\"num\":1,\"name\":\"业务测试专用冰箱Ling-O1\",\"shippingGroupId\":\"2569673965\",\"skuNo\":\"100253719\",\"type\":1,\"categoryId\":null,\"skuId\":\"1000088365\"}]}]}";

        Map<String, Object> map = JSONObject.parseObject(s);
        String code = map.get("code").toString();
        String body = map.get("body").toString();
        System.out.println(code);
        System.out.println(body);
        System.out.println("*********");
        Map<String, Object> map1 = JSONObject.parseObject(body);



       /* //System.out.println(all_information);
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




        }*/
    }
}
