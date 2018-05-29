package sparkRDD

import org.apache.spark.{SparkConf, SparkContext}

/**
  * Created by zhangheng on 2017/9/7.
  * 键值对 ，操作
  *Spark中包含了键值对 类型的RDD提供 了一些转悠的操作。这些RDD被称为pair RDD
  * pair RDD 构成了很多程序的要素
  */
object sparkTestkey_value {
  def main(args: Array[String]): Unit = {

    //转化操作 （以键值对集合{（1,2） ，（3,4），（3,6）}）

    /*
    reduceByKey() 合并具有相同健的值，   {(1,2), (3,10)}
    groupByKey()  对具有相同健的值进行分组  {(1,[2]),(3, [4,6])}
    keys()  返回一个仅包含key 的RDD
    values() 返回一个仅包含值得RDD
    sortByKey() 返回一个根据健 排序的RDD
     */

    //聚合操作    当数据集以键值对形式组织的时候，聚合具有相同键的元素进行一些统计是很常见的操作。

// scala 实现  实现 单词计数
    //val result = words.map(x => (x, 1)).reduceByKey((x, y) => x + y)

    //创建一个Spark Context
    val conf = new SparkConf().setAppName("wordCount").setMaster("local")
    val sc = new SparkContext(conf)
    val data = Array(1,2,3,4,5,3,4,6,3,1,2)
    //集合中的元素被复制到 一个可并行操作 的分布式数据集中，
    val distData = sc.parallelize(data)

    //求 每个学生的平均成绩
    val initialScores = Array(("Fred", 88.0), ("Fred", 95.0), ("Fred", 91.0), ("Wilma", 93.0), ("Wilma", 95.0), ("Wilma", 98.0))
    val d1 = sc.parallelize(initialScores)
    type MVType = (Int, Double) //定义一个元组类型(科目计数器,分数)
    val pj = d1.combineByKey(
      score => (1, score),
      (c1: MVType, newScore) => (c1._1 + 1, c1._2 + newScore),
      (c1: MVType, c2: MVType) => (c1._1 + c2._1, c1._2 + c2._2)
    ).map { case (name, (num, socre)) => (name, socre / num) }.collect
    pj.foreach(println)


    //rdd 排序
    // rdd.sortByKey(ascending=True)  升顺 ，ascending=Fasle 降序
    //countByKey （）对每一个健对应的元素分别计数
    //lookup（key）返回给定健 对应的所有值






  }


}
