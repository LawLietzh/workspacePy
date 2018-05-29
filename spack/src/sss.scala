/**
  * Created by zhangheng on 2017/9/4.
  */

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import scala.io.Source


object sss {
  def main(args: Array[String]): Unit = {


    val conf= new SparkConf().setAppName("wordcount")
    val sc=new SparkContext(conf)
    val line=sc.textFile("E://数据资料//spark//rest.txt", 1)
    val word=line.flatMap(_.split(" "))
    val pairs=word.map(word => (word,1))
    val wordCounts=pairs.reduceByKey(_+_).map(x=>(x._2,x._1)).sortByKey(false, 1)
    val words=wordCounts.map(x=>x._2+":"+x._1+" ").foreach(println)
  }
}

