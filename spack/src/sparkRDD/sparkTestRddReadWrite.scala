package sparkRDD

import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by zhangheng on 2017/9/8.
  * 练习spark 的读写   操作
  */
object sparkTestRddReadWrite {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("wordCount").setMaster("local")
    val sc = new SparkContext(conf)
    '''
    //读取文件
    val input = sc.textFile("E:/数据资料/spark/test1.txt")
    println(input.collect().mkString(","))
    println("dddddddddddddddddddddddddd")

    //返回 pair RDD。key为文件名，value为文件中的数据
    val inputfile = sc.wholeTextFiles("E:/数据资料/spark/read")
    println(inputfile.collect().mkString(","))

    //保存文件  saveAsTextFile
    var rdd1 = sc.makeRDD(1 to 10,2)
    rdd1.collect().foreach(println)
    '''
    val data = Array(1,2,3,4,5)
    //集合中的元素被复制到 一个可并行操作 的分布式数据集中，
    val distData = sc.parallelize(data)
    //System.setProperty("hadoop.home.dir", "E:/hadoop/bin/")
    distData.saveAsTextFile("E:/数据资料/spark/test64")


  }

}
