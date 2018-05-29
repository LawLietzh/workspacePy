package com.gome.process; /**
 * Created by lixiang-ds3 on 2016/12/9.
 */

import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.client.Client;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.elasticsearch.*;
import java.net.InetAddress;
import java.util.List;
import org.elasticsearch.action.delete.DeleteRequest;
import org.elasticsearch.action.delete.DeleteResponse;
//import org.elasticsearch.common.settings.ImmutableSettings;
//import org.elasticsearch.common.settings.ImmutableSettings;
import org.elasticsearch.action.get.GetResponse;


public class ElasticSearchHandler {

    public static void add_chatbot_v1() {
        try {
            /* 创建客户端 */
            // client startup
            Settings settings= Settings.settingsBuilder().put("client.transport.sniff", true).put("cluster.name","ai-application").build();
            Client esclient = TransportClient.builder().settings(settings).build().addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("10.112.167.19"), 9300));
            int m = 0;

            List<String> jsonData = DataFactory.getInitJsonData();

            for (int i = 0; i < jsonData.size(); i++) {
                System.out.println(m++);
                IndexResponse response = esclient.prepareIndex("zongkun", "chats").setSource(jsonData.get(i)).get();
                if (response.isCreated()) {
                    System.out.println("创建成功!");
                }
            }
            esclient.close();
        } catch (Exception e) {
            e.printStackTrace();
        }



    }

    public static void delete_chatbot_v1(){
        // 删除 数据

        try {
            /* 创建客户端 */
            // client startup
            Settings settings = Settings.settingsBuilder().put("client.transport.sniff", true).put("cluster.name", "ai-application").build();
            Client esclient = TransportClient.builder().settings(settings).build().addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("10.112.167.19"), 9300));
            // 只是删除 zongkun  chats  中id 为 AWAv7BkxJT1kO0Yteizx  这条数据
            DeleteResponse response = esclient.prepareDelete("zongkun", "chats", "AWAv7BkxJT1kO0Yteizx")
                    .execute().actionGet();
            System.out.println(response.getId());
            //不能删除全部么


           // get 数据
            GetResponse responseGet = esclient.prepareGet("twitter", "tweet", "1")
                    .execute().actionGet();
            System.out.println("response.getId():"+response.getId());
            System.out.println("response.getSourceAsString():"+responseGet.getSourceAsString());



        } catch (Exception e) {
            e.printStackTrace();
        }








    }



    public static void main(String[] args){
        //add_chatbot_v1();
        delete_chatbot_v1();
       // add_chatbot_attr();
       //add_chatbot_product();
       // add_chatbot_final();

    }
}