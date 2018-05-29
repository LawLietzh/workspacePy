/**
  * Created by zhangheng on 2017/10/18.
  */

import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
object ttt {
  def main(args: Array[String]): Unit = {
    val conf= new SparkConf().setAppName("wordcount")
    val sc=new SparkContext(conf)
    val line=sc.textFile("E://数据资料//spark//test.txt", 1)
    val word=line.flatMap(_.split(" "))
    val pairs=word.map(word => (word,1))
    val wordCounts=pairs.reduceByKey(_+_).map(x=>(x._2,x._1)).sortByKey(false, 1)
    val words=wordCounts.map(x=>x._2+":"+x._1+" ").foreach(println)
  }

}
