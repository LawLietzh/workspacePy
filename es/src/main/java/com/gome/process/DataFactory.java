package com.gome.process;
/**
 * Created by lixiang-ds3 on 2016/12/9.
 */
import com.huaban.analysis.jieba.JiebaSegmenter;
import com.huaban.analysis.jieba.SegToken;

import java.io.*;
import java.util.*;

public class DataFactory {

    private static Map<String, String> map = new HashMap<String, String>();
    private static DataFactory singleton;
    //
    private static final String MAIN_DICT = "./src/main/resources/12.txt";
    static JiebaSegmenter segmenter = new JiebaSegmenter();

    private DataFactory()throws Exception {
        this.loadDict();
    }


    public static DataFactory getInstance()throws Exception {
        if (singleton == null) {
            synchronized (DataFactory.class) {
                if (singleton == null) {
                    singleton = new DataFactory();
                    return singleton;
                }
            }
        }
        return singleton;
    }

    public void loadDict()throws Exception {

        InputStreamReader reads1 = new InputStreamReader(new FileInputStream(MAIN_DICT),"UTF-8");
        BufferedReader bufferedReaders1 = new BufferedReader(reads1);
        String line= null;
        Set<String> set = new HashSet<String>();
        String in;
        while((line = bufferedReaders1.readLine() ) != null)
        {
            System.out.println("line:"+line);
            line = line.trim();
            String[] info = line.split("\t");
           // System.out.println(info[0]+"    "+info[1]);
            String key = info[0];
            try {
                in ="";

                key = key.trim();
                List<SegToken> seg = segmenter.process(key, JiebaSegmenter.SegMode.SEARCH);

                for (SegToken segToken : seg) {
                    in += segToken.word.getToken() + " ";
                }

            }catch(Exception e){
                continue;
            }

            System.out.println(in+"    "+info[1].trim());
                map.put(in, info[1].trim());

        }

    }

    public static List<String> getInitJsonData_pc() {
        List<String> list = new ArrayList<String>();
        InputStream inputStream = null;
        InputStreamReader inputReader = null;
        BufferedReader bufferReader = null;

        try {
            inputStream = new FileInputStream("D:\\李响\\key_word\\hebing20171016_segShiyan.txt");
            inputReader = new InputStreamReader(inputStream, "utf8");
            bufferReader = new BufferedReader(inputReader);
            String line = "";

            while ((line = bufferReader.readLine()) != null) {
                line = line.trim();
                String[] output = line.split("\t");
                String cat = output[0];
                String question = output[1];
                String ans = output[2];

//                String in = ToAnalysis.parse(question).toStringWithOutNature(" ");
//                in = in.trim();

//                System.out.println(question);
                List list1 = new ArrayList();
                list1.add(cat);
                list1.add(question);
                list1.add(ans);
                String data = JsonUtil.model2Json_pc(list1);
                list.add(data);
            }
        }catch(IOException e){
            e.printStackTrace();
        }finally{
            try {
                if (bufferReader != null) {
                    bufferReader.close();
                }
                if (inputReader != null) {
                    inputReader.close();
                }
                if (inputStream != null) {
                    inputStream.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return list;
    }


    public static List<String> getInitJsonData()throws Exception {
        /*System.out.println("看看json：  ");
        List<String> list = new ArrayList<String>();
        DataFactory.getInstance();

            int m = 1;
            String data = "";

                data = JsonUtil.model2Json(new Blog(m, "我就试试", "试试吧", "1"));
                System.out.println("看看json：  "+data);

            list.add(data);

        return list;*/
        List<String> list = new ArrayList<String>();
        DataFactory.getInstance();
        for(Map.Entry<String, String> entry : map.entrySet()) {
            int m = 1;
            String data = "";
            try {
               data = JsonUtil.model2Json(new Blog(m, entry.getKey(), entry.getValue(), "1"));
              System.out.println("看看json：  "+data);
            }catch(Exception e){
                continue;
            }
            list.add(data);
        }
        return list;

    }





    public static void main(String[] args)throws Exception
    {
        getInitJsonData();


    }
}