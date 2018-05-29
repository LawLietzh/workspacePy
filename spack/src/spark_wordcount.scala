/**
  * Created by zhangheng on 2017/9/4.
  */

import org.apache.spark._
import org.apache.spark.SparkContext
import scala.io.Source
import org.apache.spark.sql.SparkSession


object spark_wordcount {
  def main(args: Array[String]): Unit = {
    printf("ssssss")
    /*
    val spark=SparkSession.builder().appName("test").getOrCreate()
    val file=spark.sparkContext.textFile("E:/数据资料/spark/test.txt", 1).foreach(println)
    //val file=spark.sparkContext.textFile("test.txt", 1).foreach(println)
    spark.stop()
    */
    /*
       SparkContext 是Spark所有流操作的主要入口，用来告诉spark 如何访问集群，在创建SparkContext 之前，你需要构建一个SparkConf
       对象，包含了一些 你应用程序的信息。

     */
    val conf= new SparkConf().setAppName("wordcount")
    val sc=new SparkContext(conf)
    val line=sc.textFile("E:/数据资料/spark/test.txt", 1)
    val word=line.flatMap(_.split(" "))
    val pairs=word.map(word => (word,1))
    val wordCounts=pairs.reduceByKey(_+_).map(x=>(x._2,x._1)).sortByKey(false, 1)
    val words=wordCounts.map(x=>x._2+":"+x._1+" ").foreach(println)

  }
}
