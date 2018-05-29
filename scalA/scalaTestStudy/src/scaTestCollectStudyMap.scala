/**
  * Created by zhangheng on 2017/9/2.
  */
object scaTestCollectStudyMap {
  def main(args: Array[String]): Unit = {

    val colors :Map[String,String] = Map("red" -> "#FF0000", "azure" -> "#F0FFFF")
    println(colors)
      //添加 键值对  对于不可变的map，是重新创建了一个新的map，元map表不变
    val ss = colors.+ ("red1" -> "#FF0000")
    println(ss)
    /*
    Scala Map 有三个基本操作：
    keys	返回 Map 所有的键(key)
    values	返回 Map 所有的值(value)
    isEmpty	在 Map 为空时返回true
     */
    //map 的遍历
    colors.keys.foreach{
      i => println("key = " + i)
        println("value = "+ colors.get(i))
    }

    //可以使用 Map.contains 方法来查看 Map 中是否存在指定的 Key

    //Tuple   我们可以使用 t._1 访问第一个元素， t._2 访问第二个元素，如下所示：
    val t = new Tuple1(1,2.1,"trr")
    //迭代元组
    t.productIterator.foreach{ i =>
      println("value = " + i )
    }

    //   Tuple.toString() 方法将元组的所有元素组合成一个字符串  "连接后的字符串为: " + t.toString() )

    val sites = Map("runoob" -> "www.runoob.com", "google" -> "www.google.com")

    println("sites.get( \"runoob\" ) : " +  (sites.get( "runoob" ))) // Some(www.runoob.com)
    println("sites.get( \"baidu\" ) : " +  sites.get( "baidu" ))  //  None



  }

}
