package com.gome.process;


import org.elasticsearch.client.Client;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;

import java.net.InetSocketAddress;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


public class ESUtil {



	private static Client client = null;
	private static Settings settings = null;
	public static Set<String> categoryIds = new HashSet<String>(Arrays.asList(",", "?", "，","？","。", "!", "！",
			""));

	protected Set<String> getCategoryIds() {
		return categoryIds;
	}
	/**
	 * 建立连接
	 * @return
	 */
	public static Client getClient(){

        if(client==null) {
            try {
                //如果集群名是默认的elasticsearch没有改变，settings可以不哟红设置
				//1 ,通过setting对象 来指定集群配置信息  cluster 集群
				//                                    指定集群名称，                                 启动嗅探功能
                settings = Settings.builder().put("cluster.name", Config.clustername).put("client.transport.sniff", true).build();

                /*
                2,创建 客户端
                通过setting来创建，若不指定则默认链接的集群名为 elasticsearch
                 */
                InetSocketAddress isa = new InetSocketAddress(Config.esip, Config.esport);
                client = TransportClient.builder().settings(settings).build().addTransportAddress(new InetSocketTransportAddress(isa));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return client;
	}

	/**
	 * 建立连接
	 * @return
	 */
	public static void closeClient(){
		client.close();
	}

}
