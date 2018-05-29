/**
  * Created by zhangheng on 2017/9/5.
  */
import org.apache.spark._
import org.apache.spark.SparkContext
import scala.io.Source
import org.apache.spark.sql.SparkSession
object sparkTestLianxi {
  def main(args: Array[String]): Unit = {
    printf("ssssss")

    /*
       SparkContext 是Spark所有流操作的主要入口，用来告诉spark 如何访问集群，在创建SparkContext 之前，你需要构建一个SparkConf
       对象，包含了一些 你应用程序的信息。

     */
    //setAppName()参数是你程序的名字，      setMaster（master） master，是spark，Mesos，Yarn 集群的URL，或运行在本地模式，使用专用字符串“local”
    //初始化 Spark
    //setMaster("local")  ：集群URL，告诉Spark如何连接到集群上在这几个例子中我们使用的是 local ，这个
    //特殊值可以让 Spark 运行在单机单线程上而无需连接到集群。
    val conf= new SparkConf().setAppName("wordcount").setMaster("local")
    val sc=new SparkContext(conf)
    val data = Array(1,2,3,4,5)
    //集合中的元素被复制到 一个可并行操作 的分布式数据集中，
    val distData = sc.parallelize(data)
    //一旦创建完成，这个分布式数据集，就可以被并行操作，例如，我们可以调用distData.reduce,将这个数组中的元素相加，
    val sum = distData.reduce((a,b) => a+b)
    println(sum)
    // 文本文件 RDDs 可以使用 SparkContext 的 textFile 方法创建。
    // 在这个方法里传入文件的 URI (机器上的本地路径或 hdfs://，s3n:// 等)，
    // 然后它会将文件读取成一个行集合。这里是一个调用例子：
    val line = sc.textFile("E:/数据资料/spark/test.txt")
    line.count()//统计RDD中元素（行）个数
    line.first()//第一行
//筛选
    val filters = line.filter(line =>line.contains("wo"))
    println("ffffffffffffffff")
    //返回过滤后的 数据
    println(filters.first(),filters.count)

    //一旦创建完成，distFile就能做数据集 操作，例如，我们可以使用下面的方式 使用 map  和reduce 来将所有行的长度相加
    //这个时候 lineLen并没有被执行，
    val lineLen = line.map(s => s.length)
    //如果我们想 再次使用lieLen 我们可以添加
    val sumlen = lineLen.persist()
    println(sumlen)
    val sumLeng = lineLen.reduce((a,b) => a+b)
    println("lllllllllllllllllllllllll")
    println(sumLeng)
    println("dddddddddddddd")
    val pairs = line.map(s => (s,1))
    val count = pairs.reduceByKey((a,b) => a+b)

    println(count)
    //关闭
    sc.stop()



    /*
    val line=sc.textFile("E:/数据资料/spark/test.txt", 1)
    val word=line.flatMap(_.split(" "))
    val pairs=word.map(word => (word,1))
    val wordCounts=pairs.reduceByKey(_+_).map(x=>(x._2,x._1)).sortByKey(false, 1)
    val words=wordCounts.map(x=>x._2+":"+x._1+" ").foreach(println)
    */

  }

}
