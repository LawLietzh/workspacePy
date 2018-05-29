package java_sentence;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/*
 * 笛卡尔积，生成相似句子
 * 修改一
 *
 */
public class sentenceCartesian {

    /*
    传入的参数 是List 列表，列表中 存的数据是： 第一个元素 是原始问句，
                                                第二个元素是 关键词#同义词#同意词
                                                第三。。。。
                                                第四。。。。
                                                第五。。。。
    list 的长度 最大为5

    输出：同义句列表  ，也是一个list

     */
public static List<String> similarSentences(List<String> args)
{
    List<String> similarList = new ArrayList<String>();
    List<String> argsList = args;
    //保证 每次argsList的长度都是5   一个句子，4个替换词，不够的用# 补全
    if(argsList.size()<5)
    {
        for(int i =argsList.size();i<5;i++ )
        {
            argsList.add("#");

        }
    }
   // System.out.println(argsList.size());
	   /*
	    * s1    lists1   类别
	    * s2    lists2   问题
	    * d     listd    答案
	    * k1   listk1  K1
	    *
	    * k2    listk2  K2
	    *
	    * k3   listk3  k3
	    * k4   listk4  k4
	    *
	    */


    String duiying = "";

    String wenti = argsList.get(0).trim();
    duiying = wenti;
    similarList.add(duiying);
    duiying = "";
    //先单独 遍历 替换 第一个k ，
    String[] strk1 = argsList.get(1).trim().split("#");
    if(strk1.length>=2)
    {

        for(int a = 1 ; a<strk1.length ;a++)
        {
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[a]);
            duiying = wentiXIN;

            similarList.add(duiying);
            duiying = "";
        }

    }

    //再单独 遍历 替换 第二个 K，
    String[] strk2 = argsList.get(2).trim().split("#");
    if(strk2.length>=2)

    {
        for(int a = 1 ; a<strk2.length ;a++)
        {
            String wentiXIN = wenti.replaceAll(strk2[0], strk2[a]);
            duiying = wentiXIN;

            similarList.add(duiying);
            duiying = "";
        }

    }

    //再单独 遍历 替换 第三个 K，
    String[] strk3 = argsList.get(3).trim().split("#");
    if(strk3.length>=2)
    {

        for(int a = 1 ; a<strk3.length ;a++)
        {
            String wentiXIN = wenti.replaceAll(strk3[0], strk3[a]);
            duiying = wentiXIN;

            similarList.add(duiying);
            duiying = "";
        }

    }

    //再单独 遍历 替换 第四个 K，
    String[] strk4 = argsList.get(4).trim().split("#");
    if(strk4.length>=2)
    {

        for(int a = 1 ; a<strk4.length ;a++)
        {
            String wentiXIN = wenti.replaceAll(strk4[0], strk4[a]);
            duiying = wentiXIN;

            similarList.add(duiying);
            duiying = "";
        }

    }

    //混合 替换   k1  和 k2
    if(strk1.length>=2 && strk2.length>=2)
    {

        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);
            for(int c = 1 ; c<strk2.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk2[c-1], strk2[c]);
                duiying = wentiXIN;

