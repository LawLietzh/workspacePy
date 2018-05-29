package fenci;

/**
 * Created by zhangheng on 2017/12/5.
 */
import org.ansj.domain.Term;
import org.ansj.library.DicLibrary;
import org.ansj.splitWord.analysis.ToAnalysis;

import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
public class ansj_test
{
    // 用户词典
    private static Set<String> set = new HashSet<String>();
//    private static final String MAIN_DICT = "C://Users//zhangheng//Desktop//lixiang//lixiang1023//key_word3.txt";
    private static final String MAIN_DICT = "./src/main/resources/key_word3.txt";
    public static void main(String[] args)throws Exception
    {
        //读字典
        InputStreamReader reads1 = new InputStreamReader(new FileInputStream(MAIN_DICT),"UTF-8");
        BufferedReader bufferedReaders1 = new BufferedReader(reads1);
        String line= null;
        Set<String> set = new HashSet<String>();
        int s1 = 0;
        while((line = bufferedReaders1.readLine() ) != null)
        {
            if(!set.contains(line))
            {
                set.add(line);
            }
        }

        for (String str : set) {
            DicLibrary.insert("dic", str);
        }

        //写
        String pathX = "C://Users//zhangheng//Desktop//lixiang//lixiang1023//hebing_fenci.txt";
        FileOutputStream fos = new FileOutputStream(pathX);
        OutputStreamWriter osw = new OutputStreamWriter(fos, "UTF-8");


        //读
        String path = "C://Users//zhangheng//Desktop//lixiang//lixiang1023//hebing.txt";
        InputStreamReader read = new InputStreamReader(new FileInputStream(path),"UTF-8");
        BufferedReader bufferedReader = new BufferedReader(read);
        String lineH= null;
        List<String> list = new ArrayList<String>();
        int s = 0;
        while((lineH = bufferedReader.readLine() ) != null)
        {
            String[] linearray = lineH.split("\t");
            String key =linearray[1];
            String in = "";
            List<Term> term = ToAnalysis.parse(key).getTerms();
            for(Term word : term){
                String wc = word.getName();
                in += wc + " ";
            }
            in = in.trim();

            String str = linearray[0]+"\t"+in +"\t"+linearray[2];
            osw.write(str);
            osw.write("\r\n");
            osw.flush();


        }


        bufferedReader.close();
        osw.close();



    }

}
