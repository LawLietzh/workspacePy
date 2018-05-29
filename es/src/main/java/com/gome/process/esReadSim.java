package com.gome.process;

import org.elasticsearch.action.search.SearchRequestBuilder;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.Client;
import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.index.query.QueryStringQueryBuilder;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.SearchHits;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.*;

/**
 * Created by zhangheng on 2018/1/11.
 */
public class esReadSim {
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
    public static void main(String[] args) throws IOException {
        Set<String> set = new HashSet<String>();
        //写数据
        String path = "E://数据资料//数据分析//智能客服语料整理//esSHIyuan.txt";
        FileOutputStream fos = new FileOutputStream(path);
        OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");
        int t = 0;

        String in  = "网页游戏 已 付款 为什么 还 是 显示 “ 等待付款 ” ";
        /*

            这是布尔查询  ，should  和 must的用法
            must :: 多个查询条件的完全匹配,相当于 and。
            must_not :: 多个查询条件的相反匹配，相当于 not。
            should :: 至少有一个查询条件匹配, 相当于 or。
            QueryStringQueryBuilder(0)  在es 中，通过输入查询数据，获得搜索结果，我们一般用QueryStringQueryBuilder()
            eg:  QueryStringQueryBuilder  queryBuilder = new QueryStringQueryBuilder(content); //content 为要查询的数据
            // analyzer 为ik分词，keywords 通过ik 进行分词    查询的字段位 title 和 content
            quweyBuilder.analyzer("ik").field("title").field("content")




         */
        BoolQueryBuilder qb = QueryBuilders.boolQuery().should(new QueryStringQueryBuilder(in).field("question")).should(QueryBuilders.termQuery("flag", "1"));
       // BoolQueryBuilder qb = QueryBuilders.boolQuery().should(new QueryStringQueryBuilder(in).field("question"));
        builder.setQuery(qb);
        SearchResponse response = builder.execute().actionGet();
        //
        SearchHits hits = response.getHits();
        //存储 从es中搜索的答案 和问题
        Map<String, String> map = new HashMap<String, String>();
        Map<String, Double> que_score = new TreeMap<String, Double>();
        //定义从es 中搜出来的 相似问题的 列表
        List<String> similar = new ArrayList<String>();

        if (hits.totalHits() > 0) {
            for (SearchHit hit : hits) {
                //question 是从es 中搜索到的相似问题
                String question = hit.getSource().get("question").toString();
                String ans = hit.getSource().get("answer").toString();

                question = question.trim();
                float score = hit.getScore();

                if (score > 2.0) {

                    System.out.println(""+score+"    question:      " + question + "    " + "ans:     " + ans);
                }


                // System.out.println(t);

       /* SearchResponse searchResponse = client.prepareSearch(Config.esdatabase).setTypes(Config.estable).setQuery(QueryBuilders.matchAllQuery()) //查询所有
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
        System.out.println(set.size());*/
            }


            // osw.close();


        }
    }
}