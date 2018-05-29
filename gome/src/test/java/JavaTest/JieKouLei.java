package JavaTest;

import java.util.HashMap;
import java.util.Hashtable;

/**
 * Created by zhangheng on 2018/4/26.
 * 接口计数，这种技术 主要用来描述类具有什么功能，而不是给出每个功能的具体实现
 */
public class JieKouLei {
    public static void main(String[] args)
    {
        HashMap<String,Integer> hashMap = new HashMap<String,Integer>();
        hashMap.put("a",1);
        hashMap.put(null,1);
        hashMap.put("",1);
        Hashtable<String,Integer> hashtable = new Hashtable<String,Integer>();
        hashtable.put("",5);
        System.out.println(hashtable.get(""));
       // hashtable.put(null,1);
    }
}
