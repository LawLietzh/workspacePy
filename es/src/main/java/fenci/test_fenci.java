package fenci;

import org.ansj.domain.Term;
import org.ansj.library.DicLibrary;
import org.ansj.splitWord.analysis.ToAnalysis;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by zhangheng on 2017/12/19.
 */
public class test_fenci {
    // 用户词典
    private static Set<String> set = new HashSet<String>();
    //    private static final String MAIN_DICT = "C://Users//zhangheng//Desktop//lixiang//lixiang1023//key_word3.txt";
    private static final String MAIN_DICT = "./src/main/resources/key_word3.txt";

    //添加词典
    public static void cidian()throws Exception{
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
    }
    public static  void main(String[] args)throws Exception
    {
        cidian();
        String key = "我的国美美豆";
        String in = "";

        List<Term> term = ToAnalysis.parse(key).getTerms();

        for(Term word : term){
            String wc = word.getName();
            in += wc + " ";
        }
        in = in.trim();
        System.out.println(in);
    }


}
