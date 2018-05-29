package com.juvenxu.mvnbook.gongzou;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Created by zhangheng on 2017/12/19.
 */

public class yuyinJson {
    public static final String pathJson = "E://数据资料//数据分析//yuying_string.txt";
    public static final String pathJson_jx = "E://数据资料//数据分析//wav//6.txt";
    public static void main(String[] args) throws IOException
    {
        //写
        FileOutputStream fos = new FileOutputStream(pathJson_jx);
        OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");

        //读取
        InputStreamReader read = new InputStreamReader(new FileInputStream(pathJson),"UTF-8");
        BufferedReader bufferedReader = new BufferedReader(read);
        String line = null;
        List<String> list = new ArrayList<String>();
        String  jsonString = "";
        while ((line = bufferedReader.readLine())!=null)
        {
            jsonString =  jsonString+line;
        }

        //解析
        List<Map<String, String>> mapList = JSON.parseObject(jsonString, new TypeReference<List<Map<String, String>>>() {});
        System.out.println(mapList.size());
        for (int i = 0; i < mapList.size(); i++) {

            for (String s1 : mapList.get(i).keySet()) {

                if (s1.equals("onebest") ) {
                    //System.out.println(s1 + "==>" + mapList.get(i).get(s1));
                    osw.write(mapList.get(i).get(s1));
                    osw.write("\r\n");
                    osw.flush();
                }
            }
        }

        bufferedReader.close();
        osw.close();
            System.out.println("===================================================");


    }
}
