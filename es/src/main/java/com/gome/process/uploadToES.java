package com.gome.process;
//向 es中打数据

import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.client.Client;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;

import java.net.InetAddress;
import java.util.List;

/**
 * Created by zhangheng on 2018/1/10.
 */
public class uploadToES {
    public static void add_chatbot_pc() {
        try {
            /* 创建客户端 */
            // client startup
            Settings settings= Settings.settingsBuilder().put("client.transport.sniff", true).put("cluster.name","ai-application").build();
            Client esclient = TransportClient.builder().settings(settings).build().addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("10.112.167.19"), 9300));
            int m = 0;

            List<String> jsonData = DataFactory.getInitJsonData_pc();

            for (int i = 0; i < jsonData.size(); i++) {
                System.out.println(m++);
                IndexResponse response = esclient.prepareIndex("chatbot_v2_1", "chats").setSource(jsonData.get(i)).get();
                if (response.isCreated()) {
                    System.out.println("创建成功!");
                }
            }
            esclient.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
    public static void main(String[] args)
    {

        //add_chatbot_pc();
    }
}
