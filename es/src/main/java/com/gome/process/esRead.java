package com.gome.process;
//import com.gome.process.Config;
import org.elasticsearch.action.search.SearchRequestBuilder;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.search.SearchType;
import org.elasticsearch.client.Client;
import org.elasticsearch.common.unit.TimeValue;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.SearchHits;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by zhangheng on 2017/12/4.
 * http://www.genshuixue.com/i-cxy/p/11589174
 */
public class esRead {
    private static SearchRequestBuilder builder = null;
    public static Client client = null;

    static {
        client = ESUtil.getClient();

        builder = client.prepareSearch(Config.esdatabase).setTypes(Config.estable);
    }

    /*
    查看集群信息
    注意我的集群结构是：

     */
    //TransportClient transportClient = null;

    // 读全量数据
    public static void main(String[] args) throws IOException
    {
        Set<String> set = new HashSet<String>();
        //写数据
        String path = "E://数据资料//数据分析//智能客服语料整理//esQuanliang.txt";
        FileOutputStream fos = new FileOutputStream(path);
        OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");
        int t = 0;
       // System.out.println(t);

        SearchResponse searchResponse = client.prepareSearch(Config.esdatabase).setTypes(Config.estable).setQuery(QueryBuilders.matchAllQuery()) //查询所有
                //.setQuery(QueryBuilders.matchQuery("name", "tom").operator(Operator.AND)) //根据tom分词查询name,默认or
                //.setQuery(QueryBuilders.multiMatchQuery("tom", "name", "age")) //指定查询的字段
                //.setQuery(QueryBuilders.queryString("name:to* AND age:[0 TO 19]")) //根据条件查询,支持通配符大于等于0小于等于19
                //.setQuery(QueryBuilders.termQuery("name", "tom"))//查询时不分词
                .setSize(1000)
                .setScroll(new TimeValue(6000))
                .setSearchType(SearchType.SCAN).execute().actionGet();
        String scrollid = searchResponse.getScrollId();
        while (true)
        {
                SearchResponse response2 = client.prepareSearchScroll(scrollid)
                        .setScroll(new TimeValue(6000)).execute().actionGet();
                SearchHits searchHit = response2.getHits();
                if (response2.getHits().getHits().length == 0)
                {
                    System.out.println("oh no=====");
                    break;
                }
                System.out.println("查询数量："+searchHit.getHits().length);
            for (SearchHit hit : searchHit.getHits())
            {
                t = t + 1;
                String classify = hit.getSource().get("classify").toString().trim();
                String question = hit.getSource().get("question").toString().trim();
                String answer = hit.getSource().get("answer").toString().trim();
                String line = classify + "\t" + question + "\t" + answer;
                System.out.println(line);
                if (!set.contains(line)) {
                    set.add(line);
                    osw.write(line);
                    osw.write("\n");
                    osw.flush();
                }

            }

            }
        System.out.println(t);
        System.out.println(set.size());
        }


       // osw.close();


    }



