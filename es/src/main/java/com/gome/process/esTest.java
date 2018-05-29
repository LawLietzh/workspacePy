package com.gome.process;

import org.elasticsearch.action.search.SearchRequestBuilder;
import org.elasticsearch.action.search.SearchType;
import org.elasticsearch.client.Client;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.sort.SortOrder;

import java.net.InetAddress;
//import org.elasticsearch.common.settings.ImmutableSettings;
//import org.elasticsearch.common.settings.ImmutableSettings;

/**
 * Created by zhangheng on 2017/12/7.
 */
public class esTest
{
    public static void add_chatbot_v1() {
        try {
            /* 创建客户端 */
            // client startup                                                                                            设置集群名称
            Settings settings= Settings.settingsBuilder().put("client.transport.sniff", true).put("cluster.name","ai-application").build();
            //获取client 实例，连接本地9300 端口，client和集群通过9300 端口通信
            Client client = TransportClient.builder().settings(settings).build()
                    .addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("10.112.167.19"), 9300));

            SearchRequestBuilder srb =client.prepareSearch("zongkun").setTypes("chats").setSearchType(SearchType.DFS_QUERY_THEN_FETCH)
                    .setQuery(QueryBuilders.matchAllQuery()).setFrom(0).setSize(10)
                    //.addAggregation(question)//聚合（类似于sql 中的函数以及group by）
                    .addSort("question", SortOrder.DESC);//按照一个字段排序
            //显示所有记录
           // QueryBuilders qb1 = QueryBuilders.matchAllQuery();

        } catch (Exception e) {
            e.printStackTrace();
        }







    }
}