                similarList.add(duiying);
                wentiXIN = wentiXIN.replaceAll(strk2[strk2.length-1], strk2[0]);
                duiying = "";
            }
        }
    }

    //混合 替换   k1  和 k3
    if(strk1.length>=2 && strk3.length>=2)
    {

        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);
            for(int c = 1 ; c<strk3.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk3[c-1], strk3[c]);
                duiying = wentiXIN;

                similarList.add(duiying);
                wentiXIN = wentiXIN.replaceAll(strk3[strk3.length-1], strk3[0]);
                duiying = "";
            }
        }
    }

    //混合 替换   k1  和 k4
    if(strk1.length>=2 && strk4.length>=2)
    {

        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            System.out.println(wenti);

            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);

            System.out.println(wentiXIN);
            for(int c = 1 ; c<strk4.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk4[c-1], strk4[c]);
                duiying = wentiXIN;

                similarList.add(duiying);
                wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
                duiying = "";

            }
        }
    }

    //混合 替换   k2  和 k3
    if(strk2.length>=2 && strk3.length>=2)
    {

        for(int b = 1; b<strk2.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk2[0], strk2[b]);
            for(int c = 1 ; c<strk3.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk3[c-1], strk3[c]);
                duiying = wentiXIN;
                similarList.add(duiying);
                wentiXIN = wentiXIN.replaceAll(strk3[strk3.length-1], strk3[0]);
                duiying = "";
            }

        }
    }



    //混合 替换   k2  和 k4
    if(strk2.length>=2 && strk4.length>=2)
    {

        for(int b = 1; b<strk2.length;b++)
        {

            //混合替换
            String wentiXIN = wenti.replaceAll(strk2[0], strk2[b]);
            for(int c = 1 ; c<strk4.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk4[c-1], strk4[c]);
                duiying = wentiXIN;
                similarList.add(duiying);
                wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
                duiying = "";


            }
        }
    }

    //混合 替换   k3  和 k4
    if(strk3.length>=2 && strk4.length>=2)
    {

        for(int b = 1; b<strk3.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk3[0], strk3[b]);
            for(int c = 1 ; c<strk4.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk4[c-1], strk4[c]);
                duiying = wentiXIN;
                similarList.add(duiying);
                duiying = "";
                wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
            }
        }
    }

    //混合 替换   k1  和 k2  和 k3
    if(strk1.length>=2 && strk2.length>=2 && strk3.length>=2)
    {

        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);
            for(int c = 1 ; c<strk2.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk2[c-1], strk2[c]);
                for(int d = 1;d<strk3.length;d++)
                {
                    //System.out.println("&&&&"+wentiXIN);
                    wentiXIN = wentiXIN.replaceAll(strk3[d-1], strk3[d]);
                    duiying = wentiXIN;
                    similarList.add(duiying);
                    duiying = "";
                    // 添加这一句  为了让 第二次循环 替换的时候 回到原来替换之前
                    wentiXIN = wentiXIN.replaceAll(strk3[strk3.length-1], strk3[0]);
                }

            }

        }
    }


    //混合 替换   k1  和 k2  和 k4
    if(strk1.length>=2 && strk2.length>=2 && strk4.length>=2)
    {

        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);
            for(int c = 1 ; c<strk2.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk2[c-1], strk2[c]);
                for(int d = 1;d<strk4.length;d++)
                {
                    wentiXIN = wentiXIN.replaceAll(strk4[d-1], strk4[d]);
                    duiying = wentiXIN;
                    similarList.add(duiying);
                    wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
                    duiying = "";
                }
            }

        }
    }

    //混合 替换   k1  和 k3  和 k4
    if(strk1.length>=2 && strk3.length>=2 && strk4.length>=2)
    {


        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);
            System.out.println(wentiXIN);
            for(int c = 1 ; c<strk3.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk3[c-1], strk3[c]);

                for(int d = 1;d<strk4.length;d++)
                {
                    wentiXIN = wentiXIN.replaceAll(strk4[d-1], strk4[d]);
                    duiying = wentiXIN;

                    similarList.add(duiying);
                    wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
                    duiying = "";
                }
            }

        }
    }

    //混合 替换   k2  和 k3  和 k4
    if(strk2.length>=2 && strk3.length>=2 && strk4.length>=2)
    {

        for(int b = 1; b<strk2.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk2[0], strk2[b]);

            for(int c = 1 ; c<strk3.length ; c++)
            {

                wentiXIN = wentiXIN.replaceAll(strk3[c-1], strk3[c]);

                for(int d = 1;d<strk4.length;d++)
                {
                    wentiXIN = wentiXIN.replaceAll(strk4[d-1], strk4[d]);

                    duiying = wentiXIN;
                    similarList.add(duiying);

                    wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
                    duiying = "";
                }
            }

        }
    }

    //混合 替换   k1  和 k2  和 k3 和 k4
    if(strk1.length>=2 && strk2.length>=2 && strk3.length>=2 && strk4.length>=2 )
    {


        for(int b = 1; b<strk1.length;b++)
        {
            //混合替换
            String wentiXIN = wenti.replaceAll(strk1[0], strk1[b]);

            for(int c = 1 ; c<strk2.length ; c++)
            {
                wentiXIN = wentiXIN.replaceAll(strk2[c-1], strk2[c]);

                for(int d = 1;d<strk3.length;d++)
                {
                    wentiXIN = wentiXIN.replaceAll(strk3[d-1], strk3[d]);


                    for(int f = 1;f<strk4.length;f++)
                    {
                        wentiXIN = wentiXIN.replaceAll(strk4[f-1], strk4[f]);

                        duiying = wentiXIN;
                        similarList.add(duiying);
                        // 添加这一句  为了让 第二次循环 替换的时候 回到原来替换之前
                        wentiXIN = wentiXIN.replaceAll(strk4[strk4.length-1], strk4[0]);
                        duiying = "";
                    }
                   if(d == strk3.length-1)
                    {
                        wentiXIN = wentiXIN.replaceAll(strk3[strk3.length-1], strk3[0]);

                    }

                }



            }

        }
    }
    System.out.println("同义句扩展完毕！");
    return  similarList;

}


    public static void main(String[] args)  {


        List<String> aaa = new ArrayList<String>();
        aaa.add("aaa");
        aaa.add("aaa");
        aaa.add("aaa");
        aaa.add("bbb");
        Set set=new HashSet(aaa);

        System.out.println(set.toString());




        List<String> similarList = new ArrayList<String>();
       //例子展示
      /* List<String> argsList = new ArrayList<String>();
        argsList.add("如何设置支付密码？");
        argsList.add("如何#怎么#咋");
        argsList.add("设置#重置#设定#设立");
        argsList.add("支付密码#交易密码");*/

        List<String> argsList = new ArrayList<String>();
        argsList.add("今年 是 什么 年 " );

        argsList.add("今年#今年1#今年2#今年3#今年4#今年5");

        argsList.add("是#是1#是2#是3#是4#是5");
        argsList.add("什么#什么1#什么2#什么3#什么4#什么5");
        argsList.add("年#年1#年2#年3#年4#年5");

        similarList = similarSentences(argsList);
/*

        System.out.println(similarList.size());
        for(int i = 0;i<similarList.size();i++)
        {
            System.out.println(similarList.get(i));
        }

*/

    }

}
