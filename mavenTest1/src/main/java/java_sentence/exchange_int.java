package java_sentence;
import java.util.ArrayList;
import java.util.List;


/**
 * Created by zhaoxinglei on 2018/1/10.
 *
 */
public class exchange_int {
    public static void main(String[] args){

        String strs="年今是什么年";
       /* String[] str_jn="年#年1#年2#年3".split("#");
        String[] str_n="今年#今年1#今年2#今年3".split("#");*/

        String[] str_jn="年今#年今1#年今2#年今3".split("#");
        String[] str_n="年#年1#年2#年3".split("#");

        List<String> list1=new ArrayList<String>();
        for (int i=1;i<str_jn.length;i++){
            for(int j=1;j<str_n.length;j++){
                String str=strs;
                StringBuilder sb=new StringBuilder(str_jn[i]);
                for(int ind=sb.length();ind>0;ind--){
                    sb.insert(ind,"%");
                }
                System.out.println(sb);
                String cha=sb.toString();
                String str1=str.replaceAll(str_jn[0],cha);
                //
                String res=new exchange_int().change(str1,cha,str_n[0],str_n[j]);
                list1.add(res);
            }
        }
        for (String s:list1
             ) {
            s=s.replaceAll("%","");
            System.out.println(s);
        }
    }
    public String change(String str1,String cha1,String s,String c){
        String res="";
        int index=0;
        StringBuilder sb=new StringBuilder(c);
        for(int ind=sb.length();ind>0;ind--){
            sb.insert(ind,"%");
        }
        String cha=sb.toString();
        while(!str1.equals("")){
            if(str1.indexOf(s)!=0){
                int index1=str1.indexOf(s);
                if(index1+1<str1.length()&&str1.charAt(index1+1)=='%'){
                    res+=str1.substring(0,str1.indexOf(cha1)+cha1.length());
                    str1=str1.substring(str1.indexOf(cha1)+cha1.length(),str1.length());
                }else{
                    res+=str1.substring(0,index1+1).replaceAll(s,cha);
                    str1=str1.substring(index1+1,str1.length());
                }
            }else{
                res=str1;
                break;
            }
        }
        return res;
    }
}
