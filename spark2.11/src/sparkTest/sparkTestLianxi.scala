package sparkTest
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import  org.apache.spark.mllib
/**
  * Created by zhangheng on 2017/10/26.
  *Spark 机器学习 第一张 1.1  到 1.3
  * RDD  resilient distributed  Dataset   弹性分布式数据集
  *
  */
object sparkTestLianxi {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("Simple Application").setMaster("local")
    val sc = new SparkContext(conf)
    val file = sc.textFile("D://woshi.txt")
    file.foreach(println)

    val line=sc.parallelize(List(1,2,3,4))
    val word=line.map{case x=>x+1}.foreach(println)

    val path = "D://woshi.txt"
    //读取文件
    val rddRromTextFile = sc.textFile(path )
    //计算每行长度
    val intsFromStringsRDD = rddRromTextFile.map(line =>line.size)
    //统计有多少行
    val numRecords = intsFromStringsRDD.count
    val sumOfRecords = intsFromStringsRDD.sum
    println(sumOfRecords)
    println(sumOfRecords/numRecords)


    //spark 主要有转换和执行操作   数据转换并不执行，只有执行操作被调用的时候，才会调用
    val transformedRDD = rddRromTextFile.map(line =>line.size).filter(size =>size>3).map(size => size*2)
    println(transformedRDD)//这个时候，并没有执行

    val computation = transformedRDD.sum()
    println(computation)


    //RDD 缓存策略  spark 最为强大的功能之一 就是能够把数据缓存在集群的内存里，可以通过RDD的 cache 函数来实现。
    //广播变量
    val broadcastAlist = sc.broadcast(List("a","b"))
    //把list 转为RDD  ，map 取出广播变量 使用value方法，让后和 list拼接
    val broadcastYingyong = sc.parallelize(List("1","2","3")).map(x => broadcastAlist.value ++ x)
    broadcastYingyong.collect()
    println(broadcastYingyong.take(3).mkString)

    println("spark 编程入门")
    //读取文件
    val data = sc.textFile("D://userpurchase.txt").map(line =>line.split(",")).map(pur => (pur(0),pur(1),pur(2)))
    //购买次数
    println(data.count())
    //求多少个不同的用户 购买过商品
    val uniqueUsers = data.map{case(user,product,price) =>user}.distinct().count()
    println(uniqueUsers)
    // 求和的中收入
    val totalRevenue = data.map{case(user,product,price) =>price.toDouble}.sum()
    println(totalRevenue)
    //求最畅销的商品是啥
    val productByPopularity = data.map{case(user,product,price) => (product,1)}.reduceByKey(_ + _).collect().sortBy(-_._2)
    val mostpopular = productByPopularity(0)








  }

}
